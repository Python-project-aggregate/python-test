import imaplib

def plugin_load(pligin_name:str, sep=':'):

    m, _, c = pligin_name.partition(sep)
    mod = imaplib.import_module(m)



if __name__ == '__main__':
    mod = __import__('test1')
    cls = getattr(mod, 'A')
    cls().showme()
