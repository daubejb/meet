#!usr/bin/python
#  functions.py

import datetime
import sys


def write_md_to_file(gcalendar, args):
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
        att_build = 'Email | Status\n\n'
        for attendee in meeting.meeting['attendees']:
            email = attendee.get('email')
            response_status = attendee.get('responseStatus')
            if 'resource' not in email:
                att_build = att_build + '{} | {}\n\n'.format(
                    email, response_status
                )
        f.write(att_build)
        f.close()
