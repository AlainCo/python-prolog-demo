
# must import PyswiplUtil before pyswip because it sets environment variables for pyinstaller packages
from prolog import PyswiplUtil
from pyswip import Prolog

pyswip_util=PyswiplUtil() 
prolog = Prolog()
pyswip_util.consult(prolog,'family.pl') # pyswip prolog.consult has a bug on Windows with \ in path

prolog.assertz("father(michael,john)")
print(list(prolog.query("father(michael,X)")))
