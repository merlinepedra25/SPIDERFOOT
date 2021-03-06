import pytest
import unittest

from modules.sfp_opencorporates import sfp_opencorporates
from sflib import SpiderFoot


@pytest.mark.usefixtures
class TestModuleOpencorporates(unittest.TestCase):

    def test_opts(self):
        module = sfp_opencorporates()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        sf = SpiderFoot(self.default_options)
        module = sfp_opencorporates()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_opencorporates()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_opencorporates()
        self.assertIsInstance(module.producedEvents(), list)
