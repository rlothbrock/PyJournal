import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("LICENSE", "r", encoding="utf-8") as lc:
    license__ = lc.read()


setuptools.setup(
    name="PyJournal-rlothbrock",
    version="0.0.1",
    author="rlothbrock",
    author_email="rlothbrock.10@gmail.com",
    description="A simple Python App for managing inventories and keep a small Store",
    long_description=long_description,
    license=license__,
    long_description_content_type="text/markdown",
    url="https://github.com/rlothbrock/PyJournal",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)