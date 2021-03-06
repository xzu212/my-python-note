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

使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：如果指定的键不存在就会出错。

就字典而言，可使用方法`get()`在指定的键不存在时返回一个默认值，从而避免这样的错误。

方法`get()`的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存在时要返回的值，是可选的。

```
alien_0 = {'color':'green','speed':'5'}
point_value = alien_0.get('points','No point value assigned.')
print(point_value)

---
No point value assigned.
```
>如果字典中有键`'points'`，将获得与之相关联的值；如果没有，将获得指定的默认值。虽然这里没有键`'points' `，但将获得一条清晰的消息，不会引发错误。
>
>如果指定的键有可能不存在，应考虑使用方法`get()`，而不要使用方括号表示法。

>调用`get()`时，如果没有指定第二个参数且指定的键不存在，Python将返回值`None`。这个特殊值表示没有相应的 值。`None`并非错误，而是一个表示所需值不存在的特殊值。

## 遍历字典

字典可用于以各种方式存储信息，因此有多种遍历方式：可遍历字典的所有键值对，也可仅遍历键或值。

### 遍历所有键值对

>下面的字典存储一名用户的用户名、名和姓：

```
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")
    
---
Key:username
Value:efermi

Key:first
Value:enrico

Key:last
Value:fermi
```
>编写遍历字典的`for`循环，可声明两个变量，用于存储键值对中的键和值。这两个变量可以使用任意名称。
>
>`for`语句的第二部分包含字典名和方法`items()`，它返回一个键值对列表。
>
>接下来，`for`循环依次将每个键值对赋给指定的两个变量，使用这两个变量来打印每个键及其相关联的值。

```
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

---
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```
>Python遍历字典中的每个键值对，并将键赋给变量`name`，将值赋给变量`language`。

### 遍历字典中的所有键

在不需要使用字典中的值时，方法`keys()`很有用。

******

>遍历字典`favorite_languages`，并将每个被调查者的名字都打印出来：

```
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in favorite_languages.keys():
    print(name.title())

---
Jen
Sarah
Edward
Phil
```
>Python提取字典`favorite_languages`中的所有**键**，并依次将它们赋给变量`name`。输出列出每个被调查者的名字。

遍历字典时，会默认遍历所有的键。因此，把
```
for name in favorite_languages.keys():
```
替换为
```
for name in favorite_languages:
```
输出将不变。显式地使用`keys()`可以让代码更容易理解。

>在循环中，可使用键来访问与之相关联的值。
```
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")

---
Hi Jen.
Hi Sarah.
	Sarah,I see you love C!
Hi Edward.
Hi Phil.
	Phil,I see you love Python!
```
>创建一个列表，其中包含要收到打印消息的朋友。
>
>在循环中，打印每个人的名字，并检查当前的名字是否在列表`friends`中。
>
>如果在，就打印一句特殊的问候语，其中包含这位朋友喜欢的语言。
>
>为获悉朋友喜欢的语言，我们使用了字典名，并将变量`name`的当前值作为键。

还可使用方法`keys()`确定某个人是否接受了调查:
```
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
---
Erin, please take our poll!
```
>方法`keys()`并非只能用于遍历：
>
>实际上，它返回一个列表，其中包含字典中的所有键。
>
>因此代码核实`'erin'`是否包含在这个列表中。因为她并不包含在这个列表中，所以打印一条消息，邀请她参加调查。

### 按特定顺序遍历字典中的所有键

要以特定顺序返回元素，一种办法是在`for`循环中对返回的键进行排序。

为此，可使用函数`sorted()`来获得按特定顺序排列的键列表的副本：
```
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for name in sorted(favorite_languages.keys()): 
    print(f"{name.title()}, thank you for taking the poll.")
    
---
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
```

### 遍历字典中的所有值

如果主要对字典包含的值感兴趣，可使用方法`values()`来返回一个值列表，不包含任何键。

>获得一个列表，其中只包含被调查者选择的各种语言，而不包含被调查者的名字：
>
>`for`语句提取字典中的每个值，并将其依次赋给变量`language`。通过打印这些值，就获得了一个包含被调查者所选择语言的列表：

```
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
---
The following languages have been mentioned:
Python
C
Ruby
Python
```
>这种做法提取字典中所有的值，而没有考虑是否重复。
>
>涉及的值很少时，这也许不是问题，但如果被调查者很多，最终的列表可能包含大量重复项。
>
>为剔除重复项，可使用集合`set`。集合中的每个元素都必须是独一无二的：

