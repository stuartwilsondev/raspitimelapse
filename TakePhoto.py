#!/usr/bin/env python

import os
import logging
from datetime import datetime
import argparse

# Global parameter to set if we log to stdout or just a file
log_to_screen = False

#Set global logger
logging.basicConfig(
    format='%(asctime)s:%(filename)s:%(levelname)s:__%(message)s',
    filename='photo.log',
    level=logging.INFO
)


#Wrapper around standard logger. Defaults to INFO
def log_message(message, level='info'):
    if log_to_screen:
        print "LOG:: %s" % message

    if level == 'debug':
        logging.debug(message)

    elif level == 'info':
        logging.info(message)

    elif level == 'warning':
        logging.warning(message)

    elif level == 'error':
        logging.error(message)

    elif level == 'critical':
        logging.critical(message)

    else:
        logging.info(message)


#Class to create a unique directory (or provide the current one)
class UniqueDirectory(object):
    def __init__(self, directory):
        self.parent_directory = directory
        self.today = datetime.now()
        self.name = self.generate_directory_name()


    def get_today(self):
        return self.today

    def get_directory_name(self):
        return self.name

    def get_parent_directory(self):
        parent_directory = self.parent_directory

        return parent_directory.rstrip('/')

    def generate_directory_name(self):
        today = self.get_today()

        directory_name = "%s/timelapse_%d-%d-%d_%d" % (
            self.get_parent_directory(),
            today.year,
            today.month,
            today.day,
            today.hour
        )

        #create it if it does not exist
        if not os.path.isdir(directory_name):
            os.mkdir(directory_name)
            log_message("Created Directory: %s" % directory_name)
        else:
            log_message("Directory: %s already exists" % directory_name)

        return directory_name


#Image class Maxwidth 2592 MaxHeight 1944
class TimeLapseImage(object):
    def __init__(self, width, height, directory):
        self.today = datetime.now()
        self.width = width
        self.height = height
        self.directory = directory
        self.file_name = self.generate_unique_file_name()

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_today(self):
        return self.today

    def get_directory(self):
        return self.directory

    def get_file_name(self):
        return str(self.file_name)

    def generate_unique_file_name(self):
        today = self.get_today()

        file_name = "img_%d-%d-%d_%d_%d" % (
            today.year,
            today.month,
            today.day,
            today.hour,
            today.minute
        )

        return file_name

