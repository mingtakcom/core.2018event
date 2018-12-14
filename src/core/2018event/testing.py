# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import core.2018event


class Core2018EventLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=core.2018event)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'core.2018event:default')


CORE_2018EVENT_FIXTURE = Core2018EventLayer()


CORE_2018EVENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CORE_2018EVENT_FIXTURE,),
    name='Core2018EventLayer:IntegrationTesting',
)


CORE_2018EVENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CORE_2018EVENT_FIXTURE,),
    name='Core2018EventLayer:FunctionalTesting',
)


CORE_2018EVENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CORE_2018EVENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='Core2018EventLayer:AcceptanceTesting',
)
