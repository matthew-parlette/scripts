Overview
=========

Listen for dash button presses and create a trello card based on what button was pressed.

Installation
============

    $ sudo pip install -r requirements.txt

This is best to run as a daemon, to do this, add a symlink:

    $ sudo ln -s /path/to/scripts/handle-dash-press.conf /etc/init/handle-dash-press.conf

And start it:

    $ sudo initctl reload-configuration
    $ sudo start handle-dash-press

Usage
=====

Start dash handler
------------------

    $ handle-dash-press
