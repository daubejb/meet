#!usr/bin/python
#  main.py

import datetime
import sys

from terminal.terminal import get_user_input
from interface.api import GoogleAPI
from google.gcalendar import gCalendar


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

    #  create a calendar object
    gcalendar = gCalendar()
    gcalendar.new_meeting(meetings)

    if args.markdown:
        for meeting in gcalendar.meetings:
            markdown_filename = '{} - {}.md'.format(
                meeting.meeting['start_date'],
                meeting.meeting['summary'])
            hr = '_ _ _\n\n'
            chars_to_remove = dict((ord(char), None) for char in '\\/*?:"<>|')
            clean_md_filename = markdown_filename.translate(chars_to_remove)
            f = open(clean_md_filename, 'w')
            f.write('# {}\n\n'.format(meeting.meeting['summary']))
            f.write('**Organizer**: {}\n\n'.format(
                meeting.meeting['organizer']
            ))
            f.write('**Start**: {} - {}  | \
                    **End**: {} - {}  | \
                    **Location**: {}\n\n'.format(
                meeting.meeting['start_date'],
                meeting.meeting['start_time'],
                meeting.meeting['end_date'],
                meeting.meeting['end_time'],
                meeting.meeting['location']
            ))
            f.write(hr)
            f.write('## Notes:\n\n')
            f.write('1. take notes here\n\n')
            f.write(hr)
            f.write('## Description:\n\n{}\n\n'.format(
                meeting.meeting['description']
            ))
            f.write(hr)
            f.write('**Calendar link**: {}\n\n'.format(
                meeting.meeting['html_link']
            ))
            f.write('**Attendees**:\n\n')
            attendee_builder = ''
            for attendee in meeting.meeting['attendees']:
                email = attendee.get('email')
                response_status = attendee.get('responseStatus')
                if 'resource' not in email:
                    attendee_builder = attendee_builder + '{}: {}\n\n'.format(
                        email, response_status
                    )
            f.write(attendee_builder)
            f.close()

    if args.google:
        print('google it is')
    #         # flink = 'Calendar link: {}\n\n'.format(htmlLink)
    #         # fattendees_header = '**Attendees**:\n\n'
    #         # fperson = ''
    #         # if attendees == 'No attendees':
    #         #     fattendees = attendees
    #         # else:
    #         #     for attendee in attendees:
    #         #         email = attendee.get('email')
    #         #         response_status = attendee.get('responseStatus')
    #         #         if 'resource' not in email:
    #         #             fperson = fperson + '{}: {}\n\n'.format(
    #         #                 email, response_status)


if __name__ == '__main__':
    main()
