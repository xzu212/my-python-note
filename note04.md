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

```
>>> age_0 = 22 
>>> age_1 = 18 
>>> age_0 >= 21 and age_1 >= 21 
False
>>> age_1 = 22 
>>> age_0 >= 21 and age_1 >= 21 
True
```

为改善可读性，可将每个测试分别放在一对圆括号内，但并非必须这样做：
```
(age_0 >= 21) and (age_1 >= 21)
```

2. 使用`or`检查多个条件

>关键字`or`也能够让你检查多个条件，但只要至少一个条件满足，就能通过整个测试。
>
>仅当两个测试都没有通过时，使用`or`的表达式才为`False`。

```
>>> age_0 = 22 
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21 
True
>>> age_0 = 18 
>>> age_0 >= 21 or age_1 >= 21 
False
```

### 检查特定值是否包含在列表中

>要判断特定的值是否已包含在列表中，可使用关键字`in`。

```
>>>requested_toppings = ['mushrooms','onions','pineapple']
>>>'mushrooms' in requested_toppings
True
>>>'pepperoni' in requested_toppings
False
```

### 检查特定值是否不包含在列表中

>还有些时候，确定特定的值未包含在列表中很重要。在这种情况下，可使用关键字`not in`。

```
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")
    
---
Marie,you can post a response if you wish.
```

### 布尔表达式

>**布尔表达式**，它不过是条件测试的别名。与条件表达式一样，布尔表达式的结果要么为`True`，要么为`False`。

## if语句

### 简单的if语句

```
age = 19
if age > 18:
    print("You are old enough to vote !")
    
---
You are old enough to vote !
```

在`if`语句中，缩进的作用与在`for`循环中相同。如果测试通过了，将执行`if`语句后面所有缩进的代码行，否则将忽略它们。 

在紧跟`if`语句后面的代码块中，可根据需要包含**任意数量**的代码行。

### if-else语句

>在条件测试通过时执行一个操作，在没有通过时执行另一个操作，可使用Python提供的if-else语句。

```
age = 17
if age >= 18:
    print("You are old enough to vote !")
    print("Have you register to vote as soon as you turn 18 !")
else:
    print("Sorry , you are too young to vote .")
    print("Please register to vote as soon as you turn 18 !")
    
---
Sorry , you are too young to vote .
Please register to vote as soon as you turn 18 !
```

### if-elif-else 结构

>检查超过两个的情形，可使用Python提供的`if-elif-else`结构。
>
>Python只执行`if-elif-else`结构中的一个代码块。它依次检查每个条件测试，直到遇到通过了的条件测试。
>
>测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试。

```
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    
---
Your admission cost is $25.
```
简化代码：
```
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

```

### 使用多个elif代码块

```
age = 12
if age < 4:
    price = 0
elif age <18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")
```

### 省略else代码块

```
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age > 65:
    price = 20

print(f"Your admission cost is ${price}.")
```

### 测试多个条件

>`if-elif-else`结构功能强大，但仅适用于只有一个条件满足的情况：遇到通过了的测试后，Python就跳过余下的测试。
>
>这种行为很好，效率很高，让你能够测试一个特定的条件。 
>
>**然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含`elif`和`else`代码块的简单`if`语句。**
>
>在可能有多个条件为`True`且需要在每个条件为`True`时都采取相应措施时，适合使用这种方法。

```
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza.")

---
Adding mushrooms.
Adding extra cheese.

Finished making your pizza.
```

**如果只想执行一个代码块，就使用`if-elif-else`结构；如果要执行多个代码块，就使用一系列独立的`if`语句。**

## 使用if语句处理列表

### 检查特殊元素
