#!/usr/bin/python

import argparse
import logging
import os
import yaml

from plugin import PluginMount, PluginProvider

global config

def merge(x,y):
    # store a copy of x, but overwrite with y's values where applicable
    merged = dict(x,**y)

    xkeys = x.keys()

    # if the value of merged[key] was overwritten with y[key]'s value
    # then we need to put back any missing x[key] values
    for key in xkeys:
        # if this key is a dictionary, recurse
        if isinstance(x[key],dict) and y.has_key(key):
            merged[key] = merge(x[key],y[key])

    return merged

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process command line options.')
    parser.add_argument('-d','--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('-c','--config-file', help='Specify a config file to use',
                        type=str, default='config.yaml')
    parser.add_argument('--version', action='version', version='0')
    args = parser.parse_args()

    # Setup logging options
    log_level = logging.DEBUG if args.debug else logging.INFO
    log = logging.getLogger(os.path.basename(__file__))
    log.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(funcName)s(%(lineno)i):%(message)s')

    ## Console Logging
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(formatter)
    log.addHandler(ch)

    ## File Logging
    fh = logging.FileHandler(os.path.basename(__file__) + '.log')
    fh.setLevel(log_level)
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info("Initializing...")

    log.info("Loading configuration...")
    # Load Config
    global config
    defaults = {
        # "setting": "value",
    }
    if os.path.isfile(args.config_file):
        log.debug("Loading config file %s" % args.config_file)
        config = yaml.load(file(args.config_file))
        if config:
            # config contains items
            config = merge(defaults,yaml.load(file(args.config_file)))
            log.debug("Config merged with defaults")
        else:
            # config is empty, just use defaults
            config = defaults
            log.debug("Config file was empty, loaded config from defaults")
    else:
        log.debug("Config file does not exist, creating a default config...")
        config = defaults

    log.debug("Config loaded as:\n%s, saving this to disk" % str(config))
    with open(args.config_file, 'w') as outfile:
        outfile.write( yaml.dump(config, default_flow_style=False) )
    log.debug("Config loaded as %s" % str(config))
    log.info("Configuration loaded")

    log.info("Loading plugins...")
    from plugins import *
    global plugins
    plugins = [p(log, config) for p in PluginProvider.plugins]
    log.debug("Plugins loaded as %s" % str(plugins))
    log.info("Plugins loaded")

    log.info("Initialization complete")
