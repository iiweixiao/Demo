import collections
print("Regular dictionary")
d={}
d['a']='A'
d['d']='B'
d['c']='C'
d['1'] = '1'
print(d)
for k,v in d.items():
    print (k,v)#这个每次运行，print的结果都不一样
print("\nOrder dictionary")
d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['d'] = 'D'
d1['c'] = 'C'
d1['2'] = '2'
d1['1'] = '1'
for k,v in d1.items():
    print(k,v)#无论运行多少次，print的结果唯一
    #a A
    # b B
    # c C
    # 2 2
    # 1 1