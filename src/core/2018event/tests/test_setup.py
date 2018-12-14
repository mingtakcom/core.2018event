# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from core.2018event.testing import CORE_2018EVENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that core.2018event is properly installed."""

    layer = CORE_2018EVENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if core.2018event is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'core.2018event'))

    def test_browserlayer(self):
        """Test that ICore2018EventLayer is registered."""
        from core.2018event.interfaces import (
            ICore2018EventLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICore2018EventLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CORE_2018EVENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['core.2018event'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if core.2018event is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'core.2018event'))

    def test_browserlayer_removed(self):
        """Test that ICore2018EventLayer is removed."""
        from core.2018event.interfaces import \
            ICore2018EventLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICore2018EventLayer,
            utils.registered_layers())
