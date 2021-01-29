# type: ignore

'''
Fastapi sqlalchemy-async
--------------
'''
from setuptools import setup
from toml import load

pyproject = load('pyproject.toml')
long_description = open('README.md', 'r').read()

setup_info = pyproject.get('tool').get('poetry')

setup(
    name='fastapi-sqlalchemy-async',
    version=setup_info.get('version'),
    url='https://github.com/uselessscat/fastapi-sqlalchemy-async',
    project_urls={
        'Code': 'https://github.com/uselessscat/fastapi-sqlalchemy-async',
        'Issues': 'https://github.com/uselessscat/fastapi-sqlalchemy-async/issues',
    },
    license='MIT',
    author='Ariel Carvajal',
    author_email='arie.cbpro@gmail.com',
    description=setup_info.get('description'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[p.get('include') for p in setup_info.get('packages')],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=setup_info.get('dependencies').keys(),
    extras_require={
        'postgresql': ['asyncpg'],
        'mysql': ['aiomysql'],
        'sqlite': ['aiosqlite'],
        'postgresql+aiopg': ['aiopg']
    },
    tests_require=setup_info.get('dev-dependencies').keys(),
    test_suite='tests',
    classifiers=setup_info.get('classifiers'),
)
