### 切片
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;切片是通过索引区间访问线性结构的一段数据，xxx[ start : stop ]表示返回[ start , stop)区间的子序列，支持负索引，start可以省略，默认值为0 ; stop也可以省略，默认值为末尾，索引超过上界（右边界），就取到末尾;超过下界（左边界），取到开头。start一定要在stop的左边。  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ : ]表示从头至尾，全部元素被取出，等效于copy()方法  

##### 线性结构
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;线性结构是可迭代的，可以使用len()获取长度，能通过下标访问，可以被切片。  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;列表、元组、字符串、bytes、bytearray等都属于可迭代对象。

步长切片
>[ start : stop : step]  
&nbsp;&nbsp;&nbsp;step为步长，可以为正、负整数，默认值为1，step要和start : stop同向，否则返回空序列

切片赋值  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;切片操作写在等号左边，被插入可迭代对象写在等号右边，右边必须是可迭代对象。

### IPython使用
帮助  
* ？  
&nbsp;&nbsp;&nbsp;&nbsp;Ipython的概述和简介  
* help(name)  
&nbsp;&nbsp;&nbsp;&nbsp;查询指定名称的帮助  
* obj?  
&nbsp;&nbsp;&nbsp;&nbsp;列出obj对象的详细信息  
* obj??  
&nbsp;&nbsp;&nbsp;&nbsp;列出更加详细的信息  

##### 特殊变量
_ 表示前一次输出  
__ 表示倒数第二次输出  
___ 表示倒数第三次输出  
_dh 目录历史  
_oh 输出历史

##### shell命令
!+shell命令 可以执行shell命令
>ex:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!ls -l  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!touch test.txt  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;files = !ls -l | grep py

***
### 集set
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set翻译为集合，collection翻译为集合类型，是一个大概念。set是**可变的、无序的、不重复**的元素的集合

##### set定义 初始化
set( ) -> 空集合  
set (iterable) -> 新的集合  
s1 = { }  这不是空集合，这个是空字典

##### set的元素
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set的元素要求必须可以hash,不可hash的类型右list、set等，set的元素不可以使用索引，set可以迭代。

##### set增加
add(elem)  
&nbsp;&nbsp;&nbsp;增加一个元素到set中  
&nbsp;&nbsp;&nbsp;如果元素存在，什么都不做  

update(*others)  
&nbsp;&nbsp;&nbsp;合并其他元素到set集合中来  
&nbsp;&nbsp;&nbsp;参数others必须是可迭代对象  
&nbsp;&nbsp;&nbsp;是就地修改的

##### set删除
remove(elem)  
&nbsp;&nbsp;&nbsp;从set中移除一个元素  
&nbsp;&nbsp;&nbsp;元素不存在，抛出KeyError异常。  

discard(elem)  
&nbsp;&nbsp;&nbsp;从set中移除一个元素  
&nbsp;&nbsp;&nbsp;元素不存在，什么都不做  

pop() ->item  
&nbsp;&nbsp;&nbsp;移除并返回任意的元素  
&nbsp;&nbsp;&nbsp;空集返回KeyError异常  

clear()  
&nbsp;&nbsp;&nbsp;移除所有元素

##### set修改、查询
修改  
&nbsp;&nbsp;&nbsp;因为set是无序的、不重复的，修改等于删除再加入新的元素，所以set没有修改操作，要么删除，要么加入新的元素。  

查询  
&nbsp;&nbsp;&nbsp;非线性结构，无法索引  

遍历  
&nbsp;&nbsp;&nbsp;可以迭代所有元素

##### set和线性结构
&nbsp;&nbsp;&nbsp;线性结构的查询时间复杂度是O(n),即随着数据规模的增大而增加耗时  
&nbsp;&nbsp;&nbsp;set、dict的结构，内部使用hash值作为key，时间复杂度可以做到O(1),查询时间和数据规模无关  

可hash  
&nbsp;&nbsp;&nbsp;数字型int、float、complex，布尔型Ture、False，字符串string、bytes，tuple，None以上都是不可变类型，是可哈希类型。  

set的元素必须是可hash的

