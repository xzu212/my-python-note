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

Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1 ，可让Python返回最后一个列表元素。  

这种语法很有用，因为经常需要在不知道列表长度的情况下访问最后的元素。  

这种约定也适用于其他负数索引。例如，索引-2返回倒数第二个列表元素，索引-3返回倒数第三个列表元素，依此类推。

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
