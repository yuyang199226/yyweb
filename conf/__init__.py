import importlib
from . import global_settings
import settings
class SettingConf(object):
    def __init__(self):
        for i in dir(global_settings):
            if i.isupper():
                setattr(self, i, getattr(global_settings, i))
        for i in dir(settings):
            if i.isupper():
                setattr(self, i,getattr(settings, i))
    def __getitem__(self, item):
        return getattr(self,item)
    def __getattr__(self, item):
        return None
setting = SettingConf()

MIDDLE_LIST= []
for i in range(len(setting['MIDDLEWARE'])-1, -1, -1):
    module_str, cls_str = setting['MIDDLEWARE'][i].rsplit('.',1)
    module = importlib.import_module(module_str)
    cls = getattr(module, cls_str)
    if i == len(setting['MIDDLEWARE'])-1:
        md = cls('func')
        LAST_MIDDLEMARE = md
        MIDDLE_LIST.append(md)
    else:
        md = cls(MIDDLE_LIST.pop())
        MIDDLE_LIST.append(md)

# for i in setting['MIDDLEWARE']:
#     module_str, cls_str = i.rsplit('.',1)
#     module = importlib.import_module(module_str)
#     cls = getattr(module, cls_str)
#     MIDDLE_LIST.append(cls)

# print(LAST_MIDDLEMARE)


