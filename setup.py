from setuptools import setup

setup(
    name="TODO",
    version="1.0.0",
    author="Adam Faulconbridge",
    author_email="afaulconbridge@googlemail.com",
    packages=["TODO"],
    description="TODO.",
    long_description=open("README.md").read(),
    install_requires=[""],
    extras_require={
        "dev": [
            "pytest-cov",
            "flake8",
            "black",
            "pylint",
            "pip-tools",
            "pipdeptree",
            "pre-commit",
        ],
    },
)
