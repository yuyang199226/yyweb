from . import basemiddleware
from conf import setting
from  . import session
import os
import json


class SessionMiddleware(basemiddleware.MiddleWareMin):

    def process_request(self,request):
        session_instance = session.SessionFactory().create_session(setting.SESSIONE_ENGINE,request)
        request.session = session_instance

    def process_response(self,request,response):


        request.session.modified = True



        if request.session.modified == True:
            setting.GLOBAL_SESSION_DICT[request.session.session_key]= {
                'value':json.dumps(request.session.cache),
                # 'expire':request.session.get_expire()
            }
            response.set_cookie(setting.SESSION_COOKIE_KEY, request.session.session_key)
        print('session-response')
        return response

