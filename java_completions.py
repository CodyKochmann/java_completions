# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-08-01 12:59:22
# @Last Modified 2016-08-01 Your Name>
# @Last Modified time: 2016-08-01 13:00:05

# auto updater for sublime text 2

import sys

package_name = 'java_completions'

def plugin_loaded():
    from package_control import events

    if events.install(package_name):
        print('Installed %s!' % events.install(package_name))
    elif events.post_upgrade(package_name):
        print('Upgraded to %s!' % events.post_upgrade(package_name))


def plugin_unloaded():
    from package_control import events

    if events.pre_upgrade(package_name):
        print('Upgrading from %s!' % events.pre_upgrade(package_name))
    elif events.remove(package_name):
        print('Removing %s!' % events.remove(package_name))


# Compat with ST2
if sys.version_info < (3,):
    plugin_loaded()
    unload_handler = plugin_unloaded
