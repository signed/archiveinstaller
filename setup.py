import codecs
import os
import re

from setuptools import setup, find_packages

###############################################################################

NAME = "archive-installer"
PACKAGES = find_packages(where="src")
META_PATH = os.path.join("src", "archiveinstaller", "__init__.py")
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7"
]
INSTALL_REQUIRES = ['requests', 'ndg-httpsclient', 'pathlib2']
TEST_REQUIRES = ['mock', 'PyHamcrest']
LONG_DESCRIPTION="""archiveinstaller
================

Takes the url of an archive (tar or zip) downloads it and extracts it to a location of your choice.
Depending on the configuration you pass additional environment and path variables are added.
"""

###############################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
            r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
            META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))

if __name__ == "__main__":
    setup(
            name=NAME,
            description=find_meta("description"),
            license=find_meta("license"),
            url=find_meta("uri"),
            version=find_meta("version"),
            author=find_meta("author"),
            author_email=find_meta("email"),
            maintainer=find_meta("author"),
            maintainer_email=find_meta("email"),
            long_description=LONG_DESCRIPTION,
            packages=PACKAGES,
            package_dir={"": "src"},
            zip_safe=False,
            classifiers=CLASSIFIERS,
            install_requires=INSTALL_REQUIRES,
            tests_require=TEST_REQUIRES,
            package_data={
                'archiveinstaller.shell': ['application.sh'],
            },
            include_package_data=True,
    )
