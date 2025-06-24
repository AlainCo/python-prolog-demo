
# must import PyswipUtil before pyswip because it sets environment variables for pyinstaller packages
from prolog import PyswipUtil
from pyswip import Prolog

try:
    pyswip_util=PyswipUtil() 
    prolog = Prolog()
    #prolog.consult(relative_to="src",path="prolog/family.pl")
    #prolog.consult(relative_to="src/prolog",path="family.pl")
    #prolog.consult(path="src/prolog/family.pl")
    pyswip_util.consult(prolog,"family.pl") 
    
    prolog.assertz("father(michael,john)")
    print(list(prolog.query("father(michael,X)")))
    
    #pyswip_util.consult(prolog,"familywith'quote'.pl") # test quote escape # still a bug in pyswip consult with quote
    #prolog.consult(relative_to="src",path="prolog/familywith'quote'.pl")
    #print(list(prolog.query("fatherquote(michael,X)")))
except Exception as e:
    print(f"Exception: {e}")