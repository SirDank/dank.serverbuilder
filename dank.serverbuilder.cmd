@echo off
title Dank Minecraft Server Builder
echo "============================================================================================="
echo "  _____              _       _____                          ____        _ _     _            "
echo " |  __ \            | |     / ____|                        |  _ \      (_) |   | |           "
echo " | |  | | __ _ _ __ | | __ | (___   ___ _ ____   _____ _ __| |_) |_   _ _| | __| | ___ _ __  "
echo " | |  | |/ _` | '_ \| |/ /  \___ \ / _ \ '__\ \ / / _ \ '__|  _ <| | | | | |/ _` |/ _ \ '__| "
echo " | |__| | (_| | | | |   < _ ____) |  __/ |   \ V /  __/ |  | |_) | |_| | | | (_| |  __/ |    "
echo " |_____/ \__,_|_| |_|_|\_(_)_____/ \___|_|    \_/ \___|_|  |____/ \__,_|_|_|\__,_|\___|_|    "
echo "                                                                                             "
echo "============================================================================================="                                                                                            
color 09
color 0b
color 0c
color 0d
color 0e
color 0a
color 09
color 0b
color 0c
color 0d
color 0e
color 0a
color 09
color 0b
color 0c
color 0d
color 0e
color 0a

echo.
echo Helps you build and host a minecraft paper server using ngrok!
echo.
set /P name=Server Name: 

