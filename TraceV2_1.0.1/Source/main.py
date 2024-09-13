import os
import sys
import time
import json
import requests
from urllib.request import urlopen
import re
import threading
import os.path

welcomemessage = """
___________                        ____   ____________  
\__    ___/___________    ____  ___\   \ /   /\_____  \ 
  |    |  \_  __ \__  \ _/ ___\/ __ \   Y   /  /  ____/ 
  |    |   |  | \// __ \\\  \__\  ___/\     /  /       \ 
  |____|   |__|  (____  /\___  >___  >\___/   \_______ \

----------------------------------------------------------------------
//////////////////////////////////////////////////////////////////////

TRACEV2 RELEASE 1.0.1
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
COMMANDS - TraceV2 1.0.1
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
changelog - Displays the new version changelog. (ver 1.0.1+)

"""

changelog = """
/////////////////////////////////////////////////////
-----------------------------------------------------
CHANGELOG - TraceV2 1.0.1
-----------------------------------------------------
/////////////////////////////////////////////////////

1. Added an auto-update system.
2. Added an auto-update system installer. (automatic)
3. Added functionality to PingFire
4. Geolocator generates a google maps link.
5. Added the changelog function.
------------------------------------------------------
//////////////////////////////////////////////////////

"""


def output_as_tracev2(text):
    print('[TraceV2]: ' + text)


def getIP():
    try:
        d = str(urlopen('http://checkip.dyndns.com/').read())
        ip = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
        return ip
    except Exception as e:
        output_as_tracev2(f'Error retrieving IP address: {e}')
        return None


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    updater_path = 'autoupdater.exe'
    if os.path.exists(updater_path):
        os.startfile(updater_path)
    else:
        print(f"File '{updater_path}' not found.")

    print(welcomemessage)

    while True:
        commandinput = input("[Command]: ").lower().strip()

        if commandinput == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(AllCommands)

        elif commandinput == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif commandinput == "exit":
            output_as_tracev2('Exiting...')
            sys.exit()

        elif commandinput == "banner":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(welcomemessage)

        elif commandinput == "rawjson_geolocator":
            try:
                output_as_tracev2('Starting RAWJSON_GEOLOCATOR...')
                ipadress_input = input('[IP]: ')
                time.sleep(0.5)
                made_request = requests.get(f'http://www.ipinfo.io/{ipadress_input}/json')
                text_req = made_request.text
                os.system('cls' if os.name == 'nt' else 'clear')
                output_as_tracev2('Found data.')
                print(text_req)
            except Exception as e:
                output_as_tracev2(f'Error in rawjson_geolocator: {e}')

        elif commandinput == "geolocator":
            try:
                output_as_tracev2('Starting geolocator...')
                time.sleep(0.5)
                geolocator_ip = input('[IP]: ')
                geolocator_request = requests.get(f'http://www.ipinfo.io/{geolocator_ip}')
                text_req = geolocator_request.text
                dataarray = json.loads(text_req)
                if 'error' in dataarray:
                    output_as_tracev2(f'Invalid IP! Error code: {dataarray["status"]}')
                else:
                    output_as_tracev2('Found data!')
                    print(f'[IP]: {dataarray["ip"]}')
                    if 'hostname' in dataarray:
                        print(f'[HOSTNAME]: {dataarray["hostname"]}')
                    if 'city' in dataarray:
                        print(f'[CITY]: {dataarray["city"]}')
                    if 'region' in dataarray:
                        print(f'[REGION]: {dataarray["region"]}')
                    if 'country' in dataarray:
                        print(f'[COUNTRY]: {dataarray["country"]}')
                    if 'loc' in dataarray:
                        print(f'[COORDINATES(RAW)]: {dataarray["loc"]}')
                        b2 = dataarray['loc'].split(',')
                        print(f'[GEOLOCATION(GOOGLE MAPS)]: https://www.google.com/maps/?q={b2[0]},{b2[1]}')
                    if 'org' in dataarray:
                        print(f'[ORG]: {dataarray["org"]}')
                    if 'timezone' in dataarray:
                        print(f'[TIMEZONE]: {dataarray["timezone"]}')
            except Exception as e:
                output_as_tracev2(f'Error in geolocator: {e}')

        elif commandinput == "displaymyip":
            ip = getIP()
            if ip:
                output_as_tracev2(f'Your IP address is {ip}')

        elif commandinput == "changelog":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(changelog)

        elif commandinput == "pingfire":
            try:
                output_as_tracev2('Starting PingFire...')
                ip = input('[IP]: ')
                output_as_tracev2('Starting attack...')

                def ping_target():
                    while True:
                        subprocess.Popen(['ping', ip])
                        time.sleep(0.05)

                ping_thread = threading.Thread(target=ping_target)
                ping_thread.start()

            except Exception as e:
                output_as_tracev2(f'Error in pingfire: {e}')

        else:
            output_as_tracev2('Command not found, type "help" for a list of commands.')


if __name__ == "__main__":
    main()
