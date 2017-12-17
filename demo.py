import yyweb
from yyweb import HTTP_Response, render


@yyweb.router('/index')
def index(request):
    return render(request, 'index.html')

@yyweb.router('/login')
def login(request):
    if request.method == 'GET':
        ls = ['北京', '上海', '武汉', '济南', '青岛']
        dic = {'name':'wangsha'}
        return render(request, 'login.html', {'username':'yuyang', 'ls':ls,'dic':dic})
    elif request.method == 'POST':
        print(request.form_data)
        print(request.body)
        return HTTP_Response('ok')

@yyweb.router('/home')
def home(request):
    # return HTTP_Response('222222')
    response = render(request, 'blog/home.html')
    print(request.cookies)
    response.set_cookie('guy', 'nice')
    response.set_signed_cookie('auth', 'yuyang', 'asd')
    return response

if __name__ ==  '__main__':
    yyweb.start()