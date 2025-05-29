
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
[{'X': 'dan'}, {'X': 'lucy'}, {'X': 'john'}]
```

## run packaged version
```
dist\python-prolog-demo.exe
```
it should produce same result:
```json
[{'X': 'dan'}, {'X': 'lucy'}, {'X': 'john'}]
```

# Developer's info

## bug in consult on windows
I've found a bug with prolog.consult() on Windose. The backslash of windows paths are considered as escape by prolog. no way to change that as the path is built by pyswip using Path.

The `PyswiplUtil.consult()` does nearly the same, but escaping the backslash... I've posted a message on pyswip googlegroup...
Also it does all relative to the prolog folder, and the folder 

## initialization of SWI Prolog...
ther is a problem to initialize SWI Prolog when using pyinstaller... you need to package the installation folder of SWI Prolog, and adjuste some environment variables with pyinstaller informations...

now it is done in prolog/init_pyswipl.py module . you have to import it before importing pyswip.

# TODO:
* Find things to do

# Disclaimer: 
* I'm an old programmer (Java, C/C++, and many scripting languages), but a rookie in Python and Prolog
* I'm lazy
* Tell me if something can be improved (easily)
* Don't hesitate to share use case.

# Credits: 
Thanks to Grok, Claude, Deepseek, and Le Chat Mistral, for the teaching.
