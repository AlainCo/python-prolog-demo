import sys
import os
from pathlib import Path

# set SWI Prolog environment before importing pyswip
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.environ['SWI_HOME_DIR'] = os.path.join(sys._MEIPASS,'swipl')
    os.environ['LIBSWIPL_PATH'] = os.path.join(sys._MEIPASS,'swipl/bin/libswipl.dll') #not required
    prolog_relative_to=Path(os.path.join(sys._MEIPASS,'src/prolog'))
else:
    prolog_relative_to=Path(__file__).expanduser().parent

from pyswip import Prolog

class PyswiplUtil:
    def __init__(self):
        pass
        
    def consult(self,prolog:Prolog,path,catcherrors: bool = False):
        """patch the pyswip consult method which dont manage backlash in windows path"""
        #prolog.consult(relative_to=prolog_relative_to,path=path,catcherrors=catcherrors)
        path = prolog_relative_to  / path
        next(prolog.query(str(path).replace('\\','\\\\').replace('\'','\\\'').join(["consult('", "')"]), catcherrors=catcherrors))