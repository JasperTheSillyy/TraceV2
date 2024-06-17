"""

TRACEV2 1.0.0 RELEASE

-------------------------

Coded in python by @urlocalbru on discord.

"""

import os
import requests
import sys
import time
import json
from urllib.request import urlopen
import re as r

welcomemessage = """
___________                        ____   ____________  
\__    ___/___________    ____  ___\   \ /   /\_____  \ 
  |    |  \_  __ \__  \ _/ ___\/ __ \   Y   /  /  ____/ 
  |    |   |  | \// __ \\\  \__\  ___/\     /  /       \ 
  |____|   |__|  (____  /\___  >___  >\___/   \_______ \

----------------------------------------------------------------------
//////////////////////////////////////////////////////////////////////

TRACEV2 RELEASE 1.0.0
Windows IP tool and geolocator.
Improved TraceV1, new and improved features.
Coded by @urlocalbru on discord.

//////////////////////////////////////////////////////////////////////
----------------------------------------------------------------------

Type "help" for a list of commands.
Type "clear" to clear the console.

-----------------------------------------------------------------------

"""

AllCommands = """
////////////////////////////
----------------------------
COMMANDS - TraceV2 1.0.0
----------------------------
////////////////////////////

help - Displays all commands.
clear - Clears the console.
geolocator - Geolocator tool.
exit - Exit TraceV2.
displaymyip - Displays your ip adress.
rawjson_geolocator - Geolocator tool, but displays in the raw json format.
pingfire - Rapid server pinging tool, lightweight DOS.
banner - Displays the TraceV2 banner/welcome message.

"""
# Getting things ready in the console
os.system('cls')
os.system('title TraceV2 1.0.0 Build')

#main

print(welcomemessage)

def output_as_tracev2(text):
    print('[TraceV2]: '+text)

def getIP():
    d = str(urlopen('http://checkip.dyndns.com/')
            .read())

    return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

def main():
    commandinput = input("[Command]: ")
    if commandinput.lower() == "help":
        os.system("cls")
        print(AllCommands)
        main()
    elif commandinput.lower() == "clear":
        os.system("cls")
        main()
    elif commandinput.lower() == "exit":
        output_as_tracev2('Exitting...')
        sys.exit()
    elif commandinput.lower() == "banner":
        print(welcomemessage)
        main()
    elif commandinput.lower() == "rawjson_geolocator":
        output_as_tracev2('Starting RAWJSON_GEOLOCATOR...')
        ipadress_input = input('[IP]: ')
        time.sleep(0.5)
        made_request = requests.get('http://www.ipinfo.io/'+ipadress_input+'/json')
        text_req = made_request.text
        os.system('cls')
        output_as_tracev2('Found data.')
        print(text_req)
        main()
    elif commandinput.lower() == "geolocator":
        output_as_tracev2('Starting geolocator...')
        time.sleep(0.5)
        geolocator_ip = input('[IP]: ')
        geolocator_request = requests.get('http://www.ipinfo.io/'+geolocator_ip)
        text_req = geolocator_request.text
        dataarray = json.loads(text_req)
        # Manually check through all data because I suck at coding in python.
        if 'error' in dataarray:
            output_as_tracev2('Invalid IP! Error code: '+str(dataarray['status']))
            main()
        if 'ip' in dataarray:
            output_as_tracev2('Found data!')
            os.system('cls')
            print('[IP]: '+dataarray['ip'])
            if 'hostname' in dataarray:
                print('[HOSTNAME]: '+dataarray['hostname'])
            if 'city' in dataarray:
                print('[CITY]: '+dataarray['city'])
            if 'region' in dataarray:
                print('[REGION]: '+dataarray['region'])
            if 'country' in dataarray:
                print('[COUNTRY]: '+dataarray['country'])
            if 'loc' in dataarray:
                print('[COORDINATES(RAW)]: '+dataarray['loc'])
            if 'org' in dataarray:
                print('[ORG]: '+dataarray['org'])
            if 'timezone' in dataarray:
                print('[TIMEZONE]: '+dataarray['timezone'])
            main()
    elif commandinput == "displaymyip":
        output_as_tracev2('Your IP adress is '+getIP())
        main()
    else:
        output_as_tracev2('Command not found, type "help" for a list of commands.')
        main()
main()