echo.
for /F %%a in ('"curl -s https://papermc.io/api/v2/projects/paper/"') do set versions=%%a >nul 2>nul
set versions=%versions:{"project_id":"paper","project_name":"Paper","version_groups":[=%
set versions=%versions:"versions":[=%
set versions=%versions:"=%
set versions=%versions:[=%
set versions=%versions:]=%
set versions=%versions:{=%
set versions=%versions:}=%
set "versions=%versions:,=, %"
echo Available Versions: %versions%
echo.

set /P minecraft_version=Minecraft Paper Version: 
echo.
set /P ram=RAM in MB: 
echo.
set /P offline=Allow Cracked Players [ y / n ]: 
if "%offline%" == "y" ( echo "-----> Run configure_server.cmd only after you have run the server for the first time!" )

md C:\DankServerBuilder
cd C:\DankServerBuilder
md C:\DankServerBuilder\plugins
explorer.exe C:\DankServerBuilder

echo.
echo "-----> Downloading Minecraft [Paper] %minecraft_version%... "
for /f "delims=" %%a in ('powershell.exe -Command "Invoke-WebRequest https://papermc.io/api/v2/projects/paper/versions/$env:minecraft_version | ConvertFrom-Json | Select -expand builds"') do set build=%%a
set downloadurl=https://www.dropbox.com/s/pmyapxkwoqxjgm6/server-icon.png?dl=1
set downloadpath=C:\DankServerBuilder\server-icon.png
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
set downloadurl=https://papermc.io/api/v2/projects/paper/versions/%minecraft_version%/builds/%build%/downloads/paper-%minecraft_version%-%build%.jar
set downloadpath=C:\DankServerBuilder\paper.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Please manually download and install Java Development Kit 16... "
echo "-----> Click on Windows and your download should start shortly... "
echo "-----> You could skip this if the server version is 1.16.5 or below and already have Java installed... "
powershell.exe -Command "Start-Process https://adoptium.net/"
set /P done=Hit [ENTER] to continue...

echo.
echo "-----> Downloading Ngrok.zip... "
set downloadurl=https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip
set downloadpath=C:\DankServerBuilder\ngrok.zip
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Unzipping Ngrok.zip... "
powershell.exe -Command "Expand-Archive -Force -Path ngrok.zip -DestinationPath C:\DankServerBuilder" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading DankServerBuilder.zip... "
set downloadurl=https://www.dropbox.com/s/jooobguiazciceq/DankServerBuilder.zip?dl=1
set downloadpath=C:\DankServerBuilder\DankServerBuilder.zip
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Unzipping DankServerBuilder.zip... "
powershell.exe -Command "Expand-Archive -Force -Path DankServerBuilder.zip -DestinationPath C:\DankServerBuilder" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading Plugin [EssentialsX]... "
for /f "delims=" %%a in ('powershell.exe -Command "(Invoke-WebRequest "https://api.github.com/repos/EssentialsX/Essentials/releases" | ConvertFrom-Json)[0].tag_name"') do set build=%%a
set downloadurl=https://github.com/EssentialsX/Essentials/releases/download/%build%/EssentialsX-%build%.0.jar
set downloadpath=C:\DankServerBuilder\plugins\EssentialsX-%build%.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading Plugin [EssentialsXChat]... "
set downloadurl=https://github.com/EssentialsX/Essentials/releases/download/%build%/EssentialsXChat-%build%.0.jar
set downloadpath=C:\DankServerBuilder\plugins\EssentialsXChat-%build%.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading Plugin [EssentialsXSpawn]... "
set downloadurl=https://github.com/EssentialsX/Essentials/releases/download/%build%/EssentialsXSpawn-%build%.0.jar
set downloadpath=C:\DankServerBuilder\plugins\EssentialsXSpawn-%build%.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading Plugin [ProtocolLib]... "
set downloadurl=https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/artifact/target/ProtocolLib.jar
set downloadpath=C:\DankServerBuilder\plugins\ProtocolLib.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading Plugin [TAB]... "
for /f "delims=" %%a in ('powershell.exe -Command "(Invoke-WebRequest "https://api.github.com/repos/NEZNAMY/TAB/releases" | ConvertFrom-Json)[0].tag_name"') do set build=%%a
set downloadurl=https://github.com/NEZNAMY/TAB/releases/download/%build%/TAB-%build%.jar
set downloadpath=C:\DankServerBuilder\plugins\TAB-%build%.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading Plugin [BetterSleeping]... "
for /f "delims=" %%a in ('powershell.exe -Command "(Invoke-WebRequest "https://api.github.com/repos/Nuytemans-Dieter/BetterSleeping/releases" | ConvertFrom-Json)[0].tag_name"') do set build=%%a
set downloadurl=https://github.com/Nuytemans-Dieter/BetterSleeping/releases/download/%build%/BetterSleeping.jar
set downloadpath=C:\DankServerBuilder\plugins\BetterSleeping-%build%.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading Plugin [ActionHealth]... "
for /f "delims=" %%a in ('powershell.exe -Command "(Invoke-WebRequest "https://api.github.com/repos/zeshan321/ActionHealth/releases" | ConvertFrom-Json)[0].tag_name"') do set build=%%a
set downloadurl=https://github.com/zeshan321/ActionHealth/releases/download/%build%/ActionHealth.jar
set downloadpath=C:\DankServerBuilder\plugins\ActionHealth-%build%.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Cleaning Zips... "
del /f ngrok.zip >nul 2>nul
del /f DankServerBuilder.zip >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Opening ngrok.com... "
echo "Go to Authentication > Your Authtoken and click copy, then paste it here."
echo.
powershell.exe -Command "Start-Process https://dashboard.ngrok.com/auth/your-authtoken"
set /P auth=Ngrok AuthToken: 
echo.
ngrok.exe authtoken %auth%
echo.
echo "-----> AuthToken Saved!"

echo.
echo "-----> Creating configure_server.cmd... "
echo "-----> Run this script once only after you have run the server for the first time!"
(
    echo @echo off
    echo color 0a
    echo title Configure Minecraft Server
    echo echo "-----> Run this script only after you have run the server for the first time!"
    echo echo "-----> Configuring Server..."
    echo powershell.exe -Command "((Get-Content server.properties -Raw) -replace 'spawn-protection=16','spawn-protection=0') | Set-Content server.properties"
    echo powershell.exe -Command "((Get-Content server.properties -Raw) -replace 'max-players=20','max-players=69') | Set-Content server.properties"
    echo powershell.exe -Command "((Get-Content server.properties -Raw) -replace 'motd=A Minecraft Server','motd=\u00A7a---\u00A76>\u00A7b\u00A7l %name% \u00A76<\u00A7a---') | Set-Content server.properties"
    if "%offline%" == "y" ( echo powershell.exe -Command "((Get-Content server.properties -Raw) -replace 'online-mode=true','online-mode=false') | Set-Content server.properties" )
    echo echo "-----> Done!"
    echo pause
) >configure_server.cmd
echo "-----> Done!"

echo.
echo "-----> Creating start_only_ngrok.cmd... "
(
    echo @echo off
    echo title Ngrok Tunnel
    echo ngrok tcp 25565
    echo pause
) >start_only_ngrok.cmd
echo "-----> Done!"

echo.
echo "-----> Creating start_only_server.cmd... "
(
    echo @echo off
    echo color 0a
    echo title Minecraft Server Console
    echo java -Xmx%ram%M -jar paper.jar -nogui
    echo pause
) >start_only_server.cmd
echo "-----> Done!"

echo.
echo "-----> Creating start_server_and_ngrok.cmd... "
(
    echo @echo off
    echo color 0a
    echo title Minecraft Server Console
    echo start start_only_ngrok.cmd
    echo java -Xmx%ram%M -jar paper.jar -nogui
    echo pause
) >start_server_and_ngrok.cmd
echo "-----> Done!"

echo.
echo "-----> Accepting Minecraft EULA... "
::powershell.exe -Command "((Get-Content eula.txt -Raw) -replace 'false','true') | Set-Content eula.txt"
(
    echo eula=true
) >eula.txt
echo "-----> Done!"

echo.
echo "============< Server Creation Complete >============"
echo.
echo "               /-/                \-\               "
echo "             -- /                  \ --             "
echo "            /  /                    \  \            "
echo "        \  /  --\                  \--  \  /        "
echo "        |\-      --   |---\      --      -/|        "
echo "        \ -      /-  /     ----  \       - /        "
echo "        --      -   /         |   -      --         "
echo "         -      /   | +    +  /   \      -          "
echo "       -/      |   /-        |     |      \-        "
echo "      /        /     \-      /  /  \        \       "
echo "     /        /   -\   \    | /-    \        \      "
echo "   -/        /      --\      /       \        \-    "
echo "  /         |          --  /-         |         \   "
echo "  |         /           | -           \         |   "
echo "  \      --|            | |            |--      /   "
echo "   | ---/               | |               \--- |    "
echo "   |/                   | |                   \|    "
echo "   ________.__      ________                 __     "
echo "  /   _____|________\______ \ _____    ____ |  | __ "
echo "  \_____  \|  \_  __ |    |  \\__  \  /    \|  |/ / "
echo "  /        |  ||  | \|    `   \/ __ \|   |  |    <  "
echo " /_______  |__||__| /_______  (____  |___|  |__|_ \ "
echo "         \/                 \/     \/     \/     \/ "
echo.
color 09
color 0b
color 0c
color 0d
color 0e
color 0a
color 09
color 0b
color 0c
color 0d
color 0e
color 0a
color 09
color 0b
color 0c
color 0d
color 0e
color 0a
echo.
echo " :::::::::  ::::::::::     :::     :::::::::       ::::    ::::  :::::::::: "
echo " :+:    :+: :+:          :+: :+:   :+:    :+:      +:+:+: :+:+:+ :+:        "
echo " +:+    +:+ +:+         +:+   +:+  +:+    +:+      +:+ +:+:+ +:+ +:+        "
echo " +#++:++#:  +#++:++#   +#++:++#++: +#+    +:+      +#+  +:+  +#+ +#++:++#   "
echo " +#+    +#+ +#+        +#+     +#+ +#+    +#+      +#+       +#+ +#+        "
echo " #+#    #+# #+#        #+#     #+# #+#    #+#      #+#       #+# #+#        "
echo " ###    ### ########## ###     ### #########       ###       ### ########## "
echo.
echo To start your server, run start_server_and_ngrok.cmd
echo.
echo Your servers IP is shown in the ngrok window, it looks something like this
echo "-----> 0.tcp.ngrok.io:00000 < last 5 digits will be random"
echo.
echo Run configure_server.cmd after you have run your server for the first time!

echo timeout /t 10 /nobreak > NUL
powershell.exe -Command "Start-Process https://allmylinks.com/sir-dankenstein"

echo.
pause
