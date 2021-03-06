import bottle
import urllib
import os
import time
import re
import json
from http.cookies import SimpleCookie
from  jinja2 import Template
from wsgiref.simple_server import make_server
from conf import setting, LAST_MIDDLEMARE, md
from utils.snippets import make_bytes, make_str,signed_cookie,handle_cookies,parse_form_data
# import conf
# BASE_DIR = ''
URL_PATTERNS = []



def render_function(html,context):
    if not context:
        return make_bytes(html)
    template = Template(html)
    try:
        rendered_html = template.render(context)
        return make_bytes(rendered_html)
    except Exception as e:
        raise 'you should pass key word arguments or dict'
    

class Request(object):
    '''Request 对象
    '''
    def __init__(self, environ):
        self.environ = environ
        # environ_cp = copy.deepcopy(environ)
        self.path_info = environ.get('PATH_INFO')
        self.method = environ.get('REQUEST_METHOD')
        self._cookies = environ.get('HTTP_COOKIE')
        self.query_params = environ.get('QUERY_STRING')
        self.url_kwargs = {}

        try:
            request_body_size = int(self.environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        request_body = self.environ['wsgi.input'].read(request_body_size)
        self._body = request_body
    
    @property
    def cookies(self):
        return handle_cookies(self._cookies)
    
    @property
    def form_data(self):
        
        if self.method == 'POST':
            return parse_form_data(self._body)
        else:
            return self._body
    
    @property
    def body(self):
        return self._body

def render(request,template_path, context=None):
    '''render a html file
    '''
    if not template_path:
        raise 'must have a tempate path'

    try:
        f = open(template_path, 'r', encoding='utf-8')
        html_body = f.read()
        f.close()
        html_body = render_function(html_body, context)
        response = HTTP_Response(html_body, render=True)
        return response
    except FileNotFoundError as e:

        html_path = os.path.join('templates', template_path)
        try:
            f = open(html_path, 'r', encoding='utf-8')
            html_body = f.read()
            f.close()
            html_body = render_function(html_body, context)
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
        self.headers = {}
        self._cookies = None
        if self.render:
            self.content_type = 'text/html; charset=utf-8'
        self.headers['Content-type'] =  self.content_type

    def set_cookie(self, key, value, **options):
        '''设置cookie'''
        if not self._cookies:
            self._cookies = SimpleCookie()
        if len(value) > 4096: raise ValueError('Cookie value to long.')
        self._cookies[key] = value

        for k, value in options.items():
            # if k == 'max_age':
            #     if isinstance(value, timedelta):
            #         value = value.seconds + value.days * 24 * 3600
            if k == 'expires':
                if isinstance(value, (int, float)):
                    value = time.time()+value
                    value = time.gmtime(value)
                value = time.strftime("%a, %d %b %Y %H:%M:%S GMT", value)
            self._cookies[key][k.replace('_', '-')] = value
    def set_signed_cookie(self, key, value, salt, path='/', expires=None):
        self._cookies[key] = signed_cookie(value, salt)
 

class Myapp01(object):

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, environ, start_response):
        request = Request(environ)
        url = self.path_info = environ.get('PATH_INFO')
        url_flag = False
        for i in URL_PATTERNS:
            match_obj = re.search(i[0], url)
            if match_obj:
                url_flag = True
                break    
            else:
                continue
        if url_flag:
            LAST_MIDDLEMARE.get_response = i[1]
            if match_obj.groupdict():
                request.url_kwargs = match_obj.groupdict()
            response = md(request)
            status = response.status
            headers = [(str(k), str(v)) for k, v in response.headers.items()]
            # res_cookie = response._cookies.output(header='')
            for c in response._cookies.values():
                headers.append((str('Set-Cookie'), str(c.output(header=''))))
            # headers.append(
            #     (str('Set-Cookie'), str(res_cookie))
            # )
            start_response(status, headers)
            return [response.body]
        else:
            status = '404 not found'
            headers = [('Content-type', 'text/plain; charset=utf-8')]
            if setting.DEBUG == True:
                ret = make_bytes(json.dumps([t[0] for t in URL_PATTERNS]))
            else:
                ret = bytes('当前访问的url不存在', encoding='utf-8')
            start_response(status, headers)
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
    server = make_server(host, port, app01)
    if setting.DEBUG == True:
        style = 'debug'
    else:
        style = 'produce'
    print('IP:%s --- 端口:%s --- 模式:%s'%(host, port, style))
    server.serve_forever()
if __name__ == '__main__':
    start()
