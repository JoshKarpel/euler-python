from setuptools import setup

setup(
    name = 'euler',
    version = '0.1.0',
    py_modules = ['euler', 'problems'],
    package_data = {'': 'answers.txt'},
    include_package_data = True,
    install_requires = [
        'click',
    ],
    entry_points = '''
        [console_scripts]
        euler=euler:cli
    ''',
)
