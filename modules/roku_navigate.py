# -*- coding: utf-8 -*-
'''
Navigation support for the ROKU module

:maintainer: Christer Edwards (christer.edwards@gmail.com)
:maturity: 20150920
:depends: none
:platform: all
'''
from __future__ import absolute_import

import urllib
import logging


LOG = logging.getLogger(__name__)

__proxyenabled__ = ['roku']
__virtualname__ = 'roku'


def __virtual__():
    '''
    Only work on proxy
    '''
    if 'proxymodule' in __opts__:
        return __virtualname__
    return False


def search():
    return __opts__['proxymodule']['roku.navigate_search']()


def home():
    '''
    Navigate to the Home screen
    '''
    return __opts__['proxymodule']['roku.navigate_home']()


def back():
    '''
    Navigate using the Back button
    '''
    return __opts__['proxymodule']['roku.navigate_back']()


def select():
    '''
    Navigate using the Select button
    '''
    return __opts__['proxymodule']['roku.navigate_select']()


def left():
    '''
    Navigate using the Left button
    '''
    return __opts__['proxymodule']['roku.navigate_left']()


def right():
    '''
    Navigate using the Right button
    '''
    return __opts__['proxymodule']['roku.navigate_right']()


def up():
    '''
    Navigate using the Up button
    '''
    return __opts__['proxymodule']['roku.navigate_up']()


def down():
    '''
    Navigate using the Down button
    '''
    return  __opts__['proxymodule']['roku.navigate_down']():


def input(search):
    '''
    Input text using the Input field
    '''
    data = urllib.quote_plus(search)
    for i in data:
        __opts__['proxymodule']['roku.navigate_input'](i)

