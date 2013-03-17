#from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.sql import text
from sqlalchemy.exc import DBAPIError
from .models import (DBSession, MyModel)
import logging

log = logging.getLogger(__name__)


@view_config(route_name='home', renderer='templates/homepage.html')
def homepage(request):
    return {'name': 'name'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_tutorial_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


@view_config(route_name='swanglish', renderer='templates/swanglish.html')
def swanglish(request):
    return {'name': 'name'}


@view_config(route_name='translate', renderer='json')
def translate(request):
    translate_word = request.POST['translate_word']
    translatedword = ""
    # try SiSwati disctinary
    translate_list = []
    translation_list = []
    sql = text('''select siswati_version, english_version from swanglish where siswati_version='%s' ''' % (translate_word))
    try:
        result = DBSession.execute(sql)
        for i in result:
            translate_list.append(i.siswati_version)
            translation_list.append(i.english_version)
            translatedword = i.english_version
            log.debug("translatedword %s" % (translatedword))
    except DBAPIError, e:
        log.debug("Error in query: %s " % e)
        return []
    # try English ditionary
    sql = text('''select english_version, siswati_version from swanglish where english_version='%s' ''' % (translate_word))
    try:
        result = DBSession.execute(sql)
        for i in result:
            translatedword = i.siswati_version
            translate_list.append(i.english_version)
            translation_list.append(i.siswati_version)
            log.debug("translatedword %s" % (translatedword))
    except DBAPIError, e:
        log.debug("Error in query: %s " % e)
        return []
    print "translate_list %s, translation_list %s" % (translate_list, translation_list)

    if len(translatedword) < 1:
        translatedword = translate_word
    else:
        translatedword = translatedword.replace("#", ",")
    return {"translatedword": translatedword, 'translate_list': translate_list, 'translation_list': translation_list}
