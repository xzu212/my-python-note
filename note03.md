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

使用函数`range()`时，还可**指定步长**。为此，可给这个函数指定第三个参数，Python将根据这个步长来生成数。

```
even_numbers = list(range(2,11,2))
print(even_numbers)

---
[2, 4, 6, 8, 10]
```

创建一个列表，将前十个整数的平方加入：
```
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

---
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
>1. 创建一个空列表`squares`；
>2. 使用函数`range()`让Python遍历1\~10的值；
>3. 计算当前数值的平方，并将结果赋给变量`square`；
>4. 将新计算得到的平方值附加到列表`squares`末尾；
>5. 最后，循环结束后打印列表`squares`。

为了让代码更简洁，可不使用临时变量`square`，而直接将每个计算得到的值附加到列表末尾：
```
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

---
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 对数字列表执行简单的统计计算

```
>>>digits = [1,2,3,4,5,6,7,8,9,0]
>>>min(digits)
0
>>>max(digits)
9
>>>sum(digits)
45
```

### 列表解析

前面的生成列表`squares`的方式包含三四行代码，而列表解析只需编写一行代码就能生成这样的列表。

列表解析将`for`循环和创建新元素的代码合并成一行，并自动附加新元素。

```
squares = [value**2 for value in range(1,11)]
print(squares)

---
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

>首先，指定一个描述性的列表名，如`squares`。
>
>然后，定义一个表达式，用于生成要存储到列表中的值。在这个示例中，表达式为`value**2`，它计算平方值。
> 
>接下来，编写一个`for`循环，用于给表达式提供值。
>
>在这个示例中，`for`循环为`for value in range(1,11)`，它将值`1~10`提供给表达式`value**2`。请注意，这里的for语句末尾没有冒号。

## 使用列表的一部分

>处理列表的部分元素，Python称之为切片。

### 切片

* 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。

* 与函数range()一样，Python在到达第二个索引之前的元素后停止。

* 要输出列表中的前三个元素，需要指定索引0和3，这将返回索引为0、1和2的元素。

```
players = ['charles','martina','michael','florence','eli']

print(players[0:3])  
['charles', 'martina', 'michael']    #只包含前三个元素

print(players[1:4])
['martina', 'michael', 'florence']    #提取第二、三、四个元素

print(players[:4])
['charles', 'martina', 'michael', 'florence']    #不指定第一个索引，自动从列表头开始

print(players[2:])
['michael', 'florence', 'eli']   #提取从第三个元素到列表末尾的所有元素

print(players[-3:])
['michael', 'florence', 'eli']    #提取最后三个元素

print(players[0:5:2])
['charles', 'michael', 'eli']    #每隔两个元素提取一个元素
```

### 遍历切片 

>要遍历列表的部分元素，可在`for`循环中使用切片。
```
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
---
Here are the first three players on my team:
Charles
Martina
Michael
```

### 复制列表

>要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引`([:])`。
>
>这让Python创建一个始于第一个元素、终止于最后一个元素的切片，即整个列表的副本。

```
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

---
My favorite foods are:
['pizza', 'falafel', 'carrot cake']
My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']

My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli']
My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'ice cream']
```

## 元组

>Python将不能修改的值称为不可变的 ，而不可变的列表被称为**元组**。

### 定义元组

>元组看起来很像列表，但使用圆括号而非中括号来标识。定义元组后，就可使用索引来访问其元素，就像访问列表元素一样。

```
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

---
200
50
```
试图修改元组的操作是被禁止的，Python不能给元组的元素赋值。

严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
```
my_t = (3,)
```
创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。

### 遍历元组中的所有值

>像列表一样，也可以使用`for`循环来遍历元组中的所有值,就像遍历列表时一样，Python返回元组中所有的元素：

```
dimensions =(200,50)
for dimension in dimensions:
    print(dimension)
    
---
200
50
```

### 修改元组变量

>不能修改元组的元素，但可以给存储元组的变量赋值。

```
dimensions = (200,50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400,80)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
---
original dimensions:
200
50

Modified dimensions:
400
80
``` 
