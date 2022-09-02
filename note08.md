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

## 继承

编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，将自动获得另一个类的所有属性和方法。原有的类称为父类，而新类称为子类。子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。

### 子类的方法`__init__()`

在既有类的基础上编写新类时，通常要调用父类的方法`__init__()`。这将初始化在父类`__init__()`方法中定义的所有属性，从而让子类包含这些属性。

下面来模拟电动汽车。电动汽车是一种特殊的汽车，因此可在前面创建的Car类的基础上创建新类ElectricCar。这样就只需为电动汽车特有的属性和行为编写代码。

>创建`ElectricCar`类的一个简单版本，它具备`Car`类的所有功能：

```
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
```
>首先是`Car`类的代码。创建子类时，父类必须包含在当前文件中，且位于子类前面。接着，定义了子类` ElectricCar`。 
>定义子类时，必须在圆括号内指定父类的名称。方法`__init__()`接受创建Car实例所需的信息。
>**super()** 是一个特殊函数，让你能够调用父类的方法。这行代码让Python调用`Car`类的方法`__init__()`，让`ElectricCar`实例包含这个方法中定义的所有属性。父类也称为超类(superclass)，名称**super** 由此而来。
>我们创建一辆电动汽车，但提供的信息与创建普通汽车时相同。创建`ElectricCar`类的一个实例，并将其赋给变量`my_tesla`。这行代码调用`ElectricCar`类中定义的方法`__init__()`，后者让Python调用父类`Car`中定义的方法`__init__()`。我们提供了实参`'tesla'` 、`'model s' `和`2019`。

### 给子类定义属性和方法

让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了。 

>下面来添加一个电动汽车特有的属性(电瓶)，以及一个描述该属性的方法。我们将存储电瓶容量，并编写一个打印电瓶描述的方法：

```
class Car:
    --snip--

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```
>添加了新属性`self.battery_size`，并设置其初始值`75`，根据`ElectricCar`类创建的所有实例都将包含该属性，但所有`Car`实例都不包含它。
>还添加了一个名为`describe_battery`的方法，打印有关电瓶的信息。
>调用这个方法，将看到一条电动汽车特有的描述：

```
2019 Tesla Model S
This car has a 75-kWh battery.
```

对于`ElectricCar`类的特殊程度没有任何限制。模拟电动汽车时，可根据所需的准确程度添加任意数量的属性和方法。

如果一个属性或方法是任何汽车都有的，而不是电动汽车特有的，就应将其加入到`Car`类而非`ElectricCar`类中。

这样，使用`Car`类的人将获得相应的功能，而`ElectricCar`类只包含处理电动汽车特有属性和行为的代码。

### 重写父类的方法

对于父类的方法，只要它不符合子类模拟的实物的行为，都可以进行重写。为此，可在子类中定义一个与要重写的父类方法同名的方法。这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。

假设`Car`类有一个名为`fill_gas_tank()`的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。下面演示了一种重写方式：

```
class ElectricCar:
    --snip--
    
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
```
如果有人对电动汽车调用方法`fill_gas_tank()`，Python将忽略`Car`类中的方法`fill_gas_tank()`，转而运行上述代码。

### 将实例用作属性

使用代码模拟实物时，给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。可以将大型类拆分成多个协同工作的小类。

例如，不断给`ElectricCar`类添加细节时，我们可能发现其中包含很多专门针对汽车电瓶的属性和方法。在这种情况下，可将这些属性和方法提取出来，放到一个名为`Battery`的类中，并将一个`Battery`实例作为`ElectricCar`类的属性：
```
class Car:
    --snip--
    
class Battery:
    """一次模拟电动汽车点评的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """就打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', '2019')

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

定义一个名为`Battery`的新类，它没有继承任何类。方法`__init__()`除`self`外，还有另一个形参`battery_size`。这个形参是可选的：如果没有给它提供值，电瓶容量将被设置为75。方法`describe_battery()`也移到了这个类中。

在`ElectricCar`类中，添加了一个名为`self.battery`的属性。这行代码让Python创建一个新的`Battery`实例（因为没有指定容量，所以为默认值75），并将该实例赋给属性`self.battery`。每当方法`__init__()`被调用时，都将执行该操作，因此现在每个`ElectricCar`实例都包含一个自动创建的`Battery `实例。 

我们创建一辆电动汽车，并将其赋给变量`my_tesla`。描述电瓶时，需要使用电动汽车的属性`battery`：
```
my_tesla.battery.describe_battery()
```
这行代码让Python在实例`my_tesla`中查找属性`battery`，并对存储在该属性中的`Battery`实例调用方法`describe_battery()`。

输出与前面相同。

这看似做了很多额外的工作，但是现在想多详细地描述电瓶都可以，且不会导致`ElectricCar`类混乱不堪。下面再给`Battery`类添加一个方法，它根据电瓶容量报告汽车的续航里程：

```
class Car: 
    --snip--
    
class Battery: 
    --snip--
    
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range =260
        elif self.battery_size ==100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
        
class ElectricCar(Car):
    --snip--
    
my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```
新增的方法`get_range()`做了一些简单的分析：如果电瓶的容量为75 kWh，就将续航里程设置为260英里；如果容量为100 kWh，就将续航里程设置为315英里，然后报告这个值。为使用这个方法，也需要通过汽车的属性`battery`来调用。

输出指出了汽车的续航里程（这取决于电瓶的容量）：
```
2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.
```

## 导入类

随着不断给类添加功能，文件可能变得很长，即便妥善地使用了继承亦如此。Python允许将类存储在模块中，然后在主程序中导入所需的模块。

### 导入单个类

创建一个只包含`Car`类的模块。这让我们面临一个微妙的命名问题：在本章中已经有一个名为car.py的文件，但这个模块也应命名为car.py，因为它包含表示汽车的代码。我们将这样解决这个命名问题：将Car类存储在一个名为car.py的模块中，该模块将覆盖前面使用的文件car.py。从现在开始，使用该模块的程序都必须使用更具体的文件名，如my_car.py。下面是模块car.py，其中只包含Car类的代码：
```
"""一个可用于表示汽车的类"""

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

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值，
        禁止将里程表读数回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
 ```
 创建另一个文件`my_car.py`，在其中导入Car类并创建其实例：
 ```
 from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```
`import`语句让Python打开模块`car`并导入其中的Car 类。这样，我们就可以使用Car类，就像它是在这个文件中定义的一样。 输出与我们在前面看到的一样：
```
2019 Audi A4
This car has 23 miles on it.
```

### 在一个模块中存储多个类

可根据需要在一个模块中存储任意数量的类。Battery类和ElectricCar类都可帮助模拟汽车，下面将它们都加入模块`car.py`中：


