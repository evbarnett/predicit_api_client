import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='predictit-client',
    version='0.2',
    author="github.com/evbarnett",
    author_email="evbarnett@protonmail.com",
    description="Client API wrapper for PredictIt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evbarnett/predicit-client",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
)
