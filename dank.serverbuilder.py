import os
import re
import sys
import time
import random
import zipfile
import requests
import webbrowser as web
import concurrent.futures
from packaging import version
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

# print banner

banner_ascii = '''

 ______               __       _______                             _______       __ __    __            
|   _  \ .---.-.-----|  |--.  |   _   .-----.----.--.--.-----.----|   _   .--.--|__|  .--|  .-----.----.
|.  |   \|  _  |     |    < __|   1___|  -__|   _|  |  |  -__|   _|.  1   |  |  |  |  |  _  |  -__|   _|
|.  |    |___._|__|__|__|__|__|____   |_____|__|  \___/|_____|__| |.  _   |_____|__|__|_____|_____|__|  
|:  1    /                    |:  1   |                           |:  1    \                            
|::.. . /                     |::.. . |                           |::.. .  /                            
`------'                      `-------'                           `-------'                             


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
sys.stdout.write(aligner(banner_ascii, banner_ascii_colored))

# updater

project = "dank.serverbuilder"
current_version = 1.4
print(f"\n{white}> {magenta}Version{white}: {current_version}")

try:
    os.remove(f"{project}.exe")
except:
    pass

Success = False
while not Success:
    try:
        latest_version = requests.get(f"https://raw.githubusercontent.com/SirDankenstien/{project}/main/version.txt").content.decode()
        if "Not Found" in str(latest_version):
            latest_version = 0
        else:
            latest_version = float(latest_version)
        Success = True
    except:
        wait = input(f"\n{white}> {red}Failed to check for an update! Make sure you are connected to the Internet! Press {white}Enter {red}to try again.")

if version.parse(str(latest_version)) > version.parse(str(current_version)):

    choice = str(input(f"\n{white}> {magenta}Update Found{white}: {latest_version}\n\n{white}> {magenta}Download latest version? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()
    if choice == "y":
        print(f"\n{white}> {magenta}Downloading {white}{project}-latest.exe{magenta}...")
        data = requests.get(f"https://github.com/SirDankenstien/{project}/blob/main/{project}.exe?raw=true", allow_redirects=True).content
        open(f"{project}-latest.exe","wb").write(data)
        data = None
        print(f"\n{white}> {magenta}Downloaded!\n\n{magenta}Terminating in 5s...")
        time.sleep(5)
        sys.exit()

#elif latest_version == current_version:
#    print(f"\n{white}> {magenta}Latest Version!")
#else:
#    print(f"\n{white}> {magenta}Development Version!")

# get available versions and print

Success = False
while not Success:
    try:
        response = requests.get("https://papermc.io/api/v2/projects/paper/").json()
        available_versions = f"\n{white}> {magenta}Available Paper Versions{white}: {magenta}" + str(response['versions']).replace("[","").replace("]","").replace("\'","").replace(".",f"{white}.{magenta}").replace(",",f"{white},{magenta}")
        print(available_versions)
        available_versions = available_versions.replace(f"{white}","").replace(f"{magenta}","")
        Success = True
    except:
        wait = input(f"\n{white}> {red}Failed to get paper versions! Make sure you are connected to the Internet! Press {white}Enter {red}to try again.")

# input

name = str(input(f"\n{white}> {magenta}Server Name{white}: {magenta}"))
version = str(input(f"\n{white}> {magenta}Version{white}: {magenta}"))

# check if version is available

versions_list = available_versions.replace(",","").replace(f"{white}","").replace(f"{magenta}","").split(" ")
version_available = False

def version_check():
    for ver in versions_list:
        if version == ver:
            global version_available
            version_available = True

version_check()

while not version_available:
    print(f"\n{white}> {red}That version is not supported{white}!")
    version = str(input(f"\n{white}> {magenta}Version{white}: {magenta}"))
    version_check()
ram = str(input(f"\n{white}> {magenta}RAM in MB {white}[ {magenta}Above 512 {white}]: {magenta}"))
offline = str(input(f"\n{white}> {magenta}Allow Cracked Players {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}"))

print(f"\n{white}> {magenta}The following step is {white}required {magenta}to run a minecraft paper server of version 1{white}.{magenta}17 and above{white}!")
print(f"{white}> {magenta}If you do not know or are unsure, type {white}\"{magenta}y{white}\"")
download_jdk = str(input(f"{white}> {magenta}Do you want to download {white}OpenJDK-16{magenta}? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()

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

print(f"\n{white}> {magenta}Prefarably use {white}port forwarding {magenta}over {white}noip.com {magenta}and {white}noip.com {magenta}over {white}ngrok")
print(f"{white}> {magenta}Note{white}: {magenta}there is a monthly manual renewal {white}({magenta}free{white}) {magenta}for each domain used in {white}noip.com")
print(f"{white}> Port forwarding {magenta}is not hard at all! A tutorial has been provided at the end of this script{white}.")
print(f"{white}> {magenta}If you do wish to {white}port forward {magenta}you can skip {white}noip.com {magenta}and {white}ngrok.")

print(f"\n{white}> {magenta}The following step is {white}not required {magenta}to host a minecraft server if you are either {white}port forwarding {magenta}or using {white}ngrok")
open_noip = str(input(f"{white}> {magenta}Do you want to open {white}noip.com{magenta}? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()

if open_noip == "y":
    print(f"\n{white}> {magenta}Opening {white}noip.com")
    web.open_new_tab("https://www.noip.com/download?page=win")

print(f"\n{white}> {magenta}The following step is {white}not required {magenta}to host a minecraft server if you are either {white}port forwarding {magenta}or using {white}noip.com's {magenta}Dynamic DNS Update Client{white}.")
download_ngrok = str(input(f"{white}> {magenta}Do you want to download {white}ngrok{magenta}? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()

# go to workspace

original_name = name

try:
    os.mkdir(name)
except:
    print(f"\n{white}> {red}The folder {white}{name} {red}already exists thus can't be created{white}! {red}Creating {white}{name} 2{red}...")
    name+= " 2"
    os.mkdir(name)

os.system(f"explorer.exe \"{name}\"")
os.chdir(name)

# extract DankServerBuilder.zip

zipfile.ZipFile(f"{filepath_temp}\DankServerBuilder.zip", 'r').extractall()

# begin download phase

os.system('cls')
print(f"\n{white}> {magenta}Preparing Downloads{white}...")

to_download_urls = []
to_download_filenames = []

def downloader(url, filename):
    data = requests.get(url, allow_redirects=True).content
    open(filename,"wb").write(data)
    data = ""
    print(f"\n{white}> {magenta}Completed {white}{filename}{magenta}!")

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

# ngrok-stable-windows-amd64.zip

if download_ngrok == "y":

    to_download_urls.append("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip")
    to_download_filenames.append("ngrok.zip")

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
    installer_filename = installer_url.split("/")[-1]

    to_download_urls.append(installer_url)
    to_download_filenames.append(installer_filename)

# begin downloads

print(f"\n{white}> {magenta}Starting Multiple Downloads{white}... [ {magenta}this might take a minute {white}]")

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
print(f"\n{white}> {magenta}Finished All Downloads in {white}{{0:.1f}} {magenta}minutes{white}!".format(time_taken))
print(f"\n{white}> {magenta}Updating {white}server.properties")

# updating server.properties

data = open("server.properties","r").read().replace("motd=A Minecraft Server",f"motd=\\u00A7a---\\u00A76>\\u00A7b\\u00A7l {original_name} \\u00A76<\\u00A7a---")

if offline == "y":
    data.replace("online-mode=true","online-mode=false")

open("server.properties","w").write(data)

print(f"\n{white}> {magenta}Creating batch scripts...")

# Creating .cmd(s)

data = f'''@echo off
color 0a
title Minecraft Server Console [ {name} ]
java -Xms512M -Xmx{ram}M -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch -jar paperclip.jar -nogui
pause
'''

open("start_server.cmd","w").write(data)

data = f'''#!/bin/sh
java -Xms512M -Xmx{ram}M -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch -jar paperclip.jar -nogui
'''

open("start_server.sh","w").write(data)

if download_ngrok == "y":

    data = '''@echo off
