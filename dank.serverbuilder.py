import os
import re
import sys
import time
import random
import zipfile
import requests
import webbrowser as web
from cloudscraper import (
    CloudScraper,
    CloudflareIUAMError,
    CloudflareCaptchaError,
    CloudflareChallengeError,
    CloudflareSolveError
)
from asyncthread import Thread
from colorama import init, Fore, Style
from fake_useragent import UserAgent

try:
    filepath = os.path.dirname(__file__) # as .py
    #filepath = os.path.dirname(sys.executable) # as .exe
    filepath_temp = os.path.dirname(__file__) # for .exe
    os.chdir(filepath)
except:
    pass

ua = UserAgent()

init(autoreset=True)
white = Fore.WHITE + Style.BRIGHT
pink = Fore.MAGENTA + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT

# print banner

def banner():
    banner = '''

              ______               __       _______                             _______       __ __    __            
             |   _  \ .---.-.-----|  |--.  |   _   .-----.----.--.--.-----.----|   _   .--.--|__|  .--|  .-----.----.
             |.  |   \|  _  |     |    < __|   1___|  -__|   _|  |  |  -__|   _|.  1   |  |  |  |  |  _  |  -__|   _|
             |.  |    |___._|__|__|__|__|__|____   |_____|__|  \___/|_____|__| |.  _   |_____|__|__|_____|_____|__|  
             |:  1    /                    |:  1   |                           |:  1    \                            
             |::.. . /                     |::.. . |                           |::.. .  /                            
             `------'                      `-------'                           `-------'                             

'''
    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]
    return ''.join(colored_chars)

sys.stdout.write(banner())

# get available versions and print

response = requests.get("https://papermc.io/api/v2/projects/paper/").json()
available_versions = f"\n{white}> {pink}Available Paper Versions{white}: {pink}" + str(response['versions']).replace("[","").replace("]","").replace("\'","").replace(".",f"{white}.{pink}").replace(",",f"{white},{pink}")
print(available_versions)
available_versions = available_versions.replace(f"{white}","").replace(f"{pink}","")

# input

name = str(input(f"\n{white}> {pink}Server Name{white}: {pink}"))
version = str(input(f"\n{white}> {pink}Version{white}: {pink}"))
while version not in available_versions:
    print(f"\n{white}> {red}That version is not supported{white}!")
    version = str(input(f"\n{white}> {pink}Version{white}: {pink}"))
ram = str(input(f"\n{white}> {pink}RAM in MB{white}: {pink}"))
offline = str(input(f"\n{white}> {pink}Allow Cracked Players {white}[ {pink}y {white}/ {pink}n {white}]: {pink}"))

print(f"\n{white}> {pink}The following step is {white}required {pink}to run a minecraft server of version 1{white}.{pink}17 and above{white}!")
print(f"{white}> {pink}If you do not know or are unsure, hit {white}[ {pink}enter {white}] {pink}it will download the installer{white}.")
skip_jdk = str(input(f"{white}> {pink}Do you have {white}OpenJDK-16 {pink}installed? {white}[ {pink}y {white}/ {pink}n {white}]: {pink}")).lower()

read_me = f'''

        :::::::::  ::::::::::     :::     :::::::::       ::::    ::::  ::::::::::
        :+:    :+: :+:          :+: :+:   :+:    :+:      +:+:+: :+:+:+ :+:       
        +:+    +:+ +:+         +:+   +:+  +:+    +:+      +:+ +:+:+ +:+ +:+       
        +#++:++#:  +#++:++#   +#++:++#++: +#+    +:+      +#+  +:+  +#+ +#++:++#  
        +#+    +#+ +#+        +#+     +#+ +#+    +#+      +#+       +#+ +#+       
        #+#    #+# #+#        #+#     #+# #+#    #+#      #+#       #+# #+#       
        ###    ### ########## ###     ### #########       ###       ### ##########
'''

read_me = read_me.replace(":",f"{white}:").replace("+",f"{white}+").replace("#",f"{pink}#")

print(read_me)

print(f"\n{white}> {pink}Prefarably use {white}port forwarding {pink}over {white}noip.com {pink}and {white}noip.com {pink}over {white}ngrok{pink}, Note{white}: {pink}there is a monthly manual renewal (free) for each domain used in {white}noip.com")
print(f"{white}> Port forwarding {pink}is not hard at all! A tutorial has been provided at the end of this script{white}.")
print(f"{white}> {pink}If you do wish to {white}port forward {pink}you can skip {white}noip.com {pink}and {white}ngrok.")

print(f"\n{white}> {pink}The following step is {white}not required {pink}to host a minecraft server if you are {white}port forwarding {pink}or using {white}ngrok")
print(f"{white}> {pink}If you do not want to port forward, hit {white}[ {pink}enter {white}] {pink}it will open {white}noip.com")
open_noip = str(input(f"{white}> {pink}Do you want to open {white}noip.com{pink}? {white}[ {pink}y {white}/ {pink}n {white}]: {pink}")).lower()

if open_noip != "n":
    print(f"\n{white}> {pink}Opening {white}noip.com")
    web.open_new_tab("https://www.noip.com/download?page=win")

print(f"\n{white}> {pink}The following step is {white}not required {pink}to host a minecraft server if you are {white}portforwarding {pink}or using {white}noip.com's {pink}Dynamic DNS Update Client{white}.")
print(f"{white}> {pink}If you do not want to port forward, hit {white}[ {pink}enter {white}] {pink}it will download ngrok{white}.")
skip_ngrok = str(input(f"{white}> {pink}Do you want to skip {white}ngrok{pink}? {white}[ {pink}y {white}/ {pink}n {white}]: {pink}")).lower()

# go to workspace

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

print(f"\n{white}> {pink}Preparing Downloads{white}...")

to_download_urls = []
to_download_filenames = []

def downloader(url, filename):
    data = requests.get(url, allow_redirects=True).content
    open(filename,"wb").write(data)
    data = ""
    print(f"\n{white}> {pink}Completed {white}{filename}{pink}!")

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

if skip_ngrok != "y":

    to_download_urls.append("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip")
    to_download_filenames.append("ngrok.zip")

# OpenJDK-16.msi

if skip_jdk != "y":

    try:
        scraper = CloudScraper()
        headers = {
            "Host": "api.adoptium.net",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": str(ua.random),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "X-Requested-With": "XMLHttpRequest"
        }

        response = scraper.get("https://api.adoptium.net/v3/assets/feature_releases/16/ga?architecture=x64&heap_size=normal&image_type=jdk&jvm_impl=hotspot&os=windows&page=0&page_size=10&project=jdk&sort_method=DEFAULT&sort_order=DESC&vendor=adoptium").json()

        matches = re.findall("https://github.com/adoptium/[a-zA-Z0-9/%._-]+msi",str(response))
        matches = list(set(matches))

        installer_filename = str(matches[0]).split("/")[-1]

        to_download_urls.append(f"{matches[0]}")
        to_download_filenames.append(installer_filename)

    except requests.RequestException:
        print(f"\n{white}> {red}Requests Error")
        sys.exit()
    except CloudflareIUAMError:
        print(f"\n{white}> {red}Cloudflare IUAM Error")
        sys.exit()
    except CloudflareCaptchaError:
        print(f"\n{white}> {red}Cloudflare Captcha Error")
        sys.exit()
    except CloudflareChallengeError:
        print(f"\n{white}> {red}Cloudflare Challange Error")
        sys.exit()
    except CloudflareSolveError:
        print(f"\n{white}> {red}Cloudflare Solve Error")
        sys.exit()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(f"{red}Error{white}: {red}{str(e)} {white}| {red}{exc_type} {white}| {red}Line{white}: {red}{exc_tb.tb_lineno}")
        wait = input("\nPress Enter to continue...\n\n")
        sys.exit()

# begin downloads

print(f"\n{white}> {pink}Starting Multiple Downloads{white}... [ {pink}this might take a few minutes {white}]")

start_time = time.time()

thread = Thread(func=[downloader(to_download_urls[i], to_download_filenames[i]) for i in range(len(to_download_urls))], workers=20)
thread.start()
thread.join()

time_taken = ( time.time() - start_time ) / 60

print(f"\n{white}> {pink}Finished All Downloads in {white}{{0:.1f}} {pink}minutes{white}!".format(time_taken))
print(f"\n{white}> {pink}Updating {white}server.properties")

# updating server.properties

data = open("server.properties","r").read().replace("motd=A Minecraft Server",f"motd=\\u00A7a---\\u00A76>\\u00A7b\\u00A7l {name} \\u00A76<\\u00A7a---")

if offline == "y":
    data.replace("online-mode=true","online-mode=false")

open("server.properties","w").write(data)

print(f"\n{white}> {pink}Creating batch scripts...")

# Creating .cmd(s)

data = f'''@echo off
color 0a
title Minecraft Server Console [ {name} ]
java -Xmx{ram}M -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch -jar paperclip.jar -nogui
pause
'''

open("start_server.cmd","w").write(data)

data = f'''#!/bin/sh
java -Xmx{ram}M -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch -jar paperclip.jar -nogui
'''

open("start_server.sh","w").write(data)

if skip_ngrok != "y":

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
java -Xmx{ram}M -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch -jar paperclip.jar -nogui
pause
'''

    open("start_server_and_ngrok.cmd","w").write(data)

# begin installation phase

if skip_ngrok != "y":

    zipfile.ZipFile("ngrok.zip", 'r').extractall()
    os.remove("ngrok.zip")

    print(f"\n{white}> {pink}Go to Authentication {white}> {pink}Your Authtoken and click copy, then paste it here{white}.")
    print(f"{white}> {pink}Opening {white}ngrok.com {pink}in {white}15 {pink}seconds.")

    time.sleep(15)
    web.open_new_tab("https://dashboard.ngrok.com/auth/your-authtoken")
    ngrok_token = str(input(f"\n{white}> {pink}Ngrok Auth Token{white}: {pink}"))
    print()
    os.system(f"ngrok.exe authtoken {ngrok_token}")

if skip_jdk != "y":

    print(f"\n{white}> {pink}Starting {white}OpenJDK-16.msi")
    os.system(f"start {installer_filename}")

    temp = str(input(f"{white}> {pink}Once you have sucessfully installed and closed {white}OpenJDK-16 {pink}hit {white}[ {pink}enter {white}] {pink}to delete the installer{white}: {pink}"))
    os.remove(installer_filename)

print(read_me)

if skip_ngrok != "y":
    print(f"\n{white}> {pink}To start your server, run {white}start_server_and_ngrok.cmd")
    print(f"{white}> {pink}To allow players to connect to your server over the internet, {white}ngrok {pink}must be running. This is for if you do not wish to {white}port forward {pink}or use {white}noip.com's {pink}Dynamic DNS Update Client{white}.")
    print(f"{white}> {pink}Your servers IP is shown in the ngrok window, it looks something like this {white}> {pink}0.tcp.ngrok.io:00000 {white}< {pink}last 5 digits will be random.")
else:
    print(f"\n{white}> {pink}To start your server, run {white}start_server.cmd")

if open_noip != "n":
    print(f"{white}> {pink}To allow players to connect to your server over the internet, follow this tutorial on using {white}noip{pink}. This is for if you do not wish to {white}port forward {pink}or use {white}ngrok.")
    open_youtube = str(input(f"{white}> {pink}Do you want to open {white}noip tutorial {pink}on {white}youtube{pink}? {white}[ {pink}y {white}/ {pink}n {white}]: {pink}")).lower()

    if open_youtube == "y":
        web.open_new_tab("https://youtu.be/L9tbsra48c0")

print(f"{white}> {pink}To allow players to connect to your server over the internet, follow this tutorial on {white}port forwarding. This is for if you do not wish to use {white}noip.com {pink}or {white}ngrok.")
open_youtube = str(input(f"{white}> {pink}Do you want to open {white}port forwarding tutorial {pink}on {white}youtube{pink}? {white}[ {pink}y {white}/ {pink}n {white}]: {pink}")).lower()

if open_youtube == "y":
    web.open_new_tab("https://youtu.be/X75GbRaGzu8")

complete = f'''{red}

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

print(complete)
time.sleep(5)
web.open_new_tab("https://allmylinks.com/sir-dankenstein")