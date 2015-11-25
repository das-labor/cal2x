#!/usr/bin/python2
import icalendar
import urllib2
import datetime
import os
import pickle

calfile = "/tmp/laborcalendar.pickle"
datafile = "/tmp/laborcal_data"

def now_in_5min_timerange(point_in_time, now):
        min5_ago = point_in_time - datetime.timedelta(minutes=5)
        return min5_ago < now < point_in_time

def cal2sound():
        req = urllib2.urlopen('https://www.das-labor.org/termine.ics')
        data = req.read()
        data2 = None

        if os.path.exists(datafile):
                with open(datafile, "rb") as fd:
                        data2 = pickle.load(fd)

        now = datetime.datetime.now()
#        now = datetime.datetime(year=2015, month=11, day=26, hour=19, minute=59, second=59) #Test

        cal = None
        """parse calendar only of ics file differs, else load from pickle file"""
        if not data == data2:
                cal = icalendar.Calendar.from_ical(data)
                with open(datafile, "wb", pickle.HIGHEST_PROTOCOL) as fd:
                        pickle.dump(data, fd)
                with open(calfile, "wb", pickle.HIGHEST_PROTOCOL) as fd:
                        pickle.dump(cal, fd)
        else:
                with open(calfile, "rb") as fd:
                        cal = pickle.load(fd)

        for event in cal.walk('vevent'):
                nextevent_date = str(event.get('dtstart').dt)
                parsed_datetime = datetime.datetime.strptime(nextevent_date, '%Y-%m-%d %H:%M:%S')
                if now_in_5min_timerange(parsed_datetime, now):
                        print("TODAYS is an event")
                        os.system("mplayer -ao pulse:10.0.1.6 /home/pi/bell.flac ")
                        break

cal2sound()
