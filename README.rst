hikvision-recover
=================

Command-line tool for generating recovery codes for Hikvision IP Cameras


Normally, to reset a hikvision camera you contact their support department to generate a recovery code. 
This package will allow you to generate the proper recovery code without contacting support. 
To do this you need the camera's serial number and current time reported by the camera.

Installation
------------

You can install via pip::


   pip install hikvision-recover

Usage 
-----

After installing via pip, the command line entry point `hikvision-recover` is available. The syntax for the command is ::

   hikvision-recover serial year month day

e.g.::

   hikvision-recover DS-ABC1234567-HIJKLMNOPQRS10987654321 2017 01 25

positional arguments:

*  serial:      Camera Serial Number
*  year:        4 digit year of current camera time
*  month:       2 digit month of current camera time
*  day:         2 digit day of current camera time

optional arguments:
  -h, --help  show help message and exit

via script
^^^^^^^^^^


You can also use this package directly in a script instead of via the command line.

.. code-block:: python

   from hikvision_recover.recover import get_code

   serial = "DS-ABC1234567-HIJKLMNOPQRS10987654321"
   year = "2017"
   month = "01"
   day = "25"
   recovery_code = get_code(serial, year, month, day)
   print(recovery_code)

