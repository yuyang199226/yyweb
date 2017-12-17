import yyweb
from yyweb import HTTP_Response


@yyweb.router('/index')
def index(request):
    print(request.method)
    return 'hello SB'

@yyweb.router('/login')
def login(request):
    print(request.path_info)
    return HTTP_Response('hello login')


if __name__ ==  '__main__':
    yyweb.start()