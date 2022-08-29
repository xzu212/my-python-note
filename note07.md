# 函数

函数是带名字的代码块，用于完成具体的工作。要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，无须反复编写完成该任务的代码，只需要调用执行该任务的函数，让Python运行其中的代码即可。

## 定义函数

```
def greet_user():
    """显示简单的问候语。"""
    print("Hello!")
    
greet_user()

---
Hello!
```

### 向函数传递信息

```
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello,{username.title()}!")
    
greet_user('jesse')

---
Hello,Jesse!
```

### 实参和形参

在函数`greet_user()`的定义中，变量`username`是一个形参(`parameter`)，即函数完成工作所需的信息。

在代码`greet_user('jesse')`中，值`'jesse'`是一个实参(`argument`)，即调用函数时传递给函数的信息。

在`greet_user('jesse')`中，将实参`'jesse'`传递给了函数`greet_user()`，这个值被赋给了形参`username`。

## 传递实参

函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。

向函数传递实参的方式很多：可使用位置实参，这要求实参的顺序与形参的顺序相同；也可使用关键字实参，其中每个实参都由变量名和值组成；还可使用列表和字典。

### 位置实参

调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。

为此，最简单的关联方式是基于实参的顺序。这种关联方式称为**位置实参**。

```
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster','harry')

---
I have a hamster.
My hamster's name is Harry.
```
 
1. **多次调用函数**

可以根据需要调用函数任意次。要再次描述，只需要再次调用即可：

```
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster','harry')
describe_pet('dog','willie')

---
I have a hamster.
My hamster's name is Harry.
I have a dog.
My dog's name is Willie.
```

### 关键字实参

关键字实参是传递给函数的名称值对。

因为直接在实参中将名称和值关联起来，所以向函数传递实参时不会混淆。

关键字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。

```
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type='hamster',pet_name='harry')

---
I have a hamster.
My hamster's name is Harry.
```

下面两个函数调用是等效的

```
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')
```

### 默认值

编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。

因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。

>例如，如果发现调用`describe_pet()`时，描述的大多是小狗，就可将形参`animal_type`的默认值设置为`'dog'`。这样，调用`describe_pet()`来描述小狗时，就可不提供这种信息：

```
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(pet_name='willie')

---
I have a dog.
My dog's name is Willie.
```
> 给形参`animal_type`指定了默认值`'dog'`，调用这个函数时，如果没有给`animal_type`指定值，Python就将把这个形参设置为`'dog'`。

### 等效的函数调用

```
def describe_pet(pet_name, animal_type='dog'):
```
>基于这种定义，在任何情况下都必须给`pet_name`提供实参。指定该实参时可采用位置方式，也可采用关键字方式。
>如果要描述的动物不是小狗，还必须在函数调用中给`animal_type`提供实参。同样，指定该实参时可以采用位置方式，也可采用关键字方式。

下面对这个函数的所有调用都可行：

```
# 一条名为Willie的小狗。 
describe_pet('willie') 
describe_pet(pet_name='willie') 
# 一只名为Harry的仓鼠。 
describe_pet('harry', 'hamster') 
describe_pet(pet_name='harry', animal_type='hamster') 
describe_pet(animal_type='hamster', pet_name='harry')
```

### 避免实参错误

提供的实参多于或少于函数完成工作所需的信息时，将出现实参不匹配错误。

## 返回值

函数可以处理一些数据，并返回一个或一组值。函数返回的值称为**返回值**。在函数中，可使用`return`语句将值返回到调用函数的代码行。
返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

### 返回简单值

```
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

---
Jimi Hendrix
```

### 让实参变成可选的

>扩展函数`get_formatted_name()`，使其同时处理中间名：

```
def get_formatted_name(first_name,middle_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

---
John Lee Hooker
```
>只要同时提供名、中间名和姓，这个函数就能正确运行。

并非所有的人都有中间名，但如果调用这个函数时只提供了名和姓，它将不能正确运行。

为了让中间名变成可选的，可给形参`middle_name`指定一个空的默认值，并在用户没有提供中间名时不使用这个形参。

为让`get_formatted_name()`在没有提供中间名时依然可行，可将形参`middle_name`的默认值设置为空字符串，并将其移到形参列表的末尾：

```
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

---
Jimi Hendrix
John Lee Hooker
```
调用这个函数时，如果只想指定名和姓，调用起来将非常简单。

如果还要指定中间名，就必须确保它是最后一个实参，这样Python才能正确地将位置实参关联到形参。

### 返回字典

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。

```
def build_person(first_name,last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name,'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

---
{'first': 'jimi', 'last': 'hendrix'}
```

>下面的修改让你能存储年龄：

```
def build_person(first_name,last_name,age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name,'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=27)
print(musician)

---
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
```

### 结合使用函数和while循环

>结合使用函数`get_formatted_name()`和`while`循环，以更正式的方式问候用户：

