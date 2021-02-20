@echo off
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
set /P minecraft_version=Minecraft Paper Version: 
set /P ram=RAM in MB: 
set /P online=Allow Cracked Players [ y / n ]: 
if "%online%" == "y" ( echo "-----> Run configure_server.bat only after you have run the server for the first time!" )
md C:\DankServerBuilder
cd C:\DankServerBuilder
explorer.exe C:\DankServerBuilder

echo.
echo "-----> Downloading Paper %minecraft_version%... "
for /f "delims=" %%a in ('powershell.exe -Command "Invoke-WebRequest https://papermc.io/api/v2/projects/paper/versions/$env:minecraft_version | ConvertFrom-Json | Select -expand builds"') do set build=%%a
set downloadurl=https://www.dropbox.com/s/pmyapxkwoqxjgm6/server-icon.png?dl=1
set downloadpath=C:\DankServerBuilder\server-icon.png
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
set downloadurl=https://papermc.io/api/v2/projects/paper/versions/%minecraft_version%/builds/%build%/downloads/paper-%minecraft_version%-%build%.jar
set downloadpath=C:\DankServerBuilder\paper.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Starting Paper.jar... "
echo timeout /t 5 /nobreak > NUL
start paper.jar
echo "-----> Done!"

echo.
echo "-----> Downloading Ngrok... "
set downloadurl=https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip
set downloadpath=C:\DankServerBuilder\ngrok.zip
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Unzipping Ngrok... "
powershell.exe -Command "Expand-Archive -Force -Path ngrok.zip -DestinationPath C:\DankServerBuilder" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Downloading EssentialsX... "
curl -o C:\DankServerBuilder\jars.zip -s -L "https://ci.ender.zone/job/EssentialsX/lastSuccessfulBuild/artifact/jars/*zip*/jars.zip" >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Unzipping EssentialsX... "
powershell.exe -Command "Expand-Archive -Force -Path jars.zip -DestinationPath C:\DankServerBuilder" >nul 2>nul
echo timeout /t 3 /nobreak > NUL
ren jars plugins >nul 2>nul
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
echo timeout /t 3 /nobreak > NUL
echo "-----> Done!"

echo.
echo "-----> Cleaning Zips... "
del /f ngrok.zip >nul 2>nul
del /f jars.zip >nul 2>nul
del /f DankServerBuilder.zip >nul 2>nul
echo "-----> Done!"

echo.
echo "-----> Delete the following manually: EssentialsXAntiBuild, EssentialsXGeoIP, EssentialsXXMPP"
explorer.exe C:\DankServerBuilder\plugins
set /P deletion=Hit [Enter] if you have done this!

echo.
echo "-----> Downloading ProtocolLib... "
set downloadurl=https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/artifact/target/ProtocolLib.jar
set downloadpath=C:\DankServerBuilder\plugins\ProtocolLib.jar
powershell.exe -Command "Start-BitsTransfer -Source '%downloadurl%' -Destination '%downloadpath%' -TransferType Download" >nul 2>nul
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
echo "-----> Saved!"

echo.
echo "-----> Creating start_only_ngrok.bat... "
(
    echo @echo off
    echo ngrok tcp 25565
    echo pause
) >start_only_ngrok.bat
echo "-----> Done!"

echo.
echo "-----> Creating start_only_server.bat... "
(
    echo @echo off
    echo color 0a
    echo java -Xms%ram%M -Xmx%ram%M -jar paper.jar -nogui
    echo pause
) >start_only_server.bat
echo "-----> Done!"

echo.
echo "-----> Creating configure_server.bat... "
echo "-----> Run this script only after you have run the server for the first time!"
(
    echo @echo off
    echo color 0a
    echo echo "-----> Run this script only after you have run the server for the first time!"
    echo echo "-----> Configuring Server..."
    echo powershell.exe -Command "((Get-Content server.properties -Raw) -replace 'spawn-protection=16','spawn-protection=0') | Set-Content server.properties"
    echo powershell.exe -Command "((Get-Content server.properties -Raw) -replace 'max-players=20','max-players=69') | Set-Content server.properties"
    echo powershell.exe -Command "((Get-Content server.properties -Raw) -replace 'motd=A Minecraft Server','motd=\u00A7a---\u00A76>\u00A7b\u00A7l %name% \u00A76<\u00A7a---') | Set-Content server.properties"
    if "%online%" == "y" ( echo powershell.exe -Command "((Get-Content server.properties -Raw) -replace 'online-mode=true','online-mode=false') | Set-Content server.properties" )
    echo echo "-----> Done!"
    echo pause
) >configure_server.bat
echo "-----> Done!"

echo.
echo "-----> Creating start_server_and_ngrok.bat... "
(
    echo @echo off
    echo color 0a
    echo start start_only_ngrok.bat
    echo java -Xms%ram%M -Xmx%ram%M -jar paper.jar -nogui
    echo pause
) >start_server_and_ngrok.bat
echo "-----> Done!"

echo.
echo "-----> Accepting Minecraft EULA... "
powershell.exe -Command "((Get-Content eula.txt -Raw) -replace 'false','true') | Set-Content eula.txt"
echo "-----> Done!"

echo.
echo "==========< Server Building Complete >=========="
echo.
echo To start your server, run start_server_and_ngrok.bat
echo.
echo Your servers IP is shown in the ngrok window, it looks something like this
echo "-----> 0.tcp.ngrok.io:00000 < last 5 digits will be random"
echo.
echo Run configure_server.bat after you have run your server for the first time
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
echo timeout /t 10 /nobreak > NUL
powershell.exe -Command "Start-Process https://allmylinks.com/sir-dankenstein"

echo.
pause
