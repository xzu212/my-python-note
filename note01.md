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
在字符串中添加换行符，可使用字符组合`\n`。
```
>>>print("Languages:\nPython\nC\nJavaScript")
Languages: 
Python 
C 
JavaScript
```

### 删除空白

Python能够找出字符串开头和末尾多余的空白。
要确保字符串末尾没有空白，可使用方法`rstrip()` 。

暂时删除：
```
>>> favorite_language = 'python ' 
>>> favorite_language 
'python ' 
>>> favorite_language.rstrip() 
'python'
>>> favorite_language 
'python '
```

永久删除字符串中的空白：
```
>>> favorite_language = 'python '
>>> favorite_language = favorite_language.rstrip() 
>>> favorite_language 
'python'
```

为删除这个字符串中的空白，要将其末尾的空白剔除，再将结果关联到原来的变量。
删除字符串开头的空白，或者同时删除字符串两边的空白。可分别使用方法lstrip() 和strip() ：
```
>>> favorite_language = ' python ' 
>>> favorite_language.rstrip() 
' python' 
>>> favorite_language.lstrip() 
'python ' 
>>> favorite_language.strip() 
'python'
```

### 使用字符串时避免语法错误 

例如：在用单引号括起的字符串中，如果包含撇号，就将导致错误。这是因为这会导致Python将第一个单引号和撇号之间的内容视为一个字符串，进而将余下的文本视为Python代码，从而引发错误。
```
message = "One of Python's strengths is its diverse community." 
print(message)
```
撇号位于两个双引号之间，因此Python解释器能够正确地理解这个字符串：
```
One of Python's strengths is its diverse community.
```

然而，如果使用单引号，Python将无法正确地确定字符串的结束位置：
```
message = 'One of Python's strengths is its diverse community.'
print(message)
```
输出错误。

## 数

在Python中，可对整数执行加（+ ）减（- ）乘（* ）除（/ ）运算。

在Python中，使用两个乘号`**`表示乘方运算。

Python还支持运算次序，因此可在同一个表达式中使用多种运算。还可以使用圆括号来修改运算次序，让Python按你指定的次序执行运算。

### 浮点数

Python将所有带小数点的数称为浮点数。

### 整数和浮点数

将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除;

在其他任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数。

### 数中的下划线

书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读，当你打印这种使用下划线定义的数时，Python不会打印其中的下划线：
```
>>> universe_age = 14_000_000_000
>>> print(universe_age) 
14000000000
```

### 同时给多个变量赋值

```
>>> x, y, z = 0, 0, 0
```

### 常量

常量  类似于变量，但其值在程序内保持不变。Python没有内置的常量类型，但会使用全大写来指出应将某个变量视为常量，其值应始终不变：

```
MAX_CONNECTIONS = 5000
```

### 注释

在Python中，注释用井号(#)标识。井号后面的内容都会被Python解释器忽略。
