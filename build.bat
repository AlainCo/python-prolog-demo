@echo off
call .venv\Scripts\activate
rem normally you should set SWI_HOME_DIR (install folder) and LIBSWIPL_PATH (libswipl dll)
if "%SWI_HOME_DIR%" == "" set SWI_HOME_DIR="C:\Program Files\swipl"
if "%LIBSWIPL_PATH%" =="" set LIBSWIPL_PATH=%SWI_HOME_DIR%\bin\libswipl.dll
if not exist "%LIBSWIPL_PATH%" goto onmissingswi

set NAME=python-prolog-demo

pyinstaller --console --onefile --clean --name %NAME% src\main.py --add-data "%LIBSWIPL_PATH%;swipl/bin/." --add-data "%SWI_HOME_DIR%;swipl"
call .venv\Scripts\deactivate
goto:eof

:onmissingswi
echo SWI Lib not valid : %LIBSWIPL_PATH%
pause
goto:eof