```
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    } 
print("The following languages have been mentioned:") 
for language in set(favorite_languages.values()): 
    print(language.title())
    
---
The following languages have been mentioned:
Ruby
Python
C
```
>通过对包含重复元素的列表调用`set()`，可让Python找出列表中独一无二的元素，并使用这些元素来创建一个集合。
>
>使用`set()`来提取`favorite_languages.values() `中不同的语言。结果是一个不重复的列表，其中列出了被调查者提及的所有语言。

## 嵌套

将字典存储在列表中，或将列表作为值存储在字典中，称为**嵌套**。

可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

### 字典列表

>创建一个包含三个外星人的列表：

```
alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15}  
aliens = [alien_0, alien_1, alien_2] 
for alien in aliens:
    print(alien)
    
---
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
```
>首先创建三个字典，其中每个字典都表示一个外星人。然后将这些字典都存储到一个名为`aliens`的列表中。最后，遍历这个列表，并将每个外星人都打印出来。

>示例，使用`range()`生成30个外星人：
```
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)
    
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print(f"Total number of aliens:{len(aliens)}")

---
{'color': 'green', 'points': '5', 'speed': 'slow'}
{'color': 'green', 'points': '5', 'speed': 'slow'}
{'color': 'green', 'points': '5', 'speed': 'slow'}
{'color': 'green', 'points': '5', 'speed': 'slow'}
{'color': 'green', 'points': '5', 'speed': 'slow'}
...
Total number of aliens:30
```
>首先创建一个空列表，用于存储接下来将创建的所有外星人。
>
>`range()`返回一系列数，告诉Python要重复这个循环多少次。每次执行这个循环时，都创建一个外星人，并将其附加到列表`aliens`末尾。
>
>使用一个切片来打印前5个外星人。
>
>打印列表的长度，以证明确实创建了30个外星人。

******

>使用`for`循环和`if`语句来修改某些外星人的颜色。例如，要将前三个外星人修改为黄色、速度为中等且值10分：
```
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':'5','speed':'slow'}
    aliens.append(new_alien)
    

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow',
        alien['speed'] = 'medium',
        alien['points'] = 10

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

---
{'color': ('yellow',), 'points': 10, 'speed': ('medium',)}
{'color': ('yellow',), 'points': 10, 'speed': ('medium',)}
{'color': ('yellow',), 'points': 10, 'speed': ('medium',)}
{'color': 'green', 'points': '5', 'speed': 'slow'}
{'color': 'green', 'points': '5', 'speed': 'slow'}
...
```

>进一步扩展这个循环，在其中添加一个`elif`代码块，将黄色外星人改为移动速度快且值15分的红色外星人：

```
for alien in aliens[0:3]: 
    if alien['color'] == 'green': 
        alien['color'] = 'yellow' 
        alien['speed'] = 'medium' 
        alien['points'] = 10 
    elif alien['color'] == 'yellow': 
        alien['color'] = 'red' 
	alien['speed'] = 'fast'
	alien['points'] = 15
```

### 在字典中存储列表

有时候，需要将列表存储在字典中，而不是将字典存储在列表中。 

例如，如果使用列表，只能存储要添加的比萨配料；但如果使用字典，就不仅可在其中包含配料列表，还可包含其他有关比萨的描述。

```
# 存储所点披萨的信息
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}
# 概述所点的披萨
print (f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
    
---
You ordered a thick-crust pizzawith the following toppings:
	mushrooms
	extra cheese
```
******
```
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name,languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
	
---
Jen's favorite languages are:
	Python
	Ruby
Sarah's favorite languages are:
	C
Edward's favorite languages are:
	Ruby
	Go
Phil's favorite languages are:
	Python
	Haskell
```

### 在字典中存储字典

```
users = {
    'aeinstein':{
        'first':'albert',
        'last': 'einstein', 
        'location': 'princeton', 
        }, 
    'mcurie': { 
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris', 
        }, 
    } 
for username, user_info in users.items(): 
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}" 
    location = user_info['location'] 
    print(f"\tFull name: {full_name.title()}") 
    print(f"\tLocation: {location.title()}")
    
---

Username: aeinstein
	Full name: Albert Einstein
	Location: Princeton

Username: mcurie
	Full name: Marie Curie
	Location: Paris
```
