# scripts

## bootstrap

### python

Generate a simple, single file python script with:

* command line parameters (for debug and config-file)
* configuration saved/loaded with yaml

    $ bootstrap-python myscript.py

Generate a multi-file python program in the current directory with:

* command line parameters (for debug and config-file)
* configuration saved/loaded with yaml
* plugin framework

    $ bootstrap-python -p myscript.py

## *-screen-blank

These two scripts will enable or disable the screen blanking in X. This is used in i3 or on the Raspberry Pi.

```
$ disable-screen-blank  # Screen is always on
$ enable-screen-blank  # Screen will blank after a timeout
```
