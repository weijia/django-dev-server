@echo off
SETLOCAL
set script_path=%~d0%~p0
echo %script_path%
rem set /p id="Enter ID: "
start cmd /k "cd %script_path%"