### 集合
基本概念  
&nbsp;&nbsp;&nbsp;全集  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所有元素的集合。例如实数集，所有实数组成的集合就是全集。  
&nbsp;&nbsp;&nbsp;子集subset和超集superset  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一个集合A所有元素都在另一个集合B内，A是B的子集，B是A的超集  
&nbsp;&nbsp;&nbsp;真子集和真超集  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A是B的子集，且A不等于B，A就是B的真子集，B是A的真超集  
&nbsp;&nbsp;&nbsp;并集：多个集合合并的结果  
&nbsp;&nbsp;&nbsp;交集：多个集合的公共部分  
&nbsp;&nbsp;&nbsp;差集：集合中除去和其他集合公共部分

##### 集合运算
并集  
&nbsp;&nbsp;&nbsp;将两个集合A和B的所有元素合并到一起，组成的集合称作集合A与集合B的并集  
&nbsp;&nbsp;&nbsp;union(*others)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;返回和多个集合合并后的新的集合  
&nbsp;&nbsp;&nbsp;| 运算符重载  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;等同union  
&nbsp;&nbsp;&nbsp;update(*others)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;和多个集合合并，就地修改  
&nbsp;&nbsp;&nbsp;|= 等同update  

交集  
&nbsp;&nbsp;&nbsp;集合A和B，由所有属于A且属于B的元素组成的集合  
&nbsp;&nbsp;&nbsp;intersection(*others)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;返回和多个集合的交集  
&nbsp;&nbsp;&nbsp;&  等同intersection  
&nbsp;&nbsp;&nbsp;intersection_update(*others)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;获取和多个集合的交集，并就地修改  
&nbsp;&nbsp;&nbsp;&= 等同intersection_update  

差集  
&nbsp;&nbsp;&nbsp;集合A和B，由所有属于A且不属于B的元素组成的集合  
&nbsp;&nbsp;&nbsp;difference(*others)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;返回和多个集合的差集  
&nbsp;&nbsp;&nbsp;- 等同difference  
&nbsp;&nbsp;&nbsp;difference_update(*others)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;获取和多个集合的差集并就地修改  
&nbsp;&nbsp;&nbsp;-= 等同difference_update  

对称差集  
&nbsp;&nbsp;&nbsp;集合A和B，由所有不属于A和B的交集元素组成的集合  
&nbsp;&nbsp;&nbsp;symmetric_differece(other)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;返回和另一个集合的差集  
&nbsp;&nbsp;&nbsp;^ 等同symmetric_differece  
&nbsp;&nbsp;&nbsp;symmetric_differece_update(other)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;获取和另一个集合的差集并就地修改  
&nbsp;&nbsp;&nbsp;^= 等同symmetric_differece_update  

issubset(other)、<=  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;判断当前集合是否是另一个集合的子集  
set1 < set2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;判断set1是否是set2的真子集  
issuperset(other)、>=  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;判断当前集合是否是other的超集  
set1 > set2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;判断set1是否是set2的真超集  
isdisjoint(other)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当前集合和另一个集合没有交集，没有交集，返回True
***
### 字典dict
&nbsp;&nbsp;&nbsp;&nbsp;字典是key-value键值对的数据的集合，和集合一样，是可变的、无序的，dict字典key不重复，是唯一的。  

##### 字典dict定义 初始化
d = dict() 或者 d = {} - > 这是定义一个空字典  

dict(**kwargs) 使用name = value 对初始化一个字典  

