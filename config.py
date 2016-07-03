# -*- coding: utf-8 -*-

##
## usage:
##   from config import config
##


import sys, os


##
## get $APP_MODE
##
app_mode = os.environ.get('APP_MODE')
if not app_mode:
    sys.stderr.write(r"""
***
*** [ERROR] $APP_MODE is not set.
*** You must set $APP_MODE environment variable.
*** Example:
***
***   $ export APP_MODE='development'  # or 'production', 'staging'
***
"""[1:])
    sys.exit(1)


##
## import configs/config_xxx.py
##
try:
    mod = __import__('configs.config_'+app_mode, fromlist=('configs',))
except ImportError as ex:
    sys.stderr.write(r"""
***
*** [ERROR] failed to import 'configs/config_%s.py'. Does it exist?
***
"""[1:] % app_mode)
    sys.exit(1)


##
## create config object
##
config = mod.Config()


##
## load private config
##
try:
    from configs import config_private
except ImportError:
    sys.stderr.write(r"""
***
*** [ERROR] failed to import 'configs/config_private.py'.
*** If you have not created it yet, please create it at first.
*** Example:
***   $ cp configs/config_private.py.sample configs/config_private.py
***   $ vi configs/config_private.py
***
"""[1:])
    sys.exit(1)
config_private.update_config(config)


##
## delete variables
##
del sys, os
del app_mode, mod, config_private

