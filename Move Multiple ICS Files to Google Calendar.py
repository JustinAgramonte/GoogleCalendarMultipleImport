#Given a folder of .ICS files, import them to Google Calendar
#HTTP Requests:
'''Google HTTP Requests: https://developers.google.com/calendar/api/v3/reference/events/import#http-request, 
https://developers.google.com/calendar/api/v3/reference/events/import#request-body, https://developers.google.com/calendar/api/v3/reference/events#resource  
'''
#Google Auth: https://developers.google.com/workspace/guides/auth-overview, https://developers.google.com/identity/gsi/web/guides/overview
#Google Calendar Week to Target: https://calendar.google.com/calendar/u/0/r/week/2023/2/3

import os, requests

filePath = input("Enter filepath: ").strip('\"')
assert os.path.isdir(filePath), "Filepath not found...copy from explorer path?"

for file in os.listdir(filePath): #opening file
    #placeholder
    print
