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
from selenium import webdriver
import os

logger = logging.getLogger("core.2018event")


class End(BrowserView):
    """ End """
    template = ViewPageTemplateFile('template/end.pt')

    def __call__(self):

        request = self.request

        portal = api.portal.get()
        if not self.request.get('HTTP_REFERER', '').startswith(portal.absolute_url()):
            self.request.response.redirect('%s?openExternalBrowser=1' % portal.absolute_url())
            return

        """
        import pdb; pdb.set_trace()
#        browser = webdriver.PhantomJS()
        browser = webdriver.Firefox()
        url = request.URL
        browser.set_window_size(400, 700)
        browser.get(url)

        browser.save_screenshot("/tmp/test.png")
        browser.close()
        """
        self.keys = {}
        self.keys['hat'], self.keys['scarf'], self.keys['phone'], self.keys['hand'], self.keys['clothes'], \
            self.keys['shoes'], self.keys['decoration'], self.keys['who'], self.keys['say'] = request.PATH_INFO.split('/')[-10:-1]
        return self.template()


class Talk(BrowserView):
    """ Talk """
    template = ViewPageTemplateFile('template/talk.pt')

    def __call__(self):

        request = self.request

        portal = api.portal.get()
        if not self.request.get('HTTP_REFERER', '').startswith(portal.absolute_url()):
            self.request.response.redirect('%s?openExternalBrowser=1' % portal.absolute_url())
            return

        self.keys = {}
#        import pdb; pdb.set_trace()
        self.keys['hat'], self.keys['scarf'], self.keys['phone'], \
            self.keys['hand'], self.keys['clothes'], self.keys['shoes'], self.keys['decoration'] = request.PATH_INFO.split('/')[-8:-1]
        return self.template()


class Image(BrowserView):
    """ Image """
    template = ViewPageTemplateFile('template/image.pt')

    def __call__(self):

        portal = api.portal.get()
        if not self.request.get('HTTP_REFERER', '').startswith(portal.absolute_url()):
            self.request.response.redirect('%s?openExternalBrowser=1' % portal.absolute_url())
            return
        return self.template()


class Index(BrowserView):
    """ Index """
    template = ViewPageTemplateFile('template/index.pt')

    def __call__(self):

        return self.template()
