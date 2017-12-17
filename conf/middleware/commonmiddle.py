
from . import basemiddleware
class CommonMiddle(basemiddleware.MiddleWareMin):
    def process_request(self,request):
        print('common request')
    def process_response(self,request,response):
        if response._cookies:
            cookie_str = ''
            for k,v in response._cookies.items():
                tmp = '%s=%s; ' %(k, v)
                cookie_str+=tmp
            response.headers['Set-Cookie'] = cookie_str[0:len(cookie_str)-3]
        return response
    
class Md2(basemiddleware.MiddleWareMin):
    def process_request(self,request):
        print('md2')
    def process_response(self,request,response):
        print('md2common response')
        return response

class Md3(basemiddleware.MiddleWareMin):
    def process_request(self,request):
        print('md3')
    def process_response(self,request,response):
        print('md3 response')
        return response