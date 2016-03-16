# archiveinstall

Takes the url of an archive (tar or zip) downloads it and extracts it to a location of your choice.
Depending on the configuration you pass additional environment and path variables are added.

## Release
python setup.py bdist_wheel
twine register -r test dist/*
twine upload -r test dist/*

set the new version in __init__.py
rm -Rf build dist
twine register -r pypi dist/*
twine upload -r pypi dist/*