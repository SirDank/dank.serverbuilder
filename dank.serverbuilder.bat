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
set /P minecraft_version=Minecraft Paper Version: 
set /P ram=RAM in MB: 
md C:\DankServerBuilder
cd C:\DankServerBuilder
explorer.exe C:\DankServerBuilder

echo.
echo "-----> Downloading Paper %minecraft_version%... "
for /f "delims=" %%a in ('powershell.exe -Command "Invoke-WebRequest https://papermc.io/api/v2/projects/paper/versions/$env:minecraft_version | ConvertFrom-Json | Select -expand builds"') do set build=%%a
curl -o C:\DankServerBuilder\paper.jar -s -L https://papermc.io/api/v2/projects/paper/versions/%minecraft_version%/builds/%build%/downloads/paper-%minecraft_version%-%build%.jar
curl -o C:\DankServerBuilder\server-icon.png -s -L "https://www.dropbox.com/s/pmyapxkwoqxjgm6/server-icon.png?dl=1"
echo "-----> Done!"

echo.
echo "-----> Downloading Ngrok... "
curl -o C:\DankServerBuilder\ngrok.zip -s -L "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip"
echo "-----> Done!"

echo.
echo "-----> Unzipping Ngrok... "
powershell.exe -Command "Expand-Archive -Force -Path ngrok.zip -DestinationPath C:\DankServerBuilder"
echo "-----> Done!"

echo.
echo "-----> Starting Paper.jar... "
start paper.jar
echo "-----> Done!"

echo.
echo "-----> Downloading EssentialsX... "
curl -o C:\DankServerBuilder\jars.zip -s -L "https://ci.ender.zone/job/EssentialsX/lastSuccessfulBuild/artifact/jars/*zip*/jars.zip"
echo "-----> Done!"

echo.
echo "-----> Unzipping EssentialsX... "
powershell.exe -Command "Expand-Archive -Force -Path jars.zip -DestinationPath C:\DankServerBuilder"
echo timeout /t 3 /nobreak > NUL
ren jars plugins
echo "-----> Done!"

echo.
echo "-----> Cleaning Zips... "
del /f ngrok.zip
del /f jars.zip
echo "-----> Done!"

echo.
echo "-----> Downloading ProtocolLib... "
curl -o C:\DankServerBuilder\plugins\ProtocolLib.jar -s -L "https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/artifact/target/ProtocolLib.jar"
echo "-----> Done!"

echo.
echo "-----> Downloading ClearLagg... "
curl -o C:\DankServerBuilder\plugins\Clearlagg.jar -s -L "https://dev.bukkit.org/projects/clearlagg/files/latest"
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
echo "-----> Creating ngrok.bat... "
(
    echo @echo off
    echo ngrok tcp 25565
    echo pause
) >ngrok.bat
echo "-----> Done!"

echo.
echo "-----> Creating start.bat... "
(
    echo @echo off
    echo color 0a
	echo start ngrok.bat
    echo java -Xms%ram%M -Xmx%ram%M -jar paper.jar -nogui
    echo pause
) >start.bat
echo "-----> Done!"

echo.
echo "-----> Accepting Minecraft EULA... "
powershell.exe -Command "((Get-Content eula.txt -Raw) -replace 'false','true') | Set-Content eula.txt"
echo "-----> Done!"

echo.
echo "==========< Configuration Complete >=========="
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
echo To start your server, run start.bat
echo Your servers IP is shown in the ngrok window, it looks something like this
echo "-----> 0.tcp.ngrok.io:00000 < last 5 digits will be random"
echo timeout /t 5 /nobreak > NUL
powershell.exe -Command "Start-Process https://allmylinks.com/sir-dankenstein"

echo.
pause
