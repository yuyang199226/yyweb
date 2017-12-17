import yyweb
from yyweb import HTTP_Response,render


@yyweb.router('/index')
def index(request):
    print(request.method)
    a = render(request, 'index.html')
    print(type(a))
    print(a.status)
    return a

@yyweb.router('/login')
def login(request):
    print(request.path_info)
    return HTTP_Response('111111')

@yyweb.router('/home')
def home(request):
    # return HTTP_Response('222222')
    return render(request, 'blog/home.html')

if __name__ ==  '__main__':
    yyweb.start()