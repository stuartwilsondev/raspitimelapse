#!/usr/bin/env python

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

class UniqueDirectory(object):

  def __init__(self):
    self.today = datetime.now()
    self.name = self.generate_directory_name()

  def get_today(self):
    return self.today

  def get_directory_name(self):
    return self.name

  def generate_directory_name(self):
    today =  self.get_today()
    directory_name = "timelapse_%d-%d-%d_%d" % (
     today.year,
     today.month,
     today.day,
     today.hour
    )

    #create it if it does not exist
    if not os.path.isdir(directory_name):
      os.mkdir(directory_name)
      print "Created Directory: %s" % directory_name
    else:
      print "Directory: %s already exists" % directory_name

    return directory_name


#Maxwidth 2592
#MaxHeight 1944
class TimeLapseImage(object):

  def __init__(self,width,height,directory):
    self.today = datetime.now()
    self.width = width
    self.height = height
    self.directory = directory
    self.file_name = self.generate_unique_file_name()
    self.command = self.create_command()

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

  def get_command(self):
    return self.command

  def generate_unique_file_name(self):
    today = self.get_today()

    file_name = "img_%d-%d-%d_%d_%d:" % (
     today.year,
     today.month,
     today.day,
     today.hour,
     today.minute
    )

    return file_name

  def create_command(self):
    command = "raspistill -w %d -h %d -o %s/%s.jpg -sh 40 -awb auto -mm average -v" % (
        self.get_width(),
        self.get_height(),
        self.get_directory().get_directory_name(),
        self.get_file_name()
      )

    print "Command to run: %s" % command

    return command


Directory = UniqueDirectory()
Img = TimeLapseImage(800,600,Directory)

#Run the command
os.system(Img.get_command())
