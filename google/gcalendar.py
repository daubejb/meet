#!/usr/bin/python
#  calendar.py


class gCalendar:
    '''Represents the users primary google calendar.'''
    def __init__(self):
        self.meetings = []

    def new_meeting(self, meetings):
        '''Create a 1 to many new meetings and append it to calendar'''
        for meeting in meetings:
            self.meetings.append(Meeting(meeting))
        return

    def find_next_meeting(self):
        pass


class Meeting:
    '''Represents a meeting on the google calendar.'''
    def __init__(self, meeting):
        '''Initialize a meeting with summary, dates, times, and creator.'''
        self.id = meeting['id']
        self.summary = meeting['summary']
        self.start_date = meeting['start'].get('dateTime')[:10]
        self.start_time = meeting['start'].get('dateTime')[11:16]
        self.end_date = meeting['end'].get('dateTime')[:10]
        self.end_time = meeting['end'].get('dateTime')[11:16]
        self.location = meeting['location']
        self.description = meeting['description']
        self.organizer = meeting['organizer'].get('email')
        self.html_link = meeting['htmlLink']
        self.revisions = meeting['sequence']
        self.attendees = meeting['attendees']

        return
        # self.start_date = start_date
        # self.end_date = end_date
        # self.start_time = start_time
        # self.end_time = end_time
        # self.location = location
        # self.description = description
        # self.creator = creator
        # self.html_link = html_link
        # self.attendees = []