import yyweb
from yyweb import HTTP_Response,render


@yyweb.router('/index')
def index(request):
    print(request.method)
    return render(request,'index.html')

@yyweb.router('/login')
def login(request):
    print(request.path_info)
    return render(request, 'login.html')

@yyweb.router('/home')
def home(request):
    return render(request, 'blog/home.html')

if __name__ ==  '__main__':
    yyweb.start()