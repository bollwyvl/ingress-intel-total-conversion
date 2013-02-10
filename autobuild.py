#!/usr/bin/env python

"""
Monitors our code for changes, builds user script

Copy/Pasta/Hack from:
http://ginstrom.com/scribbles/2012/05/10/
"""
import os
import sys
import subprocess
import datetime
import time
import re

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from build import build

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "code"))

EXT_RE = re.compile(r"(?<!\.user)\.js$")


def get_now():
    "Get the current date and time as a string"
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")


class ChangeHandler(FileSystemEventHandler):
    """
    React to changes in Python and Rest files by
    running unit tests (Python) or building docs (.rst)
    """

    def on_any_event(self, event):
        """
        If any file or folder is changed... but only run for js files
        """

        if event.is_directory:
            return

        if EXT_RE.search(event.src_path) is not None:
            print >> sys.stderr, "Building .user.js at %s" % get_now()
            build()


def main():
    """
    Called when run as main.
    Look for changes to code and doc files.
    """
    print "MONITORING %s for changes... Press Ctrl+Z to stop" % BASEDIR

    while True:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, BASEDIR, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == '__main__':
    main()
