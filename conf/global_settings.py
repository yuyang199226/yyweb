


MIDDLEWARE=[
    'conf.middleware.commonmiddle.CommonMiddle',

    'conf.middleware.commonmiddle.Md2',
    'conf.middleware.commonmiddle.Md3',
]
HOST_NAME = 'yuyang'

# SESSIONE_ENGINE = {'backend':'cache',
#                    'options':{
#                        'host':'127.0.0.1',
#                        'port':6379,
#                    }}

SESSIONE_ENGINE = {'backend':'cache',
}




SESSION_COOKIE_KEY = 'sessionid'
GLOBAL_SESSION_DICT = {}

