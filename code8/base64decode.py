s='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
def base(n,new='',st='',all=''):
    #去掉==
    for i in n:
        if i!='=':
            new+=i
    #补全位数
    for k in new:
        temp=s.index(k)
        b=bin(temp)[2:]
        st= st+(6-len(b))*'0'+b if len(b)!=6 else st+b
    #转换成base64时会补全6位，去掉多余的0
    if len(st)%8!=0:
        num=(len(st)//8)+1
        st=st+(num*8-len(st))*'0'
    # 转换成最终
    while len(st)!=0:
        final=st[:8]
        st=st[8:]
        if final=='00000000':
            continue
        delta=int(final,2)
        all+=chr(delta)
    print(all)
t1='TWFu'
t2='QQ=='
t3='QkM='
base(t1)
base(t2)
base(t3)
