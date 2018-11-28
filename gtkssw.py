#!/usr/bin/env python3
import datetime
import os

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

BASEDIR = os.path.dirname(os.path.abspath(__file__))


class StopWatch(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Stopwatch')
        self.create_variables()

        self.set_default_size(400, 100)
        self.set_resizable(False)
        self.set_time_label()
        self.set_title('Stopwatch {}'.format(self.time_label_val))

        self.create_widgets()
        self.create_layouts()

    def create_variables(self):
        self.is_running = False
        self.time_in_seconds = 0
        self.time_label_val = None

    def set_time_label(self):
        self.time_label_val = str(datetime.timedelta(seconds=self.time_in_seconds))

    def create_widgets(self):
        self.time_label = Gtk.Label()
        self.time_label.set_markup('<span font="48"><b>{}</b></span>'.format(self.time_label_val))

        self.image_start = Gtk.Image().new_from_icon_name('media-playback-start', 1)
        self.image_pause = Gtk.Image().new_from_icon_name('media-playback-pause', 1)
        self.start_pause_btn = Gtk.Button(image=self.image_start)

        self.image_update = Gtk.Image().new_from_icon_name('system-software-update', 1)
        self.update_btn = Gtk.Button(image=self.image_update)

        self.start_pause_btn.connect('clicked', self.start_pause)
        self.update_btn.connect('clicked', self.reset_label)

    def start_pause(self, button):
        if not self.is_running:
            self.is_running = True
            self.start_pause_btn.set_image(self.image_pause)
            GObject.timeout_add(1000, self.update_label)
        else:
            self.is_running = False
            self.start_pause_btn.set_image(self.image_start)

    def update_label(self):
        if self.is_running:
            self.main_def(1)
            return True

    def reset_label(self, button):
        if not self.is_running:
            self.main_def(0)

    def main_def(self, counter):
        if counter == 0:
            self.time_in_seconds = 0
        else:
            self.time_in_seconds += counter
        self.set_time_label()
        self.time_label.set_markup('<span font="48"><b>{}</b></span>'.format(self.time_label_val))
        self.set_title('Stopwatch {}'.format(self.time_label_val))


    def create_layouts(self):
        self.main_box = Gtk.Box(spacing=6,
                                orientation=Gtk.Orientation.VERTICAL)
        self.label_box = Gtk.Box()
        self.btn_box = Gtk.Box(spacing=6)

        self.label_box.pack_start(self.time_label, True, True, 0)

        self.btn_box.pack_start(self.start_pause_btn, True, True, 0)
        self.btn_box.pack_start(self.update_btn, True, True, 0)

        self.main_box.pack_start(self.label_box, True, True, 0)
        self.main_box.pack_start(self.btn_box, True, True, 0)

        self.add(self.main_box)


if __name__ == '__main__':
    win = StopWatch()
    icon_path = os.path.join(BASEDIR, 'stopwatch.png')
    win.set_icon_from_file(icon_path)
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
