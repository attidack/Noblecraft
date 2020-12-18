from setuptools import setup

setup(
    name='Noblecraft',
    version='1',
    packages=['migrations', 'migrations', 'migrations', 'migrations', 'migrations', 'pages', 'pages.migrations',
              'register', 'register.migrations', 'dashboard', 'dashboard.migrations', 'inventory',
              'inventory.migrations', 'Noblecraft', 'production', 'production.migrations'],
    package_dir={'': 'production'},
    url='http://159.65.71.111',
    license='For use at noblecraft',
    author='Jon Bird',
    author_email='attidack@gmail.com',
    description='Inventory database for Noblecraft'
)
