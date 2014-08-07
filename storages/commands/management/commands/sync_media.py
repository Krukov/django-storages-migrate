# -*- coding: utf-8 -*-
import os
import logging
from optparse import make_option

from django.conf import settings
from django.db import transaction
from django.core.management.base import AppCommand
from django.core.files.storage import FileSystemStorage, DefaultStorage
from django.core.files import File


logger = logging.getLogger(__name__)


class Command(AppCommand):
    help = 'Migrate media files from local media dir into storage (used only with django-storages)'
    option_list = AppCommand.option_list + (
        make_option('-r', '--remove', dest='remove', action='store_true', default=False,
                    help='Remove local files after migrate'),
        make_option('-f', '--field', dest='field'),
        make_option('-m', '--model', dest='model'),
    )

    def handle_app(self, app, **options):

        if not options.get('model') or not options.get('field'):
            raise Exception('Specify model and field options')

        model = getattr(app, options.get('model').capitalize())
        field = options.get('field')
        with transaction.atomic():
            for instance in model.objects.filter(**{'%s__gte' % field: 0}):
                file_obj = getattr(instance, field)

                if 'storages.backends' not in settings.DEFAULT_FILE_STORAGE \
                        and isinstance(file_obj.storage, DefaultStorage):
                    raise Exception('Field storage must be not Default')
                file_path = FileSystemStorage().path(file_obj.name)

                if os.path.exists(file_path):
                    _file = File(open(file_path))
                    file_obj.save(os.path.basename(file_path), _file)

                    if options.get('remove'):
                        os.unlink(file_path)

                    logger.info('File %s for object %s(id=%s, model=%s) successfully uploaded into S3 storage - %s',
                                file_path, instance, instance.pk, model.__name__, file_obj.url)

                else:
                    logger.warning('File %s for object %s(id=%s, model=%s) doesn\'t exists',
                                   file_path, instance, instance.pk, model.__name__)
