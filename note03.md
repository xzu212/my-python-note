# 操作列表

## 遍历整个列表

>假设有一个魔术师名单，需要将每个名字都打印出来。为此，可以分别获取名单中的每个名字，但这种做法会导致多个问题：
>
>* 例如，如果名单很长，将包含大量重复的代码。  
>* 另外，每当名单的长度发生变化时，都必须修改代码。  
>* 通过使用`for`循环，可以让Python去处理这些问题。

```
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
    
---

alice
david
carolina
```

* 首先，定义一个列表`magicians`。
* 接下来，定义一个`for循环`。从列表`magicians`中取出一个名字，并将其与变量`magician`相关联。  
* 最后，打印前面赋给变量`magician`的名字。
* 这样，对于列表中的每个名字，Python都将重复执行代码。
* 可以这样解读这些代码：对于列表magicians中的每位魔术师，都将其名字打印出来。

### 深入研究循环

对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素。  
如果列表包含一百万个元素，Python就重复执行指定的步骤一百万次，且通常速度非常快。

编写for 循环时，可以给依次与列表中每个值相关联的临时 变量指定任意名称。

```
for cat in cats: 
for dog in dogs: 
for item in list_of_items:
```

