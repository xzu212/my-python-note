# if语句

## 一个示例

>假设有一个汽车列表，将其中汽车名称打印出来。对于大多数汽车，以首字母大写的方式打印其名称，但对于汽车名'bmw' ，以全大写的方式打印。
```
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())

---
Audi
BMW
Subaru
Toyota
```

## 条件测试

>每条`if`语句的核心都是一个值为`True`或`False`的表达式，这种表达式称为**条件测试**。
>
>Python根据条件测试的值为`True`还是`False`来决定是否执行`if`语句中的代码。
>
>如果条件测试的值为`True`，Python就执行紧跟在`if`语句后面的代码；如果为`False`，Python就忽略这些代码。

### 检查是否相等

大多数条件测试将一个变量的当前值同特定值进行比较。最简单的条件测试检查变量的值是否与特定值相等：
```
car = 'bmw'
car == 'bmw'

---
True
```
```
car = 'audi'
car == 'bmw'

---
False
```

### 检查是否相等时忽略大小写

>**在Python中检查是否相等时区分大小写。**

两个大小写不同的值被视为不相等：

```
car = 'audi'
car == 'Audi'

---
False
```
如果大小写很重要，这种行为有其优点。

但如果大小写无关紧要，只想检查变量的值，可将变量的值转换为小写，再进行比较：
```
car = 'Audi'
car.lower() == 'audi'

---
True
```
函数`lower()`不会修改最初赋给变量`car`的值，因此进行这样的比较时不会影响原来的变量：
```
car

---
'Audi'
```

### 检查是否不相等

要判断两个值是否不等，可结合使用惊叹号和等号`(!=)`

```
requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
---
Hold the anchovies!
```
>`if`代码行将`requested_topping`的值与`'anchovies'`进行比较。
>
>如果这两个值不相等，Python将返回`True`，进而执行紧跟在`if`语句后面的代码；
>
>如果相等，Python将返回`False`，因此不执行紧跟在`if`语句后面的代码。
>
>因为`requested_topping`的值不是`'anchovies'`，所以执行函数调用`print()`。

大多数条件表达式检查两个值是否相等，但有时候检查两个值是否不等的效率更高。

### 数值比较

>检查一个人是否是18岁：
```
age = 18
age == 18

---
True
```

>检查两个数是否不等：

```
answer = 17
if answer != 42:
    print("That is not the correct answer.Please try again.")
    
---
That is not the correct answer.Please try again.
```

>条件语句中可包含各种数学比较：

```
>>> age = 19 
>>> age < 21 
True 
>>> age <= 21 
True 
>>> age > 21 
False 
>>> age >= 21 
False
```

### 检查多个条件

1. 使用`and`检查多个条件

>要检查是否两个条件都为`True`，可使用关键字`and`将两个条件测试合而为一。
>
>如果每个测试都通过了，整个表达式就为`True`；如果至少一个测试没有通过，整个表达式就为`False`。