dict(iterable,**kwarg)使用可迭代对象和name = value对构造字典，不过可迭代对象的对象必须是一个二元结构  
&nbsp;&nbsp;&nbsp;&nbsp;d = dict(((1,'a',(2,'b'))) 或者 d = dict(([1,'a'],[2,'b']))  

dict(mapping,**kwarg)使用一个字典取构建另一个字典  

d = {'a':10,'b':20,'c':None,'d':[1,2,3]}  

类方法dict.fromkeys(iterable,value)  
&nbsp;&nbsp;&nbsp;&nbsp;d = dict.fromkeys(range(5))  
&nbsp;&nbsp;&nbsp;&nbsp;d = dict.fromkeys(range(5),0)  

##### 字典元素的访问
d[key]  
&nbsp;&nbsp;&nbsp;&nbsp;返回key对应的值value  
&nbsp;&nbsp;&nbsp;&nbsp;key不存在抛出KeyError异常  

get(key[,default])  
&nbsp;&nbsp;&nbsp;&nbsp;返回key对应的值value  
&nbsp;&nbsp;&nbsp;&nbsp;key不存在返回缺省值，如果没有设置缺省值就返回None  

setdefault(key,[default])  
&nbsp;&nbsp;&nbsp;&nbsp;返回key对应的值  
&nbsp;&nbsp;&nbsp;&nbsp;key不存在，添加kv对，value设置为default，并返回defau，如果default没有设置，缺省值为None  

##### 字典增加和修改
d[key] = value  
&nbsp;&nbsp;&nbsp;&nbsp;将key对应的值修改为value  
&nbsp;&nbsp;&nbsp;&nbsp;key不存在添加新的kv对  

update([other]) -> None  
&nbsp;&nbsp;&nbsp;&nbsp;使用另一个字典的kv对更新本字典  
&nbsp;&nbsp;&nbsp;&nbsp;key不存在，就添加  
&nbsp;&nbsp;&nbsp;&nbsp;key存在，覆盖已经存在的key对应的值  
&nbsp;&nbsp;&nbsp;&nbsp;就地修改  

##### 字典删除
pop(key[,default])  
&nbsp;&nbsp;&nbsp;&nbsp;key存在，移除它，并返回它的value  
&nbsp;&nbsp;&nbsp;&nbsp;key不存在，返回给定的default  
&nbsp;&nbsp;&nbsp;&nbsp;default未设置，key不存在则抛出KeyError异常  

popitem()  
&nbsp;&nbsp;&nbsp;&nbsp;移除并返回一个任意的键值对  
&nbsp;&nbsp;&nbsp;&nbsp;字典为empty，抛出KeyError异常  

clear()  
&nbsp;&nbsp;&nbsp;&nbsp;清空字典

##### 字典遍历  
for ... in dict  
&nbsp;&nbsp;&nbsp;&nbsp;遍历key  
* for k in d:  
&nbsp;&nbsp;&nbsp;&nbsp;print(k)  
* for k in d.keys():  
&nbsp;&nbsp;&nbsp;&nbsp;print(k)  

&nbsp;&nbsp;&nbsp;&nbsp;遍历value  
* for k in d:  
&nbsp;&nbsp;&nbsp;&nbsp;print(d[k])  
* for k in d.keys():  
&nbsp;&nbsp;&nbsp;&nbsp;print(d.get(k))
* for v in d.values():  
&nbsp;&nbsp;&nbsp;&nbsp;print(v)  

&nbsp;&nbsp;&nbsp;&nbsp;遍历item，即kv对 
* for item in d.items():  
&nbsp;&nbsp;&nbsp;&nbsp;print(item)
* for item in d.items():  
&nbsp;&nbsp;&nbsp;&nbsp;print(item[0],item[1])
* for k,v in d.items():  
&nbsp;&nbsp;&nbsp;&nbsp;print(k,v)
* for k,_ in d.items():  
&nbsp;&nbsp;&nbsp;&nbsp;print(k)
* for _,v in d.items():  
&nbsp;&nbsp;&nbsp;&nbsp;print(v)  

python3中，keys、values、items方法返回一个类似一个生成器的可迭代对象，不会把函数的返回结果复制到内存中，返回Dictionary view对象，可以使用len()、iter()、in操作，字典的entry的动态的视图，字典变化，试图将反映出这些变化，keys返回一个类set对象，也就是可以看做一个set集合，如果values都可以hash，那么items也可以看作是类set对象。  

python2中，上面的方法会返回一个新的列表，占据新的内存空间。所以python2建议使用iterkeys、itervalues、iteritems版本，返回一个迭代器，而不是返回一个copy。

##### 字典的key
&nbsp;&nbsp;&nbsp;&nbsp;key的要求和set的元素要求一致，set的元素可以就是看作key，set可以看作dict的简化版，hashable可哈希才可以作为key，可以使用hash()测试。

##### defaultdict
collections.defaultdict([default_factory[,...]])  
&nbsp;&nbsp;&nbsp;&nbsp;第一个参数是default_factory,缺省值是None，它提供一个初始化函数。当key不存在的时候，会调用这个工厂函数来生成key对应的value  
&nbsp;&nbsp;&nbsp;&nbsp;构造一个字典，values是列表，为其添加随机个元素

##### OrderedDict
collection.OrderDict([items])  
&nbsp;&nbsp;&nbsp;&nbsp;key并不是按照加入的顺序排列，可以使用OrderDict记录顺序  
&nbsp;&nbsp;&nbsp;&nbsp;有序字典可以记录元素插入的顺序，打印的时候也是按照这个顺序输出打印  
&nbsp;&nbsp;&nbsp;&nbsp;3.6版本的Python的字典就是记录key插入的顺序(IPython不一定由效果)