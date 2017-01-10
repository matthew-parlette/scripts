Overview
========

This script searches the Sports Reporters RSS feed for an hour of the show to play it on the sonos

Prerequisites
=============

This relies on the `sonos` script in `../sonos`

Installation
============

    $ sudo pip install -r requirements.txt

Usage
=====

Play hour 1 for yesterday
---------------------

This searches every five minutes until the link is available.

    $ sports-reporters --yesterday --hour 1

Play hour 3 from Jan 9
----------------------

Date format is from the feed

    $ sports-reporters --date 01-9-2016

Play hour 2 from today if it exists
-----------------------------------

This will search the feed once. If the link it found, it will play. If not, the script exits.

    $ sports-reporters --hour 2 --exit-if-not-found
