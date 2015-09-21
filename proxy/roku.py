# -*- coding: utf-8 -*-
'''
This is a simple proxy-minion to manage ROKU devices

:maintainer: Christer Edwards (christer.edwards@gmail.com)
:maturity: 20150920
:depends: none
:platform: all
'''
from __future__ import absolute_import

# Import python libs
import logging
import salt.utils.http

__proxyenabled__ = ['roku']

LOG = logging.getLogger(__file__)

DETAILS = {}


def __virtual__():
    '''
    Only return if all the modules are available
    '''
    if salt.utils.http.query:
        return True
    else:
        return False


def init(opts):
    '''
    Every proxy module needs an 'init', though you can
    just put a 'pass' here if it doesn't need to do anything.
    '''
    LOG.debug('roku proxy init() called...')

    DETAILS['url'] = opts['proxy']['url']

    if not DETAILS['url'].endswith('/'):
        DETAILS['url'] += '/'


def ping():
    device = salt.utils.http.query(DETAILS['url'], decode_type='xml', decode=True)
    try:
        ret = device['dict'][1]['serialNumber']
    except KeyError:
        ret = 'No data returned from API'

    return ret


def package_list():
    '''
    List installed "packages", ie; channels
    '''
    channels = []
    uri = 'query/apps'
    device = salt.utils.http.query(DETAILS['url']+uri, decode_type='xml', decode=True)
    try:
        ret = device['dict']
        for app in ret:
            for key, val in app.items():
                channels.append(val)
    except KeyError:
        channels = 'No data returned from API'

    return channels


def service_stop():
    '''
    "stop" the service, ie; pause
    '''
    uri = 'keypress/Play'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def service_start():
    '''
    "start" the service, ie; play
    '''
    uri = 'keypress/Play'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def service_replay():
    '''
    Instant replay
    '''
    uri = 'keypress/InstantReplay'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def shutdown(opts):
    '''
    For this proxy shutdown is a no-op
    '''
    LOG.debug('roku proxy shutdown() called...')
    pass


def navigate_search():
    '''
    Navigate search
    '''
    uri = 'keypress/Search'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def navigate_home():
    '''
    Navigate home
    '''
    uri = 'keypress/Home'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def navigate_back():
    '''
    Navigate back
    '''
    uri = 'keypress/Back'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def navigate_select():
    '''
    Navigate select
    '''
    uri = 'keypress/Select'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def navigate_left():
    '''
    Navigate left
    '''
    uri = 'keypress/Left'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def navigate_right():
    '''
    Navigate right
    '''
    uri = 'keypress/Right'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def navigate_up():
    '''
    Navigate up
    '''
    uri = 'keypress/Up'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def navigate_down():
    '''
    Navigate down
    '''
    uri = 'keypress/Down'
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')


def navigate_input(search):
    '''
    Navigate search
    '''
    uri = 'keypress/Lit_'+search
    return salt.utils.http.query(DETAILS['url']+uri, method='POST')

