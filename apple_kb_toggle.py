"""
Plugin for Cuttlefish

When configured via cuttlefish GUI it allows automatic enable/disable of the
Left Alt/Left Win key swap so that external Apple keyboards don't need manual
setup every time.
"""
### BEGIN LICENSE
# Copyright (C) 2013 Matt Stevenson <mattoc@mattoc.com>
# http://mattoc.com | http://github.com/mattoc
# 
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE
import ast
import os
import shlex
import subprocess

from cuttlefish.actions import CuttleAction
from cuttlefish.plugins import CuttlePlugin
from cuttlefish.params import StringParam


OPT_PATH = os.path.expanduser(os.path.join('~', '.cuttlefish', 'apple_kb_options.txt'))

def save_current_layout():
    command = 'gsettings get org.gnome.libgnomekbd.keyboard options' 
    opts = subprocess.check_output(shlex.split(command))

    with open(OPT_PATH, 'w') as f:
        f.write(opts)


def get_layout():
    """Get current GNOME keyboard layout options and (if necessary) save them"""
    if os.path.isfile(OPT_PATH):
        with open(OPT_PATH, 'r') as f:
            opts = f.read()

            if opts.strip():  # check for empty-ish file
                return opts.rstrip()  # file can have newlines trailing

    # save it then run again
    save_current_layout()

    return get_layout()


def set_layout(layout):
    subprocess.call(shlex.split('gsettings set org.gnome.libgnomekbd.keyboard options "%s"' % layout))


class AppleKeyboardEnable(CuttleAction, CuttlePlugin):
    NAME = "Apple Keyboard Layout Enable"
    DESCP = "Swaps Left Alt + Win key for external Apple-style keyboards"
    CATEGORY = "Keyboard Layouts"
    PARAMS = {
        'options': get_layout(),
    }

    class Editor(CuttlePlugin.Editor):
        ORDER = ['options',]

        def begin(self):
            return {
                'options': StringParam('Existing keyboard layout options'),
            }

    def __init__(self):
        CuttleAction.__init__(self)
        CuttlePlugin.__init__(self)

    def execute(self):
        # Parse from string literal to Python list (cheeky and fragile)
        options = ast.literal_eval(self.PARAMS['options'])

        options.append('altwin\taltwin:swap_lalt_lwin')

        layout = "['%s']" % "','".join(options)
        set_layout(layout)


class AppleKeyboardDisable(CuttleAction, CuttlePlugin):
    NAME = "Apple Keyboard Layout Reset"
    DESCP = "Restores previous keyboard layout"
    CATEGORY = "Keyboard Layouts"

    def __init__(self):
        CuttleAction.__init__(self)
        CuttlePlugin.__init__(self)

    def execute(self):
        set_layout(get_layout())

