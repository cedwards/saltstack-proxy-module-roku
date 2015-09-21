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
__virtualname__ = 'pkg'


def __virtual__():
    '''
    Only work on proxy
    '''
    if 'proxymodule' in __opts__:
        return __virtualname__
    return False


def list_pkgs(versions_as_list=False, **kwargs):
    return __opts__['proxymodule']['roku.package_list']()


def install(name=None, refresh=False, fromrepo=None,
            pkgs=None, sources=None, **kwargs):
    return __opts__['proxymodule']['rest_sample.package_install'](name, **kwargs)


def remove(name=None, pkgs=None, **kwargs):
    return __opts__['proxymodule']['rest_sample.package_remove'](name)


def version(*names, **kwargs):
    '''
    Returns a string representing the package version or an empty string if not
    installed. If more than one package name is specified, a dict of
    name/version pairs is returned.

    CLI Example:

    .. code-block:: bash

        salt '*' pkg.version <package name>
        salt '*' pkg.version <package1> <package2> <package3> ...
    '''
    if len(names) == 1:
        return str(__opts__['proxymodule']['rest_sample.package_status'](names[0]))


def installed(
        name,
        version=None,
        refresh=False,
        fromrepo=None,
        skip_verify=False,
        pkgs=None,
        sources=None,
        **kwargs):

    p = __opts__['proxymodule']['rest_sample.package_status'](name)
    if version is None:
        if 'ret' in p:
            return str(p['ret'])
        else:
            return True
    else:
        if p is not None:
            return version == str(p)
