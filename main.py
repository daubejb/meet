#!usr/bin/python
#  main.py


from terminal.terminal import get_user_input
from interface.api import GoogleAPI
from google.gcalendar import gCalendar
from functions.functions import write_md_to_file


def parse_date_time(date_time):
    date = date_time[:10]
    time = date_time[11:16]
    return date, time


def main():
    #  instantiate a google api object
    google_api = GoogleAPI()

    #  use terminal to parse user input
    args = get_user_input()

    #  api call to google to get a calendar object
    meetings = google_api.get_meeting()

    #  create a calendar object
    gcalendar = gCalendar()
    gcalendar.new_meeting(meetings)

    if args.markdown:
        write_md_to_file(gcalendar, args)

    if args.google:
        print('google it is')

if __name__ == '__main__':
    main()
