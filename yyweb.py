

import json
from wsgiref.simple_server import make_server


URL_PATTERNS = []

class Request(object):
    '''Request 对象
    '''
    def __init__(self,environ):
        # environ_cp = copy.deepcopy(environ)
        self.path_info = environ.get('PATH_INFO')
        self.method = environ.get('REQUEST_METHOD')
        self.cookies = environ.get('HTTP_COOKIE')
        self.query_params = environ.get('QUERY_STRING')



class HTTP_Response(object):
    def __init__(self,content=b''):
        if isinstance(content, bytes):
            self.body = content
        else:
            str_content = json.dumps(content)
            b_content = bytes(str_content, encoding='utf-8')
            self.body = b_content




class Myapp01(object):
    def __init__(self, *args, **kwargs):
        pass 

    def __call__(self, environ, start_response):
        request = Request(environ)
        url = self.path_info = environ.get('PATH_INFO')
        print(url)
        for i in URL_PATTERNS:
            if url == i[0]:
                status = '200 OK'
                response = i[1](request)
                headers = [('Content-type', 'text/plain')]
                start_response(status, headers)
                return [response.body]
            else:
                continue

 ####################  路由   ###################
def router(url):
    def wrapper(func):
        URL_PATTERNS.append((url, func))
        return func
    return wrapper





def start(host='127.0.0.1', port=8090):
    '''启动服务器
    '''
    app01 = Myapp01()
    server = make_server('127.0.0.1', 8090, app01)
    print('运行于127.0.0.1，端口为8090')
    server.serve_forever()
if __name__ == '__main__':
    start()
