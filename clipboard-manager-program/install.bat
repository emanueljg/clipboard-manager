@echo off

set "basepath=%appdata%\cbman"
set "exepath=%basepath%\cbman_listener.exe"
set "linkpath=%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\cbman_listener.lnk"
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

xcopy /S /I /Y "cbman" "%basepath%"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%linkpath%" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%exepath%" >> %SCRIPT%
echo oLink.WorkingDirectory = "%basepath%" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%
del %SCRIPT%