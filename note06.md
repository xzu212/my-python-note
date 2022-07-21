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
