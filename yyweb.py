

import os
import re
import json
from wsgiref.simple_server import make_server
from conf import setting, LAST_MIDDLEMARE, md
# import conf
# BASE_DIR = ''
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

def render(request,template_path):
    '''render a html file
    '''
    if not template_path:
        raise 'must have a tempate path'

    try:
        f = open(template_path, 'rb')
        html_body = f.read()
        f.close()
        response = HTTP_Response(html_body, render=True)
        return response
    except FileNotFoundError as e:

        html_path = os.path.join('templates', template_path)
        try:
            f = open(html_path, 'rb')
            html_body = f.read()
            f.close()
            response = HTTP_Response(html_body, render=True)
            return response
            
        except FileNotFoundError as e:
            raise 'file not found,check the path,be sure your path is correct'


class HTTP_Response(object):
    def __init__(self, content=b'', status='200 OK', content_type='text/plain', render=False, **kwargs):
        if isinstance(content, bytes):
            self.body = content
        else:
            str_content = json.dumps(content)
            b_content = bytes(str_content, encoding='utf-8')
            self.body = b_content

        self.status = status
        self.render = render
        self.content_type = content_type
        self.headers = []
        if self.render:
            self.content_type = 'text/html; charset=utf-8'
        self.headers.append(('Content-type', self.content_type))





class Myapp01(object):
    def __init__(self, *args, **kwargs):
        pass 

    def __call__(self, environ, start_response):
        request = Request(environ)
        url = self.path_info = environ.get('PATH_INFO')
        url_flag = False
        for i in URL_PATTERNS:
            if re.search(i[0], url):
                url_flag = True
                break    
            else:
                continue
        if url_flag:
            LAST_MIDDLEMARE.get_response = i[1]
            response = md(request)
            response = i[1](request)
            status = response.status
            headers = response.headers
            start_response(status, headers)
            return [response.body]
        else:
            status = '404 not found'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            ret = bytes('当前访问的url不存在',encoding='utf-8')
            return [ret]

        
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
