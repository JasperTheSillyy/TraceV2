"""

TraceV2's auto-updater system.

"""

from urllib.request import urlopen
import json
import os
import sys

url = "https://jesperserverside.github.io/ignore/asdf.txt"
data = urlopen(url).read()
latestversion = bytes.decode(data,'utf-8')

builddatafile = open('build_data.json','r')
content = builddatafile.read()

build_data = json.loads(content)

version = build_data['build_data']['version']

if build_data['build_data']['version_type'] == "updatable":
    print('[UPDATER]: Your version is updatable. \n[UPDATER]: Checking for updates...')
    if not version == latestversion:
        print('[UPDATER]: Update available! Downloading...')
        os.system('curl https://jesperserverside.github.io/ignore/TraceV2.zip -o TraceV2_'+latestversion+'.zip')
        sys.exit()
    else:
        print('[UPDATER]: TraceV2 is up to date.')
        sys.exit()