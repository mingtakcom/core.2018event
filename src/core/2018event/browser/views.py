# -*- coding: utf-8 -*-
#from core.2018event import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

import base64
import requests
import logging

logger = logging.getLogger("core.2018event")


class Talk(BrowserView):
    """ Talk """
    template = ViewPageTemplateFile('template/talk.pt')

    def __call__(self):

        request = self.request
        self.keys = {}
        self.keys['hat'], self.keys['scarf'], self.keys['phone'], \
            self.keys['hand'], self.keys['clothes'], self.keys['shoes'], self.keys['decoration'] = request.PATH_INFO.split('/')[2:9]
        return self.template()


class Image(BrowserView):
    """ Image """
    template = ViewPageTemplateFile('template/image.pt')

    def __call__(self):

        return self.template()


class Index(BrowserView):
    """ Index """
    template = ViewPageTemplateFile('template/index.pt')

    def __call__(self):

        return self.template()
