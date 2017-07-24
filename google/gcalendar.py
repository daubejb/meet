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

        self.meeting = {
            'id': meeting['id'],
            'summary': meeting['summary'],
            'start_date': meeting['start'].get('dateTime')[:10],
            'end_date': meeting['end'].get('dateTime')[:10],
            'organizer': meeting['organizer'].get('email'),
            'html_link': meeting['htmlLink'],
        }
        try:
            self.meeting['start_time'] = meeting['start'].get(
                'dateTime')[11:16]
        except TypeError:
            self.meeting['start_time'] = 'all day'

        try:
            self.meeting['end_time'] = meeting['end'].get(
                'dateTime')[11:16]
        except TypeError:
            self.meeting['end_time'] = 'all day'

        try:
            self.meeting['description'] = meeting['description']
        except KeyError:
            self.meeting['description'] = 'No description provided.'

        try:
            self.meeting['location'] = meeting['location']
        except KeyError:
            self.meeting['location'] = 'No location provided.'

        try:
            self.meeting['attendees'] = meeting['attendees']
        except KeyError:
            self.meeting['attendees'] = 'No attendees'

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