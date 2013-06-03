Apple Keyboard Toggle Plugin for Cuttlefish
===========================================

Intro
-----
Currently swaps the Left Alt and Left Win (Super) key automatically for users
of an Apple-style external keyboard. Needs to be configured with the appropriate
Cuttlefish Events.

Requirements
------------
Should work on any Gnome-based window manager in a recent Ubuntu-based distro.

You'll need to install Cuttlefish (https://launchpad.net/cuttlefish). As
Cuttlefish only exists in the Ubuntu 12.04 repos you can add the PPA manually
to your ``/etc/apt/sources.list`` ::

    deb http://ppa.launchpad.net/noneed4anick/cuttlefish/ubuntu precise main
    deb-src http://ppa.launchpad.net/noneed4anick/cuttlefish/ubuntu precise main

And install via: ::

    $ sudo apt-get update
    $ sudo apt-get install cuttlefish


Plugin Setup
------------
Copy or symlink ``apple_kb_toggle.py`` to your ``~/.cuttlefish/plugins/``
directory and reload your user plugins (``Ctrl+R``
or Edit -> Plugins -> Reload Plugins)

1. Add an Event for plugging in an Apple-layout keyboard and set the Reaction
   to "Apple Keyboard Layout Enable".
2. Add another Event for removal of the device and set the Reaction to
   "Apple Keyboard Layout Reset". This will restore your previous settings
   (warning: this will clobber settings changed since the first event was
   triggered!)

