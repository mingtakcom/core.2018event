# -*- coding: utf-8 -*-
#from core.2018event import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

#import base64
import requests
import logging
from selenium import webdriver
from pyvirtualdisplay import Display
import random
import os

logger = logging.getLogger("core.2018event")


class GetImg(BrowserView):
    """ GetImg """

    def __call__(self):

        request = self.request

        # get webpage capture start
#        filename = '%s.png' % random.randint(1, 999999999)
        filename = request.form.get('fn')
        url = 'http://localhost:9401/core2018xmas/%s?getimg' % request.VIRTUAL_URL_PARTS[1].replace('getimg', 'end')
        os.system('python /home/andy/getimg.py %s %s' % (url, filename))
        # get webpage capture end

        return


class End(BrowserView):
    """ End """
    template = ViewPageTemplateFile('template/end.pt')

    def __call__(self):

        request = self.request

        portal = api.portal.get()
#        if not self.request.get('HTTP_REFERER', '').startswith(portal.absolute_url()):
#            self.request.response.redirect('%s?openExternalBrowser=1' % portal.absolute_url())
#            return

        self.filename = '%s.png' % random.randint(1, 999999999)
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
            self.request.response.redirect('%s/index' % portal.absolute_url())
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
            self.request.response.redirect('%s/index' % portal.absolute_url())
            return
        return self.template()


class Index(BrowserView):
    """ Index """
    template = ViewPageTemplateFile('template/index.pt')

    def __call__(self):

        self.filename = self.request.form.get('fn')
        return self.template()
