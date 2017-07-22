#!usr/bin/python
#  main.py

import datetime

from terminal.terminal import get_user_input
from interface.api import GoogleAPI

def parse_date_time(date_time):
    date = date_time[:10]
    time = date_time[11:16]
    return date, time

def main():
    #  use terminal to parse user input
    args = get_user_input()
    print(args)

    #  instantiate a google api object
    google_api = GoogleAPI()
    print(google_api)

    #  api call to google to get a calendar object
    meetings = google_api.get_meeting()

    for meeting in meetings:
        start_date_time = meeting['start'].get('dateTime')
        end_date_time = meeting['end'].get('dateTime')
        summary = meeting['summary']
        date, start_time = parse_date_time(start_date_time)
        date_not_used, end_time = parse_date_time(end_date_time)
        description = meeting['description']
        location = meeting['location']
        creator = meeting['creator'].get('email')
        organizer = meeting['organizer'].get('email')
        htmlLink = meeting['htmlLink']
        attendees = meeting['attendees']
#        attachements = meeting['attachments']
        print()
        print('summary: {}'.format(summary))
        print('date: {}'.format(date))
        print('start time: {}'.format(start_time))
        print('end time: {}'.format(end_time))
        print('description: {}'.format(description))
        print('location: {}'.format(location))
        print('creator: {}'.format(creator))
        print('organizer: {}'.format(organizer))
        print('calendar link: {}'.format(htmlLink))
        print('attendees:')
        for attendee in attendees:
            email = attendee.get('email')
            response_status = attendee.get('responseStatus')
            if 'resource' not in email:
                print('{}: {}'.format(email, response_status))

#        if args.markdown:

if __name__ == '__main__':
    main()
