# a = 'adsf'
# b ='adsfde'
#
# source = {j: {i:1 for i in a} for j in b}
# # print(record)
# # target = {}
# def flatmap(src, dest=None,prefix=''):
#     if dest == None:
#         dest = {}
#     for k, v in src.items():
#         if isinstance(v, dict):
#             flatmap(v, dest, prefix = prefix+ k +'.')
#         else:
#             dest[prefix+k] =v
#     # _faltmap(src)
#     return dest
# print(flatmap(source))
def com(s1,s2):
    final=['']
    #比较两个字符串哪个较短
    little = s2 if len(s1)>len(s2) else s1
    temp= s2 if little ==s1 else s1
    #根据较短的比较
    for j in range(len(little ),0,-1):
        i=0
        while len(little )>j:
            n=little [i:j+1]
            if n in temp:
                if len(n)>len(final[0]):
                    final.clear()
                    final=['']
                    final[0]=n
                elif len(n)==len(final[0]) and n not in final:
                    final.append(n)
            i+=1
            j+=1
        #较长的在final里面了
        if len(final[0]):
            break
    print(final)
s1='jjs'
s2='jjs'
com(s1,s2)
