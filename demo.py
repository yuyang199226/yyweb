import yyweb
from yyweb import HTTP_Response, render


@yyweb.router('/index')
def index(request):
    return render(request, 'index.html')

@yyweb.router('/login')
def login(request):
    ls = ['北京', '上海', '武汉', '济南', '青岛']
    dic = {'name':'wangsha'}
    return render(request, 'login.html', {'username':'yuyang', 'ls':ls,'dic':dic})

@yyweb.router('/home')
def home(request):
    # return HTTP_Response('222222')
    return render(request, 'blog/home.html')

if __name__ ==  '__main__':
    yyweb.start()