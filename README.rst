Apple Keyboard Toggle Plugin for Cuttlefish
===========================================

You'll need to install Cuttlefish (https://launchpad.net/cuttlefish)

#TODO: elaborate; it's only in the 12.04 repos

Plugin Setup
------------
Copy or symlink `apple_kb_toggle.py` to your `~/.cuttlefish/plugins/` directory
and reload your user plugins (``Ctrl+R`` or Edit -> Plugins -> Reload Plugins)

1. Add an Event for plugging in an Apple-layout keyboard and set the Reaction
   to "Apple Keyboard Layout Enable".
2. Add another Event for removal of the device and set the Reaction to
   "Apple Keyboard Layout Reset". This will restore your previous settings
   (warning: this will clobber settings changed since the first event was
   triggered!)

