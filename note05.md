# 字典

## 一个简单的字典

```
alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

---
green
5
```

## 使用字典 

在Python中，字典是一系列键值对。每个键都与一个值相关联，你可使用键来访问相关联的值。

与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。 

在Python中，字典用放在花括号`({})`中的一系列键值对表示，如前面的示例所示：

```
alien_0 = {'color':'green','points':5}
```

**键值对**是两个相关联的值。指定键时，Python将返回与之相关联的值。

键和值之间用冒号分隔，而键值对之间用逗号分隔。在字典中，想存储多少个键值对都可以。

### 访问字典中的值

要获取与键相关联的值，可依次指定字典名和放在方括号内的键：

```
alien_0 = {'color':'green','points':5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

---
You just earned 5 points!
```

### 添加键值对

字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名、用方括号括起的键和相关联的值。

```
alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

---
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

### 先创建一个空字典

在空字典中添加键值对有时候可提供便利，而有时候必须这样做。为此，可先使用一对空花括号定义一个字典，再分行添加各个键值对。

```
alien_0 = {} 
alien_0['color'] = 'green' 
alien_0['points'] = 5 
print(alien_0)

---
{'color': 'green', 'points': 5}
```
使用字典来存储数据或在编写能自动生成大量键值对的代码时，通常需要先定义一个空字典。

### 修改字典中的值

要修改字典中的值，可依次指定字典名、用方括号括起的键，以及与该键相关联的新值。

>将一个外星人从绿色改为黄色：
```
alien_0 = {'color': 'green'} 
print(f"The alien is {alien_0['color']}.") 
alien_0['color'] = 'yellow' 
print(f"The alien is now {alien_0['color']}.")

---
The alien is green.
The alien is now yellow.
```

******

>对一个能够以不同速度移动的外星人进行位置跟踪。为此，我们将存储该外星人的当前速度，并据此确定该外星人将向右移动多远：

```
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print(f"Original x-position: {alien_0['x_position']}") 
# 向右移动外星人。 
# 根据当前速度确定将外星人向右移动多远。 
if alien_0['speed'] == 'slow': 
    x_increment = 1 
elif alien_0['speed'] == 'medium': 
    x_increment = 2 
else: 
    # 这个外星人的移动速度肯定很快。 
    x_increment = 3 
    
# 新位置为旧位置加上移动距离。 
alien_0['x_position'] = alien_0['x_position'] + x_increment 
print(f"New x-position: {alien_0['x_position']}")

---
Original x-position: 0
New x-position: 2
```
>首先定义一个外星人，其中包含初始坐标和坐标，还有速度`'medium'`。
>
>打印`x_position`的初始值，旨在知道这个外星人向右移动了多远。
>
>使用一个`if-elif-else`结构来确定外星人应向右移动多远，并将这个值赋给变量`x_increment`。
>
>如果外星人的速度为`'slow'`，它将向右移动一个单位；如果速度为`'medium'`，将向右移动两个单位；如果为`'fast'`，将向右移动三个单位。确定移动距离后，将其与`x_position`的当前值相加，再将结果关联到字典中的键`x_position`。

### 删除键值对

对于字典中不再需要的信息，可使用`del`语句将相应的键值对彻底删除。使用`del`语句时，必须指定字典名和要删除的键。

>从字典`alien_0`中删除键`'points'`及其值：
```
alien_0 = {'color':'green','points':'5'}
print(alien_0)

del alien_0['points']
print(alien_0)

---
{'color': 'green', 'points': '5'}
{'color': 'green'}
```

### 由类似对象组成的字典

在前面的示例中，字典存储的是一个对象的多种信息，但也可以使用字典来存储众多对象的同一种信息。

```
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

---
Sarah's favorite language is C.
```
>获取Sarah喜欢的语言，并将其赋给变量`language`。创建这个新变量让函数调用`print()`变得整洁得多。

### 使用`get()`来访问值
