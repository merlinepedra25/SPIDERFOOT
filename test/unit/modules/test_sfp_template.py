import pytest
import unittest

from modules.sfp_template import sfp_template
from sflib import SpiderFoot


@pytest.mark.usefixtures
class TestModuleTemplate(unittest.TestCase):

    def test_opts(self):
        module = sfp_template()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        sf = SpiderFoot(self.default_options)
        module = sfp_template()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_template()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_template()
        self.assertIsInstance(module.producedEvents(), list)
