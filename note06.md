# 用户输入和while 循环

## 函数`input()`的工作原理

函数`input()`让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其赋给一个变量，以方便使用。

### 编写清晰的程序

每当使用函数`input()`时，都应指定清晰易懂的提示，准确地指出希望用户提供什么样的信息。

```
name = input("Please enter your name :")
print(f"\nHello,{name}!")

---
Please enter your name :Eric

Hello,Eric!
```

有时候，提示可能超过一行。例如，你可能需要指出获取特定输入的原因。在这种情况下，可将提示赋给一个变量，再将该变量传递给函数`input()`。这样，即便提示超过一行，`input()`语句也会非常清晰。

```
prompt = "If you tell us who you are,we can personalize the messages"
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello,{name}!")

---
If you tell us who you are,we can personalize the messages
What is your first name?Eric

Hello,Eric!
```

### 使用`int()`来获取输入值

使用函数`input()`时，Python将用户输入解读为**字符串**。

 ```
>>> age = input("How old are you? ") 
How old are you? 21 
>>> age 
'21'
```
用户输入的是数21，但我们请求Python提供变量age的值时，它返回的是'21' ——用户输入数值的字符串表示。

>可使用函数`int()`解决这个问题，它让Python将输入视为数值。函数`int()`将数的字符串表示转换为数值表示。

```
>>>age = input("How old are you ? ")
How old are you ? 21
>>>age = int(age)
>>>age >= 18
True
```

输入21后，Python将这个数解读为字符串，但随后`int()`将这个字符串转换成数值表示。

这样Python就能运行条件测试了：将变量age(它现在表示的是数值21)同18进行比较，看它是否大于或等于18。测试结果为True。

### 求模运算符

处理数值信息时，求模运算符(%)是个很有用的工具，它将两个数相除并返回余数。

>如果一个数可被另一个数整除，余数就为0，因此求模运算将返回0。可利用这一点来判断一个数是奇数还是偶数。

```
number = input("Enter a number ,and I'll tell you if  it's even or odd:")
Enter a number ,and I'll tell you if  it's even or odd:42

number = int(number)

if number % 2 == 0 :
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

---
The number 42 is even.
```

## while循环简介

`for`循环用于针对集合中的每个元素都执行一个代码块，而`while`循环则不断运行，直到指定的条件不满足为止。

### 使用while循环

可使用`while`循环来数数，下面的`while`循环从1数到5：

```
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

---
1
2
3
4
5
```

### 让用户选择何时退出

>可以使用while循环让程序在用户愿意时不断运行，如下面的程序所示。在其中定义了一个退出值，只要用户输入的不是这个值，程序就将接着运行：

```
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    
---
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.Hello ,everyone!
Hello ,everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.Hello ,again!
Hello ,again!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.quit
quit
```

它将单词'quit'作为一条消息打印了出来。修复这种问题，只需使用一个简单的if测试：

```
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message !='quit':
        print(message)

---
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.Hello , everyone !
Hello , everyone !

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.Hello , again.
Hello , again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program.quit
```

### 使用标志

在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。这个变量称为标志(flag)。

可以让程序在标志为True时继续运行，并在任何事件导致标志的值为False时让程序停止运行。

这样，在while语句中就只需检查一个条件：标志的当前值是否为True。然后将所有其他测试（是否发生了应将标志设置为False的事件）都放在其他地方，从而让程序更整洁。

>添加一个标志,将其命名为active，用于判断程序是否应继续运行：

```
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
```

### 使用`break`退出循环

break语句用于控制程序流程，可用来控制哪些代码行将执行、哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。

```
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished."

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
 ```
                                                  