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

在函数greet_user()的定义中，变量`username`是一个形参(parameter)，即函数完成工作所需的信息。

在代码greet_user('jesse') 中，值'jesse'是一个实参(argument)，即调用函数时传递给函数的信息。

在greet_user('jesse')中，将实参'jesse'传递给了函数greet_user()，这个值被赋给了形参username。
