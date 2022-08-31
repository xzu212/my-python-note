# 类

## 创建和使用类

大多数小狗都具备两项信息（名字和年龄）和两种行为（蹲下和打滚），我们的Dog类将包含它们。这个类让Python知道如何创建表示小狗的对象。编写这个类后，我们将使用它来创建表示特定小狗的实例。

### 创建`Dog`类

根据`Dog`类创建的每个实例都将存储名字和年龄，我们赋予了每条小狗蹲下`sit()`和打滚`roll_over()`的能力：

```
class Dog:
    """一次模拟小狗的简单测试。"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")
```

根据约定，在Python中，首字母大写的名称指的是类。这个类定义中没有圆括号，因为要从空白创建这个类。

***方法`__init__()`***

类中的函数称为方法。`__init__()`是一个特殊方法，每当根据Dog类创建新实例时，Python都会自动运行它。

在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。务必确保`__init__()`的两边都有两个下划线，否则使用类来创建实例时，将不会自动调用这个方法，进而引发难以发现的错误。 

此处方法`__init__()`定义成包含三个形参：`self`、`name`和`age`。

在这个方法的定义中，形参`self`必不可少，而且必须位于其他形参的前面。为何必须在方法定义中包含形参self呢？

因为Python调用这个方法来创建Dog实例时，将自动传入实参self。每个与实例相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。

创建Dog实例时，Python将调用Dog类的方法__init__()。我们将通过实参向Dog()传递名字和年龄，self会自动传递，因此不需要传递它。每当根据Dog 类创建实例时，都只需给最后两个形参（name和age）提供值。

定义两个变量都有前缀self。以self为前缀的变量可供类中的所有方法使用，可以通过类的任何实例来访问。

`self.name = name`获取与形参name相关联的值，并将其赋给变量name，然后该变量被关联到当前创建的实例。

`self.age = age`的作用与此类似。像这样可通过实例访问的变量称为属性。 

Dog类还定义了另外两个方法：`sit()`和`roll_over()`。 这些方法执行时不需要额外的信息，因此它们只有一个形参self。随后创建的实例能够访问这些方法，换句话说，它们都会蹲下和打滚。

当前，`sit()`和`roll_over()`所做的有限，只是打印一条消息，指出小狗正在蹲下或打滚。但可以扩展这些方法以模拟实际情况：如果这个类包含在一个计算机游戏中，这些方法将包含创建小狗蹲下和打滚动画效果的代码；如果这个类是用于控制机器狗的，这些方法将让机器狗做出蹲下和打滚的动作。

### 根据类创建实例

可将类视为有关如何创建实例的说明。Dog类是一系列说明，让Python知道如何创建表示特定小狗的实例。

