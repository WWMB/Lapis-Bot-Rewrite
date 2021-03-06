import os
import json
import time

def newtemp(date):
    newtimevars = {}
    newtimevars['times'] = []
    newtimevars['times'].append({
    'sysdate': date,
    'total': 0,
    '00:00': 0,
    '00:30': 0,
    '01:00': 0,
	'01:30': 0,
	'02:00': 0,
	'02:30': 0,
	'03:00': 0,
	'03:30': 0,
	'04:00': 0,
	'04:30': 0,
	'05:00': 0,
	'05:30': 0,
	'06:00': 0,
	'06:30': 0,
	'07:00': 0,
	'07:30': 0,
	'08:00': 0,
	'08:30': 0,
	'09:00': 0,
	'09:30': 0,
	'10:00': 0,
	'10:30': 0,
	'11:00': 0,
	'11:30': 0,
	'12:00': 0,
	'12:30': 0,
	'13:00': 0,
	'13:30': 0,
	'14:00': 0,
	'14:30': 0,
	'15:00': 0,
	'15:30': 0,
	'16:00': 0,
	'16:30': 0,
	'17:00': 0,
	'17:30': 0,
	'18:00': 0,
	'18:30': 0,
	'19:00': 0,
	'19:30': 0,
	'20:00': 0,
	'20:30': 0,
	'21:00': 0,
	'21:30': 0,
	'22:00': 0,
	'22:30': 0,
	'23:00': 0,
	'23:30': 0
	})
    with open("timevars.json","w+") as file:
        json.dump(newtimevars,file,indent="\t")
    return

class Global:
    def setup(self):
        dir = os.getcwd()
        try:
            os.makedirs(dir+"/Data/Global/Temp")
            os.chdir(dir+"/Data/Global/Temp")
            newtemp(time.strftime("%m-%d-%Y"))
            os.chdir(dir)
            print("Setup: Global directories created successfully.")
        except IOError:
            os.chdir(dir+"/Data/Global/Temp")
            newtemp(time.strftime("%m-%d-%Y"))
            os.chdir(dir)
            print("Setup: Global directories created successfully.")
