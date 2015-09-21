SaltStack Proxy-Minion ROKU Module
==================================

This collection of modules is a proof of concept for the proxy-minion support
in SaltStack 2015.8.x. There was a lot of improvement done to the underlying
proxy-minion framework in this release. This collction of modules is my first
attempt to leverage the new framework and prove out some of the capabilities.

Note: these modules are primarily written against the API documentation found
here: http://sdkdocs.roku.com/display/sdkdoc/External+Control+Guide

Installation
------------

To install this set of modules first drop the `modules/` contents into
`_modules` and the `proxy/` contents into `_proxy`. Next, sync these modules
out to your minions using `salt '*' saltutil.sync_all`.

Service
-------

The `modules/roku_service.py` maps to the `service` module for eligible proxy
minions. This allows standard `service` commands, ie;

.. code-block:: shell

    salt '*' service.start

The `service.start` command maps to the Play/Pause button. This can be used to
Play or Pause a video.

.. code-block:: shell

    salt '*' service.stop

The `service.stop` command maps to the Play/Pause button. This can be used to
Play or Pause a video.

.. code-block:: shell

    salt '*' service.restart

The `service.restart` command maps to the InstantReplay button. This can be
used to trigger an Instant Replay a video.

Package
-------

The `modules/roku_pkg.py` maps to the `pkg` module for eligible proxy minions.
This allows the standard `pkg` commands, ie;

.. code-block:: shell

    salt '*' pkg.list_pkgs

The `pkg.list_pkgs` command maps to the `query/apps` API endpoint. This can be
used to list the names of installed channels.

Navigation
----------
