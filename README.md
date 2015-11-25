# cal2x
Scripts for parsing and using iCal feed of das-labor

=== cal2sound ===

Get iCal feed and send a "ping" sound to the local pulseaudio server to stream it to all rooms.

Install icalendar python module with pip
	# pip2 install icalendar

Install dependencies
	# apt-get install alsa-base pulseaudio mplayer

Add this line to crontab

	* * * * * /usr/bin/python2 /home/pi/cal2sound.py

