@echo off
setlocal
call .venv\Scripts\activate
rem normally you should set SWI_HOME_DIR (install folder) and LIBSWIPL_PATH (libswipl dll)
if "%SWI_HOME_DIR%" == "" set SWI_HOME_DIR="C:\Program Files\swipl"
if "%LIBSWIPL_PATH%" =="" set LIBSWIPL_PATH=%SWI_HOME_DIR%\bin\libswipl.dll
if not exist "%LIBSWIPL_PATH%" goto onmissingswi
set BASEDIR=%~dp0
for /f %%i in ( "%BASEDIR:~0,-1%" ) do set DIRNAME=%%~ni
pyinstaller --console --onefile --clean --name %DIRNAME% src\main.py --add-data "%LIBSWIPL_PATH%;swipl/bin/." --add-data "%SWI_HOME_DIR%;swipl" --add-data "src/prolog/*.pl;prolog"
call .venv\Scripts\deactivate
endlocal
goto:eof

:onmissingswi
echo SWI Lib not valid : %LIBSWIPL_PATH%
endlocal
pause
goto:eof