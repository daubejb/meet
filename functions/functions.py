#!usr/bin/python
#  functions.py

import datetime
import sys
import os
import os.path


def write_md_to_file(gcalendar, args):
    for meeting in gcalendar.meetings:
        markdown_filename = '{} - {}.md'.format(
            meeting.meeting['start_date'],
            meeting.meeting['summary'])
        hr = '_ _ _\n\n'
        chars_to_remove = dict((ord(char), None) for char in '\\/*?:"<>|')
        clean_md_filename = markdown_filename.translate(chars_to_remove)
        final_file = create_os_nuetral_filepath(clean_md_filename)
        f = open(final_file, 'w')
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
        attendee_check = meeting.meeting['attendees']
        if attendee_check == 'No attendees':
            f.write(attendee_check)
        else:
            for attendee in meeting.meeting['attendees']:
                email = attendee.get('email')
                response_status = attendee.get('responseStatus')
                if 'resource' not in email:
                    att_build = att_build + '{} | {}\n\n'.format(
                        email, response_status
                    )
            f.write(att_build)
        f.close()


def write_html_to_file(gcalendar, args):
    for meeting in gcalendar.meetings:
        html_filename = '{} - {}'.format(
            meeting.meeting['start_date'],
            meeting.meeting['summary']
        )
        chars_to_remove = dict((ord(char), None) for char in '\\/*?:"<>|')
        file_name = html_filename.translate(chars_to_remove)
        file_path = create_os_nuetral_filepath(file_name)
        f = open(file_path, 'w')
        f.write('<h1>{}</h1>'.format(meeting.meeting['summary']))
        f.write('<hr><br>')
        f.write('<br><p><b>Organizer</b>: {}</p><br>'.format(
            meeting.meeting['organizer']
        ))
        f.write('<b>Start</b>: {} - {} | <b>End</b>: {} - {} | \
                 <b>Location</b>: {}<br>'.format(
            meeting.meeting['start_date'],
            meeting.meeting['start_time'],
            meeting.meeting['end_date'],
            meeting.meeting['end_time'],
            meeting.meeting['location']
        ))
        f.write('<hr><br>')
        f.write('<h2>Notes:</h2>\n\n1. take notes here<br>')
        f.write('<hr><br>')
        f.write('<br><h2>Description:</h2>\n\n{}\n\n'.format(
            meeting.meeting['description']
        ))
        f.write('<br><hr>\n\n<br>')
        f.write('<br><b>Calendar link</b>: {}\n\n'.format(
            meeting.meeting['html_link']
        ))
        f.write('<b>Attendees</b>:\n\n')
        att_build = 'Email | Status\n\n'
        attendee_check = meeting.meeting['attendees']
        if attendee_check == 'No attendees':
            f.write(attendee_check)
        else:
            for attendee in meeting.meeting['attendees']:
                email = attendee.get('email')
                response_status = attendee.get('responseStatus')
                if 'resource' not in email:
                    att_build = att_build + '{} | {}\n\n'.format(
                        email, response_status
                    )
            f.write(att_build)
        f.close()
        return file_path, file_name


def create_os_nuetral_filepath(filename):
    home_dir = os.path.expanduser('~')
    meeting_dir = os.path.join(home_dir, '.meeting_pro')
    meeting_path = os.path.join(meeting_dir, filename)
    return meeting_path
