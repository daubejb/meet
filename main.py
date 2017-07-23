#!usr/bin/python
#  main.py

import datetime
import sys

from terminal.terminal import get_user_input
from interface.api import GoogleAPI


def parse_date_time(date_time):
    date = date_time[:10]
    time = date_time[11:16]
    return date, time


def main():
    #  use terminal to parse user input
    args = get_user_input()

    #  instantiate a google api object
    google_api = GoogleAPI()

    #  api call to google to get a calendar object
    meetings = google_api.get_meeting()

    for meeting in meetings:
        start_date_time = meeting['start'].get('dateTime')
        end_date_time = meeting['end'].get('dateTime')
        summary = meeting['summary']
        try:
            date, start_time = parse_date_time(start_date_time)
            date_not_used, end_time = parse_date_time(end_date_time)
        except TypeError:
            start_time = 'all day'
            end_time = 'all day'
        try:
            description = meeting['description']
        except KeyError:
            description = 'No description provided'
        try:
            location = meeting['location']
        except KeyError:
            location = 'No location provided'
        creator = meeting['creator'].get('email')
        organizer = meeting['organizer'].get('email')
        htmlLink = meeting['htmlLink']
        try:
            attendees = meeting['attendees']
        except KeyError:
            attendees = 'No attendees'
        markdown_filename = date + '-' + summary + '.md'
        if args.markdown:
            fsummary = '# {}\n\n'.format(summary)
            fdate = '**Date**: {}  |  '.format(date)
            fstart_time = '**Start time**: {}  |  '.format(start_time)
            fend_time = '**End time**:   {}  |  '.format(end_time)
            flocation = '**Location**:   {}\n\n'.format(location)
            fhr = '_ _ _\n\n'
            fnotes = '## Notes:\n\n'
            fnote1 = '1. note\n\n'
            fdescription = '## Description:\n\n {}\n\n'.format(description)
            fcreator = '**Creator**: {}\n\n'.format(creator)
            flink = 'Calendar link: {}\n\n'.format(htmlLink)
            fattendees_header = '**Attendees**:\n\n'
            fperson = ''
            if attendees == 'No attendees':
                fattendees = attendees
            else:
                for attendee in attendees:
                    email = attendee.get('email')
                    response_status = attendee.get('responseStatus')
                    if 'resource' not in email:
                        fperson = fperson + '{}: {}\n\n'.format(
                            email, response_status)
            f = open(markdown_filename, 'w')
            f.write(fsummary)
            f.write(fcreator)
            f.write(fdate)
            f.write(fstart_time)
            f.write(fend_time)
            f.write(flocation)
            f.write(fhr)
            f.write(fnotes)
            f.write(fnote1)
            f.write(fhr)
            f.write(fdescription)
            f.write(fhr)
            f.write(fattendees_header)
            f.write(fperson)
            f.write(flink)
            f.close()

        if args.google:
            print('google it is')
if __name__ == '__main__':
    main()
