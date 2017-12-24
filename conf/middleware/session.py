


import time
import random
import json
import base64
from conf import setting


def randomkey():
    s = ''.join([chr(random.randrange(123)) for i in range(5)])
    s = s + str(time.time())
    s = base64.urlsafe_b64encode(s.encode('utf-8'))
    s = s.decode('utf-8').strip('=')
    return s




class BaseSession(object):

    def __init__(self,request):

        self.request = request
        self.cache = {}
        # self.SESSION_COOKIE_KEY =setting.SESSION_COOKIE_KEY
        if request.cookies.get(setting.SESSION_COOKIE_KEY,None):

            self.session_key = request.cookies[setting.SESSION_COOKIE_KEY]
        else:
            self.session_key = randomkey()
        self.modified = False
        pass

    def get_session(self):
        dic = self.load()
        return dic
    _session = property(get_session)

    def __getitem__(self, item):
        return self._session.get(item)

    def __setitem__(self, key, value):
        self.modified = True
        self._session[key] = value

    def load(self):
        raise NotImplemented('子类必须实现')

class CookieSession(BaseSession):

    def load(self):
        '''从cookie取得'''
        if self.cache:
            return self.cache
        else:
            pass

class CacheSession(BaseSession):
    '''GLOBAL_SESSION_DIC={
    {'asdasdasasc21321asd':{'value':{},expire:'500'}}
    }'''

    def load(self):
        '''从内存中取得'''
        if self.cache:
            return self.cache
        else:
            d = setting.GLOBAL_SESSION_DICT.get(self.session_key)
            if d:
                self.cache = json.loads(d['value'])
                return self.cache
            else:
                # raise AttributeError('没有这个key')
                return self.cache
import os
class SessionFactory(object):

    def create_session(self,engine,request):
        if engine['backend'].lower() == 'cache':
            session = CacheSession(request)
            return session

        elif engine['backend'].lower() == 'cookie':
            session = CookieSession(request)
            return session













