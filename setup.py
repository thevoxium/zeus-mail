from setuptools import setup

setup(
    name='zeus',
    version='0.1',
    py_modules=['zeus'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        zeus=zeus:cli
    ''',
)
