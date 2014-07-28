#!/usr/bin/env python

from TakePhoto import *
import RPi.GPIO as GPIO


def create_command(width, height, directory, file_name):
    command = "raspistill -w %d -h %d -o %s/%s.jpg -sh 40 -awb auto -mm average -v" % (
        width,
        height,
        directory,
        file_name
    )

    log_message("Command to run: %s" % command)

    return command

#Main
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-l', action='store_true', default=False,
                        help='Log to the console as well as file')

    parser.add_argument('-width', default=800,
                        help='Captured image Width (default 800)')

    parser.add_argument('-height', default=600,
                        help='Captured image Height (default 600)')

    parser.add_argument('-directory', default="/mnt/usb",
                        help='Parent directory to place timelapse directories in (default /mnt/usb)')

    args = parser.parse_args()

    global log_to_screen
    log_to_screen = args.l

    width = args.width
    height = args.height
    parent_directory = args.directory

    log_message('Started')

    timelapse_directory = UniqueDirectory(parent_directory)
    img = TimeLapseImage(width, height,  timelapse_directory.get_directory_name())

    command_to_run = create_command(
        img.get_width(),
        img.get_height(),
        img.get_directory(),
        img.get_file_name()
    )

    #Run the command
    os.system(command_to_run)

    log_message('Finished')

if __name__ == '__main__':
    main()
