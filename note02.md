# 列表简介

## 什么是列表

列表 由一系列按特定顺序排列的元素组成。   

在Python中，用方括号`[]`表示列表，并用逗号分隔其中的元素。

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles)

---

['trek', 'cannondale', 'redline', 'specialized']
```

### 访问列表元素

列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置告诉Python即可。  

要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在方括号内。

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles[0])

---

trek
```

### 索引从0而不是1开始

在Python中，第一个列表元素的索引为0，而不是1。第二个列表元素的索引为1。

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles[1]) 
print(bicycles[3])

---

cannondale 
specialized
```

Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为`-1` ，可让Python返回最后一个列表元素。  

这种语法很有用，因为经常需要在不知道列表长度的情况下访问最后的元素。  

这种约定也适用于其他负数索引。例如，索引`-2`返回倒数第二个列表元素，索引`-3`返回倒数第三个列表元素，依此类推。

### 使用列表中的各个值

可以像使用其他变量一样使用列表中的各个值。例如，可以使用`f字符串`根据列表中的值来创建消息。

```
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
message = f"My first bicycle was a {bicycles[0].title()}." 
print(message)

---

My first bicycle was a Trek.
```

## 修改、添加和删除元素

### 修改元素列表
修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
```
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
motorcycles[0] = 'ducati' 
print(motorcycles)

---

['honda', 'yamaha', 'suzuki'] 
['ducati', 'yamaha', 'suzuki']
```

### 在列表中添加元素

1. 在列表末尾添加元素
* 在列表中添加新元素时，最简单的方式是将元素附加(`append`)到列表。给列表附加元素时，它将添加到列表末尾。
```
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 

motorcycles.append('ducati') 
print(motorcycles)

---

['honda', 'yamaha', 'suzuki'] 
['honda', 'yamaha', 'suzuki', 'ducati']
```

* 可以先创建一个空列表，再使用一系列函数调用`append()`来添加元素。
```
motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki') 
print(motorcycles)

---

['honda', 'yamaha', 'suzuki']
```

2. 在列表中插入元素

使用方法`insert()`可在列表的任何位置添加新元素。为此，需要指定新元素的索引和值。

```
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') 
print(motorcycles)

---

['ducati', 'honda', 'yamaha', 'suzuki']
```
示例中，`'ducati'`被插入到列表开头。方法`insert()`在索引0处添加空间，并将值`'ducati'`存储到这里。  
这种操作将列表中已有的每个元素都右移一个位置。

### 从列表中删除元素

1. 使用`del`语句删除元素

- 如果知道要删除的元素在列表中的位置，可使用`del`语句。

```
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
del motorcycles[0] 
print(motorcycles)

---

['honda', 'yamaha', 'suzuki'] 
['yamaha', 'suzuki']
```

使用`del`可删除任意位置处的列表元素，条件是知道其索引。

```
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
del motorcycles[1] 
print(motorcycles)

---

['honda', 'yamaha', 'suzuki'] 
['honda', 'suzuki']
```

在这两个示例中，使用`del`语句将值从列表中删除后，就无法访问了。

2. 使用方法`pop()`删除元素

方法`pop() `删除列表**末尾**的元素，并让你能够接着使用它。

```
motorcycles = ['honda','yamaha','suzuki'] 
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

---

['honda','yamaha','suzuki']
['honda','yamaha']
suzuki
```

3. 弹出列表中任何位置处的元素

可以使用`pop()`来删除列表中任意位置的元素，只需在圆括号中指定要删除元素的索引即可。

```
motorcycles = ['honda', 'yamaha', 'suzuki']
first = motorcycles.pop(0)
print(f"My first motorcycle was {first.title()}.")

---

My first motorcycle was Honda.
```
每当使用`pop()`时，被弹出的元素就不再在列表中。

如果不确定该使用`del`语句还是`pop()`方法，下面是一个简单的判断标准：  

如果要从列表中删除一个元素，且不再以任何方式用它，就使用`del`语句；  
如果要在删除元素后还能继续使用它，就使用方法`pop()`。

4. 根据数值删除元素

有时候，不知道要从列表中删除的值所处的位置。如果只知道要删除的元素的值，可使用方法`remove()`。
```
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles))

---

['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```
使用`remove()`从列表中删除元素时，也可接着使用它的值。
```
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")

---

['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
A Ducati is too expensive for me.
```

##  组织列表

在列表中，元素的排列顺序常常无法预测，因为你并非总能控制数据的顺序。有时候，希望保留列表元素最初的排列顺序，而有时候又需要调整排列顺序。

### 使用方法`sort()`对列表永久排序

```
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

---

['audi', 'bmw', 'subaru', 'toyota']
```

方法`sort()`**永久性**地修改列表元素的排列顺序。

还可以按与字母顺序相反的顺序排列列表元素，只需向`sort()`方法传递参数`reverse=True`即可。

```
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

---

['toyota', 'subaru', 'bmw', 'audi']
```

### 使用函数`sorted()`对列表临时排序

要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数`sorted()`。函数`sorted()`能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。

```
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))

---

Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']
```

如果要按与字母顺序相反的顺序显示列表，也可向函数`sorted()`传递参数`reverse=True`。

### 倒着打印列表

要反转列表元素的排列顺序，可使用方法`reverse()`。

```
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

---

['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```
`reverse()`不是按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序。

方法`reverse()`永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，只需对列表再次调用`reverse()`即可。

### 确定列表的长度

使用函数`len()`可快速获悉列表的长度。
```
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars) 
4
```
