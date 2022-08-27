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
 
