Installation
============

    $ sudo pip install -r requirements.txt

Usage
=====

Play hour 1 for today
---------------------

This searches every five minutes until the link is available.

    $ czaban --hour 1

Play hour 3 from Jan 9
----------------------

Date format is from http://www.podcastarena.com/czaban/

    $ czaban --date 1-9-2016

Play hour 2 if it exists
------------------------

This will search the site once. If the link it found, it will play. If not, the script exits.

    $ czaban --hour 2 --exit-if-not-found
