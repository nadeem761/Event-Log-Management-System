# -*- coding: cp1252 -*-
#
# Windows Event Log Viewer
# FB - 201012116
#from http://code.activestate.com/recipes/577499-windows-event-log-viewer/
import win32evtlog # requires pywin32 pre-installed
server = 'DESKTOP-D57JJ0U' # name of the target computer to get event logs
logtype = 'System'  'Application'  'Security'
hand = win32evtlog.OpenEventLog(server,logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

while True:
    events = win32evtlog.ReadEventLog(hand, flags,0)
    if events:
        for event in events:
            print('Event Category:', event.EventCategory)
            print('Time Generated:', event.TimeGenerated)
            print('Source Name:', event.SourceName)
            print('Event ID:', event.EventID)
            print('Event Type:', event.EventType)
            data = event.StringInserts
            if data:
                print('Event Data:')
                for msg in data:
                    print(msg.encode('cp1252','ignore'))
            print("")