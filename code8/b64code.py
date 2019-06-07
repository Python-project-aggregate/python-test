a = b'ABCDEFGHIJKLMNOPQESTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
import base64

src = 'abcd'

def base64encode(src:str)->bytes:
    ret = bytearray()
    # bytearray = ()
    if isinstance(src, str):
        _src = src.encode()
    else:
        return
    length = len(_src)

    for offset in range(0, length, 3):
        triple = _src[offset:offset+3]
        print(triple)
        r = 3 - len(triple)
        if r:
            triple += b'\x00' * r
        b = int.from_bytes(triple, 'big')
        for i in range(18, -1, -6):
            index = b >> i if i == 18 else b >> i & 0x3F
            ret.append(a[index])
        if r:
            ret[-r:] = b'=' * r
    return bytes(ret)

def base64decode(base):
    d = {}
    base64 = ''
    strbase = ''
    base = base.decode()
    # print(base)
    for k,v in enumerate(a.decode()):
        # print(k,v)
        d.update({v:k})
    # print(d)
    for i in base:
        base64 += '0'*6 if i == '=' else '{:06b}'.format(d[i])
        # print(base64)
    for offset in range(0, len(base64), 8):
        print(base64)
        _str = base64[offset:offset+8]
        # print(chr(int(_str)))
        if '1' not in _str:
            break
        strbase += chr(int(_str,2))
        print(strbase)
        # print(_str)
    return strbase


if __name__ == '__main__':
    # print(base64encode(src))
    # print(base64.b64encode(b'abcd'))
    print(base64decode(b'QQ=='))