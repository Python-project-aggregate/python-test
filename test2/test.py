a = 'adsf'
b ='adsfde'

source = {j: {i:1 for i in a} for j in b}
# print(record)
# target = {}
def flatmap(src, dest=None,prefix=''):
    if dest == None:
        dest = {}


    for k, v in src.items():
        if isinstance(v, dict):
            flatmap(v, dest, prefix = prefix+ k +'.')
        else:
            dest[prefix+k] =v
    # _faltmap(src)
    return dest
print(flatmap(source))