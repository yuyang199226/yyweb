
DEBUG = True
HOST_NAME= 'yyweb'


MIDDLEWARE=[
    'conf.middleware.commonmiddle.CommonMiddle',
    'conf.middleware.sessionmiddle.SessionMiddleware',
    'conf.middleware.commonmiddle.Md2',
    'conf.middleware.commonmiddle.Md3',
    'md.MD4'
]
DATABASE = [
    {'engine': 'MySQL',
        'options': {'name': 'blog',
        'password': '123',
        'HOST': '127.0.0.1',
        'PORT': '3306'}
    
    }
]