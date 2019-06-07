### 参数注解
##### 函数定义的弊端
python是动态语言，变量随时可以被赋值，且能赋值为不同的类型  
python不是静态编译语言，变量类型是在运动期决定的  
动态语言很灵活，但是这种特性也是弊端
~~~
def add(x,y):
    return x + y
print(add(4,5))
print(add('hello','world'))
print(add(4,'hello'))  #报错，整形和字符串不能相加
~~~
难发现：由于不做任何类型检查，直到运行期问题下回显示出来，或者线上运行时才能暴露出问题  
难使用：函数的使用者看到函数的时候，并不知道你的函数的设计，并不知道应该传入什么类型的数据  

**解决这种动态语言定义的弊端**  
增加文档Documentation String  
&nbsp;&nbsp;&nbsp;&nbsp;这只是一个惯例，不是强制标准，不能要求程序员一定为函数提供说明文档  
&nbsp;&nbsp;&nbsp;&nbsp;函数定义更新了，文档未必同步更新
~~~
def add(x,y):
    """
    :param x: int
    :param y: int
    :return: int
    """
    return x + y
print(help(add))
~~~
##### 函数注解
~~~
def add(x:int, y:int) -> int:
    """
    :param x: int
    :param y: int
    :return: int
    """
    return x + y
print(help(add))
print(add(4,5))
print(add('mag','edu')) #使用pycharm时输入实参类型不正确时会有颜色提醒，但是不会影响函数执行
~~~
函数注解  
&nbsp;&nbsp;&nbsp;&nbsp;python3.5引入  
&nbsp;&nbsp;&nbsp;&nbsp;对函数的参数进行类型注解  
&nbsp;&nbsp;&nbsp;&nbsp;对函数的返回值进行类型注解  
&nbsp;&nbsp;&nbsp;&nbsp;只对函数参数做一个辅助的说明，并不对函数参数进行类型检查  
&nbsp;&nbsp;&nbsp;&nbsp;提供给第三方工具，做代码分析，发现隐藏的bug  
&nbsp;&nbsp;&nbsp;&nbsp;函数注解的信息，保存在__annotations__属性中  

变量注解  
&nbsp;&nbsp;&nbsp;&nbsp;python3.6引入。注意它也是一种对变量的说明，非强制  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i : int = 3

##### 业务应用
函数参数类型类型检查  
思路  
&nbsp;&nbsp;&nbsp;&nbsp;函数参数的检查，一定是在函数外，如果把检查代码侵入到函数中  
&nbsp;&nbsp;&nbsp;&nbsp;函数应该作为参数，传入到函数中  
&nbsp;&nbsp;&nbsp;&nbsp;检查函数拿到函数传入的实际参数，与形参声明对比  
&nbsp;&nbsp;&nbsp;&nbsp;__annotations__属性是一个字典，其中包括返回值类型的声明。假设要做位置参数的判断，无法和字典中的声明对应。使用inspect模块  

##### inspect模块
Parameter对象  
&nbsp;&nbsp;&nbsp;&nbsp;保存在元组中，是只读的  
&nbsp;&nbsp;&nbsp;&nbsp;name，参数的名字  
&nbsp;&nbsp;&nbsp;&nbsp;annotation，参数的注解，可能没有定义  
&nbsp;&nbsp;&nbsp;&nbsp;default，参数的缺省值，可能没有定义  
&nbsp;&nbsp;&nbsp;&nbsp;empty，特殊的类，用来标记default属性或者注释annotation属性的空值  
&nbsp;&nbsp;&nbsp;&nbsp;kind，实参如何绑定到形参，就是形参的类型  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POSITIONAL_ONLY,值必须是位置参数提供  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;POSITIONAL_OR_KEYWORD,值可以作为关键字或者位置参数提供  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VAR_POSITIONAL,可变位置参数，对应*args  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;KEYWORD_ONLY,keyword-only，对应\*或者\*args之后出现的非可变关键字参数  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VAR_KEYWORD,可变关键字参数，对应**kwargs

### functools模板
reduce方法  
&nbsp;&nbsp;&nbsp;&nbsp;reduce方法，顾名思义就是减少  
&nbsp;&nbsp;&nbsp;&nbsp;reduce(function,sequence[,initial]) -> value  
&nbsp;&nbsp;&nbsp;&nbsp;可迭代对象不能为空；初始值没提供就在可迭代对象中去一个元素  

partial方法  
&nbsp;&nbsp;&nbsp;&nbsp;偏函数，把函数部分的参数固定下来，相当于为部分的参数添加了一个固定的默认值，形成一个新的函数并返回  
&nbsp;&nbsp;&nbsp;&nbsp;从partial生成的新的函数，是对原函数的封装  

lru_cache装饰器  
&nbsp;&nbsp;&nbsp;&nbsp;通过一个字典缓存被装饰函数的调用和返回值  
斐波那契数列递归方法的改造
~~~
import functools
@functools.lru_cache()
def fib(n):
    return 1 if n<3 else fib(n-1) + fib(n-2)
print([fib(i+1) for i in range(35)])
~~~
##### lru_cache装饰器应用  
使用前提  
&nbsp;&nbsp;&nbsp;&nbsp;同样的函数参数一定得到同样的结果  
&nbsp;&nbsp;&nbsp;&nbsp;函数执行时间很长，且要多次执行  
本质是函数调用的参数 => 返回值  
缺点  
&nbsp;&nbsp;&nbsp;&nbsp;不支持缓存过期，key无法过期、失效  
&nbsp;&nbsp;&nbsp;&nbsp;不支持清楚操作  
&nbsp;&nbsp;&nbsp;&nbsp;不支持分布式，式一个单机的缓存  
适用场景，单机上需要空间换时间的地方，可以用缓存来将计算变成快速的查询