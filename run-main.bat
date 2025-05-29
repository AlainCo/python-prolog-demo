@echo off
cd /d %~dp0
set BASEDIR=%~dp0
for /f %%i in ( "%BASEDIR:~0,-1%" ) do set DIRNAME=%%~ni

%BASEDIR%dist\%DIRNAME%.exe 
