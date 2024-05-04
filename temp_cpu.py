#!/usr/bin/env python3
#
#  temp_cpu.py
#
#  Copyright 2024 oldbear <oldbear@skinwalker>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


import gi
import gtk
import gobject
import os
from subprocess import Popen, PIPE
import fcntl

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

tempOutput = os.popen("cat temp.txt").read()

def on_activate(app):	
    win = Gtk.Window(application=app)
    win.set_title(title="CPUs-T")
    win.set_default_size(250, 80)
    win.box = Gtk.Box(spacing=3)
    os.popen("echo "" > temp.txt").read()
    os.popen("sysctl dev.cpu | grep temp > temp.txt").read()
    label = Gtk.Label(label = "%s" % tempOutput)
    win.set_child(label)
    win.present()
app = Gtk.Application()
app.connect('activate', on_activate)
app.run(None)


