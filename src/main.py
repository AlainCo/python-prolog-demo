
import sys
import os

# set SWI Prolog environment before importing pyswip
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.environ['SWI_HOME_DIR'] = os.path.join(sys._MEIPASS,'swipl')
    os.environ['LIBSWIPL_PATH'] = os.path.join(sys._MEIPASS,'swipl/bin/libswipl.dll') #not required
from pyswip import Prolog

#just a test
prolog = Prolog()
prolog.assertz("father(michael,john)")
print(list(prolog.query("father(michael,X)")))