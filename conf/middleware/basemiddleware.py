

class MiddleWareMin(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        if hasattr(self,'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self,'process_response'):
            response = self.process_response(request,response)
        return response