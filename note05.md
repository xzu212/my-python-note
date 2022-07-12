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

```
alien_0 = {'color': 'green'} 
print(f"The alien is {alien_0['color']}.") 
alien_0['color'] = 'yellow' 
print(f"The alien is now {alien_0['color']}.")

---
The alien is green.
The alien is now yellow.
```
