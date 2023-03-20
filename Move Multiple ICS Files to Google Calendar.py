#Given a folder of .ICS files, import them to Google Calendar
#HTTP Requests:
'''Google HTTP Requests: https://developers.google.com/calendar/api/v3/reference/events/import#request-body, 
https://developers.google.com/calendar/api/v3/reference/events#resource'''

'''Google Auth: https://developers.google.com/workspace/guides/auth-overview,
Google Calendar Week to Target: https://calendar.google.com/calendar/u/0/r/week/2023/2/3'''

import os, requests

while True:
    filePath = input("Enter filepath: ").strip('\"')
    if os.path.isdir(filePath):
        break
    else:
        print("Filepath not found...copy from explorer path?")


for file in os.listdir(filePath): #opening file
    OpenJSON = open(os.path.join(filePath, file), 'r', encoding="utf8")
    ICS_JSON = OpenJSON.read()
    GetReq = requests.get('https://www.googleapis.com/calendar/v3/users/me/calendarList')
    #GetReq = requests.get('https://www.googleapis.com/calendar/v3/calendars/primary/events/import', data = ICS_JSON, auth = "")
    print(GetReq.status_code, GetReq.text)