from distutils.core import setup

setup(
    name='django-storage-migrate',
    version='0.1',
    packages=['storages.commands', 'storages.commands.management', 'storages.commands.management.commands'],
    url='',
    license='MIT',
    author='krukov.dv',
    author_email='frog-king69@yandex.ru',
    description='Media files migrate command'
)
