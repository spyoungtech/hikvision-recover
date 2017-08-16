Normally, to reset a hikvision camera you contact their support department to generate a recovery code. However, the method they use to do this has been cracked. This source code will generate the proper recovery code when provided the camera's serial number and current time reported by the camera.


# hikvision-recovery
Command-line tool for generating recovery codes for Hikvision IP Cameras

## Usage 

hikvision_recover.py serial year month day

positional arguments:

*  serial:      Camera Serial Number
*  year:        4 digit year of current camera time
*  month:       2 digit month of current camera time
*  day:         2 digit day of current camera time

optional arguments:
  -h, --help  show help message and exit
