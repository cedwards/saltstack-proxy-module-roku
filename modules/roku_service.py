# -*- coding: utf-8 -*-
'''
Package support for the ROKU module

:maintainer: Christer Edwards (christer.edwards@gmail.com)
:maturity: 20150920
:depends: none
:platform: all
'''
from __future__ import absolute_import

# Import python libs
import logging


LOG = logging.getLogger(__name__)

__proxyenabled__ = ['roku']
__virtualname__ = 'service'


def __virtual__():
    '''
    Only work on proxy
    '''
    if 'proxymodule' in __opts__:
        return __virtualname__
    return False


def stop():
    if '{}' in __opts__['proxymodule']['roku.service_stop']():
        return True


def start():
    if '{}' in  __opts__['proxymodule']['roku.service_start']():
        return True


def replay():
    return __opts__['proxymodule']['roku.service_replay']()

