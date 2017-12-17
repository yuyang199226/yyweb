
from . import basemiddleware
class CommonMiddle(basemiddleware.MiddleWareMin):
    def process_request(self,request):
        print('common request')
    def process_response(self,request,response):
        print('common response')
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