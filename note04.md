# if语句

## 一个示例

>假设有一个汽车列表，将其中汽车名称打印出来。对于大多数汽车，以首字母大写的方式打印其名称，但对于汽车名'bmw' ，以全大写的方式打印。
```
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())

---
Audi
BMW
Subaru
Toyota
```

## 条件测试

>每条`if`语句的核心都是一个值为`True`或`False`的表达式，这种表达式称为**条件测试**。
>
>Python根据条件测试的值为`True`还是`False`来决定是否执行`if`语句中的代码。
>
>如果条件测试的值为`True`，Python就执行紧跟在`if`语句后面的代码；如果为`False`，Python就忽略这些代码。
