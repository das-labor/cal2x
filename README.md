# cal2x
Scripts for parsing and using iCal feed of das-labor

## cal2sound

Get iCal feed and send a "ping" sound to the local pulseaudio server to stream it to all rooms.

Install icalendar python module with pip:

    # pip install icalendar

Install dependencies (debian, ubuntu, linuxmint):

	# apt-get install alsa-base pulseaudio sox


Add this line to crontab:

	* * * * * /usr/bin/python /home/pi/cal2sound.py


### Pulseaudio Streaming Server

If you want to stream to a pulseaudio server, this script is for the client.
To create a host install the graphical tool "papref" and select the checkbox of
"Enable network access to local sound devices" and "Don't require
authentication".

Then initiate the sink on the client (where this script lives) via:
    # pactl load-module module-tunnel-sink-new server=<ip-of-host> sink_name=<your sink name> channels=2 rate=32000

Then select the sink (tunneling to the host) as audio output.

### Thanks

to cdrk for the [Reception bell sound](https://freesound.org/people/cdrk/sounds/264594/ )
licensed under [CC-BY-3.0](http://creativecommons.org/licenses/by/3.0/)
