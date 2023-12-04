#!/usr/bin/env python3

import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load the birthdays json
with open('birthdays.csv', 'r') as file:
    birthdays_rows = file.readlines()[1:] # The first line contains the headers

with open('calendar_id.txt', 'r') as file:
    CALENDAR_ID = file.read().strip()

# API Google Calendar authorization
SCOPES = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('calendar_secret.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('calendar', 'v3', credentials=creds)

# Function to add a birthday to Google Calendar
def add_birthday(name, date):
    try:
        date_this_year = str(datetime.datetime.now().year) + '-' + date
        event = {
            'summary': f'Compleanno di {name}',
            'start': {'date': date_this_year},
            'end': {'date': date_this_year},
            'recurrence': ['RRULE:FREQ=YEARLY'],
        }
        event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')
    except Exception as e:
        print(f'Error in the creation of the event for {name}: {e}')

# Add all birthdays to Google Calendar
for line in birthdays_rows:
    line = line.strip()
    items = line.split(',')
    name = items[1]
    date = items[3][5:]
    add_birthday(name, date)

print('Done!')

