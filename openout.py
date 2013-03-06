#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple logout menu written in Python and Gtk+ 3.

It supports the following window managers:

o PekWM
o Openbox
o Fluxbox
o JWM
o FVWM
o IceWM
o WindowMaker

"""

__author__ = "Germán A. Racca"
__copyright__ = "Copyright (C) 2013, Germán A. Racca"
__email__ = "gracca@gmail.com"
__license__ = "GPLv3+"
__version__ = "0.1"

import os
import sys
import subprocess
from gi.repository import Gtk


class OpenOutWindow(Gtk.Window):
    """Gtk+ 3 interface for OpenOut"""

    def __init__(self):
        """Initialize the window"""
        Gtk.Window.__init__(self, title='OpenOut')
        self.set_default_size(200, 250)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_name('gtk-quit')
        self.set_border_width(10)

        # Grid container
        self.grid = Gtk.Grid(column_homogeneous=True, row_homogeneous=True,
                             column_spacing=3, row_spacing=3)
        self.add(self.grid)

        # Button 1 for logout
        self.img1 = Gtk.Image(icon_name='gnome-logout')
        self.button1 = Gtk.Button('Logout', image=self.img1)
        self.button1.connect('clicked', self.on_button1_clicked)
        self.grid.attach(self.button1, 0, 0, 2, 1)

        # Button 2 for suspend
        self.img2 = Gtk.Image(icon_name='gnome-session-suspend')
        self.button2 = Gtk.Button('Suspend', image=self.img2)
        self.button2.connect('clicked', self.on_button2_clicked)
        self.grid.attach_next_to(self.button2, self.button1,
                                 Gtk.PositionType.BOTTOM, 2, 1)

        # Button 3 for hibernate
        self.img3 = Gtk.Image(icon_name='gnome-session-hibernate')
        self.button3 = Gtk.Button('Hibernate', image=self.img3)
        self.button3.connect('clicked', self.on_button3_clicked)
        self.grid.attach_next_to(self.button3, self.button2,
                                 Gtk.PositionType.BOTTOM, 2, 1)

        # Button 4 for reboot
        self.img4 = Gtk.Image(icon_name='gnome-session-reboot')
        self.button4 = Gtk.Button('Reboot', image=self.img4)
        self.button4.connect('clicked', self.on_button4_clicked)
        self.grid.attach_next_to(self.button4, self.button3,
                                 Gtk.PositionType.BOTTOM, 2, 1)

        # Button 5 for shutdown
        self.img5 = Gtk.Image(icon_name='gnome-shutdown')
        self.button5 = Gtk.Button('Shutdown', image=self.img5)
        self.button5.connect('clicked', self.on_button5_clicked)
        self.grid.attach_next_to(self.button5, self.button4,
                                 Gtk.PositionType.BOTTOM, 2, 1)

        # Button 6 for cancel
        self.img6 = Gtk.Image(icon_name='process-stop')
        self.button6 = Gtk.Button('Cancel', image=self.img6)
        self.button6.connect('clicked', Gtk.main_quit)
        self.grid.attach_next_to(self.button6, self.button5,
                                 Gtk.PositionType.BOTTOM, 1, 1)

        # Button 7 for about
        self.img7 = Gtk.Image(icon_name='help-about')
        self.button7 = Gtk.Button('About', image=self.img7)
        self.button7.connect('clicked', self.on_button7_clicked)
        self.grid.attach_next_to(self.button7, self.button6,
                                 Gtk.PositionType.RIGHT, 1, 1)

    # Callback for logout
    def on_button1_clicked(self, widget):
        """Detect the window manager for logout"""
        wm = {'pekwm': 'killall pekwm', 'openbox': 'openbox --exit',
              'fluxbox': 'killall fluxbox', 'jwm': 'jwm -exit',
              'fvwm': 'killall fvwm', 'icewm': 'killall icewm',
              'wmaker': 'killall wmaker'}
        for wm_name, cmd_logout in wm.iteritems():
            cmd_pid = 'pidof ' + wm_name
            p = subprocess.Popen(cmd_pid, shell=True, stdout=subprocess.PIPE)
            pid, err = p.communicate()
            if pid != '':
                # logout from window manager
                p = subprocess.Popen(cmd_logout, shell=True,
                                     stdout=subprocess.PIPE)
                out, err = p.communicate()
                sys.exit(0)

    # Callback for suspend
    def on_button2_clicked(self, widget):
        """Suspend the system"""
        os.system('systemctl suspend')
        sys.exit(0)

    # Callback for hibernate
    def on_button3_clicked(self, widget):
        """Hibernate the system"""
        os.system('systemctl hibernate')
        sys.exit(0)

    # Callback for reboot
    def on_button4_clicked(self, widget):
        """Reboot the computer"""
        os.system('systemctl reboot')
        sys.exit(0)

    # Callback for shutdown
    def on_button5_clicked(self, widget):
        """Shutdown the computer"""
        os.system('systemctl poweroff')
        sys.exit(0)

    # Callback for about
    def on_button7_clicked(self, widget):
        """Show info message"""
        print 'About'


def splash():
    """Print a nice splash on command line"""
    print """
 ___                 ___       _
/ _ \ _ __  ___ _ _ / _ \ _  _| |_
 (_) | '_ \/ -_) ' \ (_) | || |  _|
\___/| .__/\___|_||_\___/ \_,_|\__|
     |_|
A simple logout menu written in Python and Gtk+ 3.
    """


def main():
    """Show the window"""
    splash()
    win = OpenOutWindow()
    win.connect('delete-event', Gtk.main_quit)
    win.show_all()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()