title Ngrok Tunnel
ngrok tcp 25565
pause
'''

    open("start_only_ngrok.cmd","w").write(data)

    data = f'''@echo off
color 0a
title Minecraft Server Console [ {name} ]
start start_only_ngrok.cmd
java -Xms512M -Xmx{ram}M -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch -jar paperclip.jar -nogui
pause
'''

    open("start_server_and_ngrok.cmd","w").write(data)

# begin installation phase

if download_ngrok == "y":

    zipfile.ZipFile("ngrok.zip", 'r').extractall()
    os.remove("ngrok.zip")

    print(f"\n{white}> {magenta}Go to Authentication {white}> {magenta}Your Authtoken and click copy, then paste it here{white}.")
    print(f"{white}> {magenta}Opening {white}ngrok.com {magenta}in {white}15 {magenta}seconds.")

    time.sleep(15)
    web.open_new_tab("https://dashboard.ngrok.com/auth/your-authtoken")
    ngrok_token = str(input(f"\n{white}> {magenta}Ngrok Auth Token{white}: {magenta}"))
    print()
    os.system(f"ngrok.exe authtoken {ngrok_token}")

if download_jdk == "y":

    print(f"\n{white}> {magenta}Starting {white}OpenJDK-16.msi")
    os.system(f"start {installer_filename}")

    temp = str(input(f"\n{white}> {magenta}Once you have sucessfully installed and closed {white}OpenJDK-16 {magenta}hit {white}[ {magenta}enter {white}] {magenta}to delete the installer{white}: {magenta}"))
    os.remove(installer_filename)

os.system('cls')
sys.stdout.write(aligner(read_me, read_me_colored))

if download_ngrok == "y":
    print(f"\n{white}> {magenta}To start your server, run {white}start_server_and_ngrok.cmd")
    print(f"{white}> {magenta}To allow players to connect to your server over the internet, {white}ngrok {magenta}must be running. This is for if you do not wish to {white}port forward {magenta}or use {white}noip.com's {magenta}Dynamic DNS Update Client{white}.")
    print(f"{white}> {magenta}Your servers IP is shown in the ngrok window, it looks something like this {white}> {magenta}0.tcp.ngrok.io:00000 {white}< {magenta}last 5 digits will be random.")
else:
    print(f"\n{white}> {magenta}To start your server, run {white}start_server.cmd")

if open_noip == "y":
    print(f"{white}> {magenta}To allow players to connect to your server over the internet, follow this tutorial on using {white}noip{magenta}. This is for if you do not wish to {white}port forward {magenta}or use {white}ngrok.")
    open_youtube = str(input(f"{white}> {magenta}Do you want to open {white}noip tutorial {magenta}on {white}youtube{magenta}? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()

    if open_youtube == "y":
        web.open_new_tab("https://youtu.be/L9tbsra48c0")

print(f"\n{white}> {magenta}To allow players to connect to your server over the internet, follow this tutorial on {white}port forwarding. {magenta}This is for if you do not wish to use {white}noip.com {magenta}or {white}ngrok.")
open_youtube = str(input(f"{white}> {magenta}Do you want to open {white}port forwarding tutorial {magenta}on {white}youtube{magenta}? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()

if open_youtube == "y":
    web.open_new_tab("https://youtu.be/X75GbRaGzu8")

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
time.sleep(5)
web.open_new_tab("https://allmylinks.com/sir-dankenstein")
