
# must import PyswipUtil before pyswip because it sets environment variables for pyinstaller packages
from prolog import PyswipUtil
from pyswip import Prolog

pyswip_util=PyswipUtil() 
prolog = Prolog()
pyswip_util.consult(prolog,"family.pl") # pyswip prolog.consult has a bug on Windows with \ in path


prolog.assertz("father(michael,john)")
print(list(prolog.query("father(michael,X)")))

pyswip_util.consult(prolog,"familywith'quote'.pl") # test quote escape
print(list(prolog.query("fatherquote(michael,X)")))
