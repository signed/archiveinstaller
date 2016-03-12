import unittest
from archiveinstaller.installer import ArchiveConfiguration
from archiveinstaller.installer import EnvironmentConfiguration
from unittest import TestCase

from hamcrest import *
from archiveinstaller.installer import Application


class ApplicationTest(TestCase):
    archive = {'url': 'http://example.org/artifact-%(version)s'}
    application = Application("do_not_care", '1.2.3', ArchiveConfiguration(archive), EnvironmentConfiguration({}))

    def test_replace_version_in_url(self):
        assert_that(self.application.url(), all_of(
            contains_string('1.2.3'),
            not_(contains_string('%(version)s'))))

    def test_replace_version_in_filename(self):
        assert_that(self.application.filename(), all_of(
            contains_string('1.2.3'),
            not_(contains_string('%(version)s'))))

if __name__ == '__main__':
    unittest.main()
