import yyweb
from yyweb import HTTP_Response,render


@yyweb.router('/index')
def index(request):
    return render(request, 'index.html')

@yyweb.router('/login')
def login(request):

    return HTTP_Response('111111')

@yyweb.router('/home')
def home(request):
    # return HTTP_Response('222222')
    return render(request, 'blog/home.html')

if __name__ ==  '__main__':
    yyweb.start()