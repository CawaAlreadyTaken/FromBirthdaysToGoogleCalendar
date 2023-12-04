# From Birthdays to Google Calendar

## A brief explanation on how to move your birthdays from the ["Birthdays" app](https://play.google.com/store/apps/details?id=com.Birthdays.alarm.reminderAlert) to your Google Calendar

1. First of all, go to [your Google Calendar account](https://calendar.google.com/calendar) (from PC) and generate a new calendar "Birthdays" (or the name that you think fits the best)
2. In the settings for the newly created calendar, select "Integrate calendar" and copy the `calendar ID`.
3. Paste the `calendar ID` in a file `calendar_id.txt` in the root of this github repository
4. Then go to [your Google Cloud Console](https://console.cloud.google.com/) and create a new project
5. Enable Google Calendar API for the project
6. Create the `ID client OAuth 2.0` credentials for your project, and download the json with the credentials
7. Save the credentials json in a file `calendar_credentials.json` in the root of this github repository
8. In `OAuth Consent Screen`, publish the app, since it will not work while in test mode

The `script` part is now ready, we just need to prepare the data.

1. Export the birthdays from the app as csv and move the `csv` file to your PC
2. Save it in a file `birthdays.txt` in the root of this github repository

Now install the modules for running the script:
```sh
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

We are finally ready! Start the `script.py` file.  

When promped to login, log with the google account in which you initially created the new calendar.
