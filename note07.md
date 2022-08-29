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

