from setuptools import setup

setup(
    name='csvToSql',
    version='0.1',
    py_modules=['csvToSql'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        csvToSql=csvToSql:generate_sql
    ''',
)
