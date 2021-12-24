# Note: dank.serverbuilder.py is meant to be run as an .exe by default, if you would like to execute the script, make the below changes...
#       - uncomment the following line > filepath = os.path.dirname(__file__) # as .py
#       - comment the following line > filepath = os.path.dirname(sys.argv[0]) # as .exe
#       - dsb_assets.zip is also required for this script to function properly! Make sure "filepath_temp" directs to its directory!

import os
import re
import sys
import time
import random
import zipfile
import requests
import webbrowser as web
import concurrent.futures
from colorama import init, Fore, Style

try:
    #filepath = os.path.dirname(__file__) # as .py
    filepath = os.path.dirname(sys.argv[0]) # as .exe
    filepath_temp = os.path.dirname(__file__) # for .exe
    os.chdir(filepath)
except:
    pass

init(autoreset=True)
white = Fore.WHITE + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT

# print banner

banner_ascii = '''
                                                                                
 ____          _     _____                     _____     _ _   _            ___ 
|    \ ___ ___| |_  |   __|___ ___ _ _ ___ ___| __  |_ _|_| |_| |___ ___   |_  |
|  |  | .'|   | '_|_|__   | -_|  _| | | -_|  _| __ -| | | | | . | -_|  _|  |  _|
|____/|__,|_|_|_,_|_|_____|___|_|  \_/|___|_| |_____|___|_|_|___|___|_|    |___|
                                                                                
'''

# randomized banner color

bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
codes = vars(Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_chars = [random.choice(colors) + char for char in banner_ascii]
banner_ascii_colored = ''.join(colored_chars).splitlines()

# colored banner aligner

def aligner(banner, banner_colored):

    width = os.get_terminal_size().columns
    banner_lines = banner.splitlines()
    for i in range(len(banner_lines)):
        banner_lines[i] = banner_lines[i].center(width).replace(banner_lines[i],banner_colored[i])
    banner_aligned = ''.join(banner_lines)
    return banner_aligned

os.system('cls')
print(aligner(banner_ascii, banner_ascii_colored))

# get available papermc versions and print

Success = False
while not Success:
    try:
        response = requests.get("https://papermc.io/api/v2/projects/paper/").json()
        available_versions = f"\n  {white}> {magenta}Available Paper Versions{white}: {magenta}" + str(response['versions']).replace("[","").replace("]","").replace("\'","").replace(".",f"{white}.{magenta}").replace(",",f"{white},{magenta}")
        print(available_versions)
        available_versions = available_versions.replace(f"{white}","").replace(f"{magenta}","")
        Success = True
    except:
        wait = input(f"\n  {white}> {red}Failed to get paper versions! Make sure you are connected to the Internet! Press {white}Enter {red}to try again.")
        
# user input

name = str(input(f"\n  {white}> {magenta}Server Name{white}: {magenta}"))
version = str(input(f"\n  {white}> {magenta}Version{white}: {magenta}"))

# check if mc version is available

versions_list = available_versions.replace(",","").replace(f"{white}","").replace(f"{magenta}","").split(" ")
version_available = False

def version_check():
    for ver in versions_list:
        if version == ver:
            global version_available
            version_available = True

version_check()

# user input [ server settings ]

while not version_available:
    print(f"\n  {white}> {red}That version is not supported{white}!")
    version = str(input(f"\n  {white}> {magenta}Version{white}: {magenta}"))
    version_check()
os.system(f"title dank.serverbuilder [ {name} - {version} ]")

ram = int(input(f"\n  {white}> {magenta}RAM in MB {white}[ {magenta}Above 512 {white}]: {magenta}"))

if ram < 512:
    ram = 512

offline = str(input(f"\n  {white}> {magenta}Allow Cracked Players {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}"))

read_me = f'''

:::::::::  ::::::::::     :::     :::::::::       ::::    ::::  ::::::::::
:+:    :+: :+:          :+: :+:   :+:    :+:      +:+:+: :+:+:+ :+:       
+:+    +:+ +:+         +:+   +:+  +:+    +:+      +:+ +:+:+ +:+ +:+       
+#++:++#:  +#++:++#   +#++:++#++: +#+    +:+      +#+  +:+  +#+ +#++:++#  
+#+    +#+ +#+        +#+     +#+ +#+    +#+      +#+       +#+ +#+       
#+#    #+# #+#        #+#     #+# #+#    #+#      #+#       #+# #+#       
###    ### ########## ###     ### #########       ###       ### ##########


'''

read_me_colored = read_me.replace(":",f"{white}:").replace("+",f"{white}+").replace("#",f"{magenta}#").splitlines()

os.system('cls')
sys.stdout.write(aligner(read_me, read_me_colored))

# JDK input

print(f"\n  {white}> {magenta}The below program step is {white}required {magenta}to run a minecraft paper server of version 1{white}.{magenta}17 and above!")
print(f"\n  {white}> {magenta}Only needs to be installed once!")
print(f"\n  {white}> {magenta}If you do not know / are unsure / never installed jre, type {white}\"{magenta}y{white}\"")
download_jdk = str(input(f"\n  {white}> {magenta}Do you want to download {white}OpenJDK-16{magenta}? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()

os.system('cls')
sys.stdout.write(aligner(read_me, read_me_colored))

# hosting method

print(f"\n  {white}> {magenta}Great! Now you need to pick a {white}host{magenta} for your mc server{white}!")
print(f"\n  {white}> {magenta}If you are {white}experienced {magenta}and would like to use {white}port forwarding {magenta}/ {white}alternative hosting methods, {magenta}Choose {white}Option 1{magenta}.")
print(f"\n  {white}> {magenta}If you are {white}new {magenta}to hosting and would like to quickly host a server with {white}playit.gg{magenta}'s tunnel, Choose {white}Option 2{magenta}.")

playit = int(input(f"\n  {white}> {magenta}Choice {white}[ {magenta}1 {white}/ {magenta}2 {white}]: {magenta}"))

if playit == 2:
    playit = True
else:
    playit = False
    
# go to workspace

original_name = name

try:
    os.mkdir(name)
except:
    print(f"\n  {white}> {red}The folder {white}{name} {red}already exists thus can't be created{white}! {red}Creating {white}{name}_new{red}...")
    name+= "_new"
    os.mkdir(name)

os.system(f"explorer.exe \"{name}\"")
os.chdir(name)

# extract dsb_assets.zip

zipfile.ZipFile(f"{filepath_temp}\dsb_assets.zip", 'r').extractall()

# begin download phase

os.system('cls')
print(f"\n  {white}> {magenta}Preparing Downloads{white}...")

to_download_urls = []
to_download_filenames = []

def downloader(url, filename):
    Success = False
    while not Success:
        try:
            data = requests.get(url, allow_redirects=True).content
            open(filename,"wb").write(data)
            data = ""
            print(f"\n  {white}> {magenta}Completed {white}{filename}{magenta}!")
            Success = True
        except:
            retry = input(f"\n  {white}> {red}Failed {white}{filename}{red}! Press {white}ENTER {red}to try again!")
    
# EssentialsX.jar

response = requests.get(f"https://api.github.com/repos/EssentialsX/Essentials/releases").json()
build = str(response[0]['tag_name'])

to_download_urls.append(f"https://github.com/EssentialsX/Essentials/releases/download/{build}/EssentialsX-{build}.jar")
to_download_filenames.append(f"plugins\EssentialsX-{build}.jar")

# EssentialsXChat.jar

to_download_urls.append(f"https://github.com/EssentialsX/Essentials/releases/download/{build}/EssentialsXChat-{build}.jar")
to_download_filenames.append(f"plugins\EssentialsXChat-{build}.jar")

# EssentialsXSpawn.jar

to_download_urls.append(f"https://github.com/EssentialsX/Essentials/releases/download/{build}/EssentialsXSpawn-{build}.jar")
to_download_filenames.append(f"plugins\EssentialsXSpawn-{build}.jar")

# ProtocolLib.jar

to_download_urls.append("https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/artifact/target/ProtocolLib.jar")
to_download_filenames.append(f"plugins\ProtocolLib.jar")

# TAB.jar

response = requests.get("https://api.github.com/repos/NEZNAMY/TAB/releases").json()

to_download_urls.append(str(response[0]['assets'][0]['browser_download_url']))
to_download_filenames.append(f"plugins\TAB.jar")

# BetterSleeping.jar

response = requests.get("https://api.github.com/repos/Nuytemans-Dieter/BetterSleeping/releases").json()

to_download_urls.append(str(response[0]['assets'][0]['browser_download_url']))
to_download_filenames.append(f"plugins\BetterSleeping.jar")

# ActionHealth.jar

response = requests.get("https://api.github.com/repos/zeshan321/ActionHealth/releases").json()

to_download_urls.append(str(response[0]['assets'][0]['browser_download_url']))
to_download_filenames.append(f"plugins\ActionHealth.jar")

# paperclip.jar

build = requests.get(f"https://papermc.io/api/v2/projects/paper/versions/{version}").json()
build = str(build['builds'][-1])

to_download_urls.append(f"https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{build}/downloads/paper-{version}-{build}.jar")
to_download_filenames.append("paperclip.jar")

# playit.gg tunnel prorgram

if playit:

    response = requests.get("https://playit.gg/download/")
    url = re.findall("https://playit.gg/downloads/playit-win[a-zA-Z0-9._-]+",str(response.content.decode()))
    playit_filename = str(url[0]).split('/')[-1]

    to_download_urls.append(str(url[0]))
    to_download_filenames.append(playit_filename)

# OpenJDK-16.msi

if download_jdk == "y":

    random_ua = str(random.choice(list(set(requests.get("https://raw.githubusercontent.com/DavidWittman/requests-random-user-agent/master/requests_random_user_agent/useragents.txt").content.decode().splitlines()))))

    headers = {
        "Host": "api.adoptium.net",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": random_ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = requests.get("https://api.adoptium.net/v3/assets/feature_releases/16/ga?architecture=x64&heap_size=normal&image_type=jdk&jvm_impl=hotspot&os=windows&page=0&page_size=10&project=jdk&sort_method=DEFAULT&sort_order=DESC&vendor=adoptium", headers=headers).json()

    installer_url = str(response[0]["binaries"][0]["installer"]["link"])
    jdk_filename = installer_url.split("/")[-1]

    to_download_urls.append(installer_url)
    to_download_filenames.append(jdk_filename)

# log4j exploit patch

log4j = f'''

{red}888                       {yellow}    d8888  {red}         888               888 888 
{red}888                       {yellow}   d8P888  {red}         888               888 888 
{red}888                       {yellow}  d8P 888  {red}         888               888 888 
{red}888      .d88b.   .d88b.  {yellow} d8P  888  {red}.d8888b  88888b.   .d88b.  888 888 
{red}888     d88""88b d88P"88b {yellow}d88   888  {red}88K      888 "88b d8P  Y8b 888 888 
{red}888     888  888 888  888 {yellow}8888888888 {red}"Y8888b. 888  888 88888888 888 888 
{red}888     Y88..88P Y88b 888 {yellow}      888  {red}     X88 888  888 Y8b.     888 888 
{red}88888888 "Y88P"   "Y88888 {yellow}      888  {red} 88888P' 888  888  "Y8888  888 888 
{red}                      888                                               
{red}                 Y8b d88P                                               
{red}                  "Y88P"                                                

'''

if ( "1.17" or "1.18" ) in version:
    extra_flag = "-Dlog4j2.formatMsgNoLookups=true "
elif ( "1.12" or "1.13" or "1.14" or "1.15" or "1.16" ) in version:
    extra_flag = "-Dlog4j.configurationFile=log4j2_112-116.xml "
    to_download_urls.append("https://launcher.mojang.com/v1/objects/02937d122c86ce73319ef9975b58896fc1b491d1/log4j2_112-116.xml")
    to_download_filenames.append("log4j2_112-116.xml")
elif ( "1.7" or "1.8" or "1.9" or "1.10" or "1.11" ) in version:
    extra_flag = "-Dlog4j.configurationFile=log4j2_17-111.xml "
    to_download_urls.append("https://launcher.mojang.com/v1/objects/4bb89a97a66f350bc9f73b3ca8509632682aea2e/log4j2_17-111.xml")
    to_download_filenames.append("log4j2_17-111.xml")
else:
    extra_flag = ""

# begin downloads

print(f"\n  {white}> {magenta}Starting Multiple Downloads{white}... [ {magenta}this might take a minute {white}]")

start_time = time.time()

futures = []
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
for i in range(len(to_download_urls)):
    futures.append(executor.submit(downloader, to_download_urls[i], to_download_filenames[i]))
for future in concurrent.futures.as_completed(futures):
    try:
        future.result()
    except:
        pass
futures.clear()

time_taken = ( time.time() - start_time ) / 60

os.system('cls')
print(f"\n  {white}> {magenta}Finished All Downloads in {white}{{0:.1f}} {magenta}minutes{white}!".format(time_taken))
print(f"\n  {white}> {magenta}Updating {white}server.properties")

# updating server.properties

data = open("server.properties","r").read().replace("motd=A Minecraft Server",f"motd=\\u00A7a---\\u00A76>\\u00A7b\\u00A7l {original_name} \\u00A76<\\u00A7a---")

if offline == "y":
    data.replace("online-mode=true","online-mode=false")

open("server.properties","w").write(data)

print(f"\n  {white}> {magenta}Creating batch scripts...")

# Creating .cmd(s)

data = f'''@echo off
color 0a
title Minecraft Server Console [ {name} ]
java -Xms512M -Xmx{ram}M -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch {extra_flag}-jar paperclip.jar -nogui
pause
'''

open("start_server.cmd","w").write(data)

data = f'''#!/bin/sh
java -Xms512M -Xmx{ram}M -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch {extra_flag}-jar paperclip.jar -nogui
'''

open("start_server.sh","wb").write(data.encode().replace(b'\r\n',b'\n'))

data = f'''@echo off
color 0a
title Minecraft Java Playit.gg Tunnel [ {name} ] Keep me running to allow players to join your server!
{playit_filename}
pause
'''

open("start_tunnel.cmd","w").write(data)

# log4j notice

os.system('cls')
sys.stdout.write(aligner(log4j.replace(red,"").replace(yellow,""), log4j))
print(f"\n  {white}> {magenta}Minecraft servers built with {white}dank.serverbuilder {magenta}are protected from the {red}log{yellow}4{red}shell {magenta}exploit!")
time.sleep(10)
os.system('cls')

# begin installation phase

if download_jdk == "y":

    print(f"\n  {white}> {magenta}Starting {white}OpenJDK-16.msi")
    time.sleep(3)
    try:
        os.startfile(jdk_filename)
    except:
        print(f"\n  {white}> {red}Failed! Please run {white}{jdk_filename} {red}manually!")

    temp = str(input(f"\n  {white}> {magenta}Once you have sucessfully installed and closed {white}OpenJDK-16 {magenta}hit {white}[ {magenta}enter {white}] {magenta}to delete the installer{white}: {magenta}"))
    os.remove(jdk_filename)

os.system('cls')
sys.stdout.write(aligner(read_me, read_me_colored))

# one-time setup

if playit:
    
    print(f"\n  {white}> {magenta}To allow players to connect to your server you first need to create a tunnel.")
    print(f"\n  {white}> {magenta}Follow the steps on {white}imgur {magenta}and complete the {white}one-time setup{magenta}.")
    print(f"\n  {white}> {magenta}If it does not open, please go to {white}https://imgur.com/a/W30s7bw {magenta}and {white}https://playit.gg/manage {magenta}manually.")
    print(f"\n  {white}> {magenta}Opening in 10s...")
    time.sleep(10)
    web.open_new_tab("https://imgur.com/a/W30s7bw")
    time.sleep(10)
    web.open_new_tab("https://playit.gg/manage")
    print(f"\n  {white}> {magenta}To start your server, run {white}start_server.cmd")
    print(f"\n  {white}> {magenta}To start your tunnel so people can connect over the internet, run {white}start_tunnel.cmd")
    wait = input(f"\n  {white}> {magenta}After you have read the above and created a tunnel, press {white}[ ENTER ] ")
    
else:
    
    print(f"\n  {white}> {magenta}As you have not selected {white}playit.gg{magenta}, To allow players to connect to your server over the internet, follow this tutorial on {white}port forwarding.")
    open_youtube = str(input(f"  {white}> {magenta}Do you want to open {white}port forwarding tutorial {magenta}on {white}youtube{magenta}? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()

    if open_youtube == "y":
        web.open_new_tab("https://youtu.be/X75GbRaGzu8")

# done!

os.system(f"title dank.serverbuilder [ complete! ]")

complete = f'''



 ___  ___ _ ____   _____ _ __                 
/ __|/ _ \ '__\ \ / / _ \ '__|                
\__ \  __/ |   \ V /  __/ |                   
|___/\___|_|    \_/ \___|_|                   

                     _   _                    
  ___ _ __ ___  __ _| |_(_) ___  _ __         
 / __| '__/ _ \/ _` | __| |/ _ \| '_ \        
| (__| | |  __/ (_| | |_| | (_) | | | |       
 \___|_|  \___|\__,_|\__|_|\___/|_| |_|       

                           _      _         _ 
  ___ ___  _ __ ___  _ __ | | ___| |_ ___  / \\
 / __/ _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \/  /
| (_| (_) | | | | | | |_) | |  __/ ||  __/\_/ 
 \___\___/|_| |_| |_| .__/|_|\___|\__\___\/   
                    |_|                       

'''

complete_colored = (red + complete).splitlines()

os.system('cls')
sys.stdout.write(aligner(complete, complete_colored))
time.sleep(3)
web.open_new_tab("https://allmylinks.com/sir-dankenstein")
