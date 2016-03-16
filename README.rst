# archiveinstall

Takes the url of an archive (tar or zip) downloads it and extracts it to a location of your choice.
Depending on the configuration you pass additional environment and path variables are added.

## Installation

to be done

## Development

## Release
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest
python setup.py bdist_wheel upload

