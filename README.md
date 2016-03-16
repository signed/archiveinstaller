# archiveinstall

Takes the url of an archive (tar or zip) downloads it and extracts it to a location of your choice.
Depending on the configuration you pass additional environment and path variables are added.

## Release
1. python setup.py bdist_wheel
1. twine register -r test dist/*
1. twine upload -r test dist/*
1. test locally
1. pip install --index-url https://testpypi.python.org/pypi --extra-index-url https://pypi.python.org/simple archive-installer
1. set the new version in __init__.py
1. rm -Rf build dist
1. twine register -r pypi dist/*
1. twine upload -r pypi dist/*