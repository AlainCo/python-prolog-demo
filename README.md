
# Functionalities
## It's just a showcase 
it shows about how to package :
* using Swi Prolog 
* with `pyswip` 
* with `pyinstaller`
It was build and tested on windows.

# Build

* check that you have the required environment variable described in `pyswip` documentation. Here is the usual values for the 64 bit version installed the standard way:
    * SWI_HOME_DIR=c:\program files\swipl
    * LIBSWIPL_PATH=C:\Program Files\swipl\bin\libswipl.dll
* Create a virtual environment as usual
* install the requirements with `install_requirements.bat`
* build the packaged application with `build.bat`

# Usage

## run unpackaged

```
python src\main.py
```
it should produce:
```json
[{'X': 'john'}]
```

## run packaged version
```
dist\python-prolog-demo.exe
```
it should produce same result:
```json
[{'X': 'john'}]
```

# TODO:
* Find things to do

# Disclaimer: 
* I'm an old programmer (Java, C/C++, and many scripting languages), but a rookie in Python and Prolog
* I'm lazy
* Tell me if something can be improved (easily)
* Don't hesitate to share use case.

# Credits: 
Thanks to Grok for the teaching.
