# the below imports are not required by the executor.py but is required by dank.serverbuilder.py

import re
import random
import zipfile
import concurrent.futures

# required imports for executor.py

import os
import sys
import time
import requests
from packaging import version
from colorama import init, Fore, Style

os.system("title dank.serverbuilder [ initializing ]")

# colors

init(autoreset=True)
red = Fore.RED + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT
white = Fore.WHITE + Style.BRIGHT

if __name__ == "__main__":

    project = "dank.serverbuilder"
    current_version = 2.1
    print(f"\n  {white}> {magenta}Version{white}: {current_version}")
    os.chdir(os.path.dirname(sys.argv[0]))

    # remove old build if exists

    try:os.remove(f"{project}.exe")
    except:pass
    
    # get latest version

    while True:
        try:
            latest_version = requests.get(f"https://raw.githubusercontent.com/SirDankenstien/{project}/main/executor_version.txt").content.decode()
            if "Not Found" in str(latest_version):latest_version = 0
            else:latest_version = float(latest_version)
            break
        except:
            wait = input(f"\n  {white}> {red}Failed to check for an update! Make sure you are connected to the Internet! Press {white}Enter {red}to try again.")

    # version checker / updater

    def download_latest():
        print(f"\n  {white}> {magenta}Downloading {white}{project}-latest.exe{magenta}...")
        data = requests.get(f"https://github.com/SirDankenstien/{project}/blob/main/{project}.exe?raw=true", allow_redirects=True).content
        open(f"{project}-latest.exe","wb").write(data)
        data = None
        print(f"\n  {white}> {magenta}Downloaded!\n\n  {white}> {magenta}Starting in 5s...")
        time.sleep(5)
        os.system(f"start {project}-latest.exe")
        sys.exit()

    if version.parse(str(latest_version)) > version.parse(str(current_version)):
        choice = str(input(f"\n  {white}> {magenta}Update Found{white}: {latest_version}\n\n  {white}> {magenta}Download latest version? {white}[ {magenta}y {white}/ {magenta}n {white}]: {magenta}")).lower()
        if choice == "y":download_latest()

    elif latest_version == current_version:
        print(f"\n  {white}> {magenta}Latest Version!")
    else:
        print(f"\n  {white}> {magenta}Development Version!")
    time.sleep(3)

    # get src from github

    while True:
        try:
            code = str(requests.get(f"https://raw.githubusercontent.com/SirDankenstien/{project}/main/{project}.py").content.decode())
            break
        except:
            wait = input(f"\n  {white}> {red}Failed to get src! Make sure you are connected to the Internet! Press {white}Enter {red}to try again")

    # execute, catch errors if any

    os.system("title dank.serverbuilder")

    try:exec(code)
    except Exception as exp:

        exc_type, exc_obj, exc_tb = sys.exc_info()
        os.system('cls')
        print(f"\n  {white}> {red}Error: {str(exp)} {white}| {red}{exc_type} {white}| {red}Line: {exc_tb.tb_lineno}")
        print(f"\n  {white}> {magenta}Please take a screenshot of this and post it on {white}https://github.com/SirDankenstien/dank.serverbuilder/issues/new")

        if not latest_version == current_version:
            choice = input(f"\n{white}> {magenta}Would you like to download the latest executor [ {white}y {magenta}/ {white}n {magenta}]: {white}").lower()
            if choice == "y":download_latest()
            
        wait = print(f"\n  {white}> {magenta}Press {white}ENTER {magenta}to continue: ")
