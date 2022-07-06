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

使用单数和复数式名称，可帮助判断代码段处理的是单个列表元素还是整个列表。

### 在`for`循环中执行更多操作

>在`for`循环中，可对每个元素执行任何操作。

```
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can`t wait to see your next trick,{magician.title()}.")

---
Alice,that was a great treak!
I can`t wait to see your next trick,Alice.
David,that was a great treak!
I can`t wait to see your next trick,David.
Carolina,that was a great treak!
I can`t wait to see your next trick,Carolina.
```

### 在`for`循环结束后执行一些操作

>`for`循环结束后，通常需要提供总结性输出或接着执行其他任务。
>
>在`for`循环后面，没有缩进的代码都只执行一次，不会重复执行。

```
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can`t wait to see your next trick,{magician.title()}.")
print("\nThank you ,everyone.That was a great magic show!")

---
Alice,that was a great trick!
I can`t wait to see your next trick,Alice.
David,that was a great trick!
I can`t wait to see your next trick,David.
Carolina,that was a great trick!
I can`t wait to see your next trick,Carolina.

Thank you,everyone.That was a great magic show!
```

## 避免缩进错误

Python根据缩进来判断代码行与前一个代码行的关系。  
一些常见的缩进错误：

* **忘记缩进**
* **忘记缩进额外的代码**
* **不必要的缩进**
* **循环后不必要的缩进**
* **遗漏了冒号**

## 创建数值列表

### 使用函数`range()`

>Python函数`range()`能够生成一系列数。

```
for value in range(1,5):
    print(value)
    
---
1
2
3
4
```
`range()`只打印1\~4，要打印1\~5，需要使用`range(1,6)`

调用函数`range()`时，也可只指定一个参数，这样它将从0开始。例如，range(6)返回数0\~5。

### 使用`range()`创建数字列表

要创建数字列表，可使用函数`list()`将`range()`的结果直接转换为**列表**。如果将`range()`作为`list()`的参数，输出将是一个数字列表。
```
numbers = list(range(1,6))
print(numbers)

---
[1, 2, 3, 4, 5]
```
