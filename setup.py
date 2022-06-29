from setuptools import setup

setup(
    name="TODO",
    version="1.0.0",
    author="Adam Faulconbridge",
    author_email="afaulconbridge@googlemail.com",
    packages=["TODO"],
    description="TODO.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/afaulconbridge/todo",
    install_requires=open("requirements.txt").readlines(),
    extras_require={
        "dev": open("requirements-dev.txt").readlines(),
    },
)
