
import hmac
import base64



def make_bytes(string, encoding='utf-8'):
    return bytes(string, encoding=encoding)

def make_str(byte, encoding='utf-8'):
    return str(byte, encoding=encoding)

def signed_cookie(msg, salt):
    hmac_new = hmac.new(make_bytes(salt), make_bytes(msg))
    hmac_msg = hmac_new.digest()
    b64 = base64.b64encode(hmac_msg)
    value = '%s|%s' %(msg, make_str(b64))
    return value

def handle_cookies(cookies=None):
    dic={}
    if cookies  == None:
        return dic
    ls = cookies.split(';')
    for i in ls:
        key, value = i.split('=')
        dic[key.strip()] = value.strip()
    return dic

def parse_form_data(data):
    data = make_str(data)
    dic={}
    ls = data.split('&')
    for i in ls:
        key, value = i.split('=')
        dic[key] = value
    return dic


