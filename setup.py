from distutils.core import setup

setup(
    name='django-storage-migrate',
    version='0.1',
    packages=['storages.commands', 'storages.commands.management', 'storages.commands.management.commands'],
    url='https://github.com/Krukov/django-storages-migrate',
    license='MIT',
    author='krukov.dv',
    author_email='frog-king69@yandex.ru',
    description='Django command for upload media files from local into storage (for django-storages)'
)
