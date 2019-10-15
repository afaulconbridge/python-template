from setuptools import setup

setup(
    name='TODO',
    version='1.0.0',
    author='Adam Faulconbridge',
    author_email='afaulconbridge@googlemail.com',
    packages=['TODO',],
    description='TODO.',
    long_description=open('README.txt').read(),
    install_requires = [
        'requests'
    ],
    extras_require = {
        'dev': ['pytest-cov', 'flake8', 'pip-tools'],
    },
    entry_points={
        'console_scripts': ['TODO=TODO:main'],
    },
)

