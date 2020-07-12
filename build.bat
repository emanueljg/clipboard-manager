@echo off

set "pth=clipboard-manager-program\cbman"

call venv\Scripts\activate.bat

call pyinstaller cbman.py ^
    --distpath %pth% ^
    --onefile ^
    --icon keyboard.ico

call pyinstaller cbman_listener.py ^
    --distpath %pth% ^
    --onefile ^
    --icon keyboard.ico ^
    --noconsole

copy config.yaml %pth%\config.yaml /Y
