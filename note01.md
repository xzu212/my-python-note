# 变量和简单数据类型

## 变量
输入：
```
message = "Hello Python world!" 
print(message)
message = "Hello Python Crash Course world!" 
print(message)
```
输出：
```
Hello Python world! 
Hello Python Crash Course world!
```
此处的`message`即为`变量`，每个变量都指向一个值。

在程序中可随时修改变量的值，而Python将始终记录变量的最新值。

### 变量的命名和使用

* 变量名只能包含字母、数字和下划线，开头只能是字母或者下划线，不能是数字开头。
* 变量名不能包含空格，但可以用下划线来分隔单词。
* Python关键字和函数名不能用作变量名。
* 变量名应该简短又具有描述性。
* 慎用小写字母`l`，和大写字母`O`，易于混淆成数字`1`和`0`。

## 字符串

字符串就是一系列字符。

在Python中，用引号括起的都是字符串，引号可以是单引号也可以是双引号。
```
"This is a string."
'This is also a string.'
'I told my friend,"Python is my favorite language!"'
"The language 'Python' is named after Monty Python,not the snake."
“One of python's strength is its diverse and supportive community."
```

### 使用方法修改字符串的大小写

```
name = "ada lovelace"
print(name.title())
```
得到输出：
```
Ada Lovelace
```
示例中，变量`name`指向小写字符串`"ada lovelace"`，在函数调用print()中，方法title()出现在变量后面。

方法是Python可对数据执行的操作。

在`name.title`中，`name`后面的句点让Python对变量`name`执行方法`title()`指定的操作。

方法`title()`以首字母大写的方式显示每个单词。

其他大小写处理方法：
```
name = "Ada Locelace"
print(name.upper)
print(name.lower)
```
输出：
```
ADA LOVELACE
ada lovelace
```

### 在字符串中使用变量

```
first_name = "ada" 
last_name = "lovelace" 
full_name = f"{first_name} {last_name}" 
print(full_name)
print(f"Hello,{full_name.title()}!")
message = f"Hello,{fullname.title()}!"
print(message)
```
得到输出：
```
ada lovelace
Hello,Ada Lovelace!
Hello,Ada Locelace!
```

在字符串中插入变量的值，可在引号前加上字母`f`，再将要插入的变量放在花括号内，在Python显示字符串时，将把每个变量都替换成该值。

`f字符串`，f是format的简写，Python通过把花括号内的变量替换为对应的值来设置字符串格式。

### 使用制表符或换行符来添加空白

在编程中，空白泛指任何非打印字符，如空格、制表符和换行符。

在字符串中添加制表符，可使用字符组合`\t`
```
>>>print("Python")
Python
>>>print("\tPython")
    Python
```
在字符串中添加换行符，可使用字符组合`\n`
```
>>>print("Languages:\nPython\nC\nJavaScript")
Languages: 
Python 
C 
JavaScript
```