```
class Dog: 
    --snip--
    
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

Python创建一条名字为'Willie'、年龄为6的小狗。遇到这行代码时，Python使用实参'Willie'和6调用Dog类的方法__init__()。

方法__init__()创建一个表示特定小狗的实例，并使用提供的值来设置属性`name`和`age`。接下来，Python返回一个表示这条小狗的实 例，而我们将这个实例赋给了变量`my_dog`。在这里，命名约定很有用：通常可认为首字母大写的名称(如Dog)指的是类，而小写的名称(my_dog)指的是根据类创建的实例。

1. 访问属性

要访问实例的属性，可使用句点表示法。访问`my_dog`的属性`name`的值：
```
my_dog.name
```
Python先找到实例`my_dog`，再查找与该实例相关联的属性`name`。在`Dog`类中引用这个属性时，使用的是`self.name`。
输出是有关my_dog的摘要：
```
My dog's name is Willie.
My dog is 6 years old.
```
2. 调用方法

根据Dog类创建实例后，就能使用句点表示法来调用Dog类中定义的任何方法了。下面来让小狗蹲下和打滚：
```
class Dog: 
    --snip--
    
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
```
要调用方法，可指定实例的名称(这里是`my_dog`)和要调用的方法，并用句点分隔。遇到代码`my_dog.sit()`时，Python在类Dog中查找方法`sit()`并运行其代码。Python以同样的方式解读代码`my_dog.roll_over()`。
```
Willie is now sitting.
Willie rolled over!
```
3. 创建多个实例

可按需求根据类创建任意数量的实例。下面再创建一个名为`your_dog`的小狗实例：
```
class Dog: 
    --snip--

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```
在本例中创建了两条小狗，分别名为Willie和Lucy。每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作：
```
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
```
即使给第二条小狗指定同样的名字和年龄，Python依然会根据Dog类创建另一个实例。你可按需求根据一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中，或者占用列表或字典的不同位置。

## 使用类和实例

### `Car`类

编写一个表示汽车的类。它存储了有关汽车的信息，还有一个汇总这些信息的方法：
```
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
```
* **定义方法`__init__()`。** 与前面的Dog类中一样，这个方法的第一个形参为`self`。该方法还包含另外三个形参：`make`、`model`和`year`。方法`__init__()`接受这些形参的值，并将它们赋给根据这个类创建的实例的属性。创建新的Car实例时，需要指定其制造商、型号和生产年份。
* **定义名为``get_descriptive_name() ``的方法。** 使用属性`year`、`make`和`model`创建一个对汽车进行描述的字符串，让我们无须分别打印每个属性的值。为在这个方法中访问属性的值，使用了`self.make`、`self.model`和`self.year`。

* 根据Car类创建了一个实例，并将其赋给变量`my_new_car`。调用方法`get_descriptive_name()`，指出我们拥有一辆什么样的汽车：

```
2019 Audi A4
```

### 给属性指定默认值

创建实例时，有些属性无须通过形参来定义，可在方法`__init__()`中为其指定默认值。 

>下面来添加一个名为`odometer_reading`的属性，其初始值总是为`0`。还添加一个名为`read_odometer()`的方法，用于读取汽车的里程表：

```
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

>创建一个名为`odometer_reading`的属性，并将其初始值设置为0。定义一个名为`read_odometer()`的方法，能够获悉汽车的里程。

```
2019 Audi A4
This car has 0 miles on it.
```

### 修改属性的值

1. 直接修改属性的值

要修改属性的值，最简单的方式是通过实例直接访问它。
>下面的代码直接将里程表读数设置为23：

```
class Car:
    --snip--

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

2. 通过方法修改属性的值

```
class Car: 
    --snip--
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```
添加方法`update_odometer()`。这个方法接受一个里程值，并将其赋给`self.odometer_reading`。
用`update_odometer()`，并向它提供了实参23(该实参对应于方法定义中的形参`mileage`)。它将里程表读数设置为23，而方法read_odometer()打印该读数：
```
2019 Audi A4
This car has 23 miles on it.
```

>对方法`update_odometer()`进行扩展，使其在修改里程表读数时做些额外的工作。下面来添加一些逻辑，禁止任何人将里程表读数往回调：
```
class:
    --snip--
    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值，禁止将里程表读数回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
```
现在，`update_odometer()`在修改属性前检查指定的读数是否合理。如果新指定的里程`mileage`大于或等于原来的里程`self.odometer_reading`，就将里程表读数改为新指定的里程；否则发出警告，指出不能将里程表往回调。

3. 通过方法对属性的值进行递增

有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设我们购买了一辆二手车，且从购买到登记期间增加了100英里的里程。下面的方法让我们能够传递这个增量，并相应地增大里程表读数：
```
class Car:
    --snip--
    
    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```
新增的方法`increment_odometer()`接受一个单位为英里的数，并将其加入`self.odometer_reading`中。创建一辆二手车`my_used_car`。调用方法`update_odometer()`并传入23_500，将这辆二手车的里程表读数设置为23 500。调用`increment_odometer()`并传入100 ，以增加从购买到登记期间行驶的100英里：
```
2015 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
```
