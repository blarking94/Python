# Allows us to specify our project configuration and to run packaging commands
# Classifiers allow us to specify intended audiance, topics, licences and compatible python versions
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="firstPackage",
    version="0.0.1",
    author="Ben Larking",
    author_email="ben@email.com",
    description="my First Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['cool'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)