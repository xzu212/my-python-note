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

Python将输入解读成了字符串，因为这个数用引号括起了。如果只想打印输入，这一点问题都没有；但如果试图将输入作为数来使用，就会引发错误。

```
>>>age  = input("How old are you ?")
How old are you ?21
>>>age >= 18
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [2], in <cell line: 1>()
----> 1 age >= 18

TypeError: '>=' not supported between instances of 'str' and 'int'
```

试图将输入用于数值比较时，Python会引发错误，因为它无法将字符串和整数进行比较。

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

The number 42 is even.
```

## while循环简介
