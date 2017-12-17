from conf.middleware.basemiddleware import MiddleWareMin

class MD4(MiddleWareMin):
    def process_request(self,request):
        print('md4')
    def process_response(self,request,response):
        print('md4 response')
        return response