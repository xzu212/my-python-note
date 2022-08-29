# 函数

函数是带名字的代码块，用于完成具体的工作。要执行函数定义的特定任务，可调用该函数。需要在程序中多次执行同一项任务时，无须反复编写完成该任务的代码，只需要调用执行该任务的函数，让Python运行其中的代码即可。

## 定义函数

```
def greet_user():
    """显示简单的问候语。"""
    print("Hello!")
    
greet_user()

---
Hello!
```

### 向函数传递信息

```
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello,{username.title()}!")
    
greet_user('jesse')

---
Hello,Jesse!
```

### 实参和形参

在函数`greet_user()`的定义中，变量`username`是一个形参(`parameter`)，即函数完成工作所需的信息。

在代码`greet_user('jesse')`中，值`'jesse'`是一个实参(`argument`)，即调用函数时传递给函数的信息。

在`greet_user('jesse')`中，将实参`'jesse'`传递给了函数`greet_user()`，这个值被赋给了形参`username`。

## 传递实参

函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。

向函数传递实参的方式很多：可使用位置实参，这要求实参的顺序与形参的顺序相同；也可使用关键字实参，其中每个实参都由变量名和值组成；还可使用列表和字典。

### 位置实参

调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。

为此，最简单的关联方式是基于实参的顺序。这种关联方式称为**位置实参**。

```
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster','harry')

---
I have a hamster.
My hamster's name is Harry.
```
 
1. **多次调用函数**

可以根据需要调用函数任意次。要再次描述，只需要再次调用即可：

```
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster','harry')
describe_pet('dog','willie')

---
I have a hamster.
My hamster's name is Harry.
I have a dog.
My dog's name is Willie.
```

### 关键字实参

关键字实参是传递给函数的名称值对。

因为直接在实参中将名称和值关联起来，所以向函数传递实参时不会混淆。

关键字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。

```
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type='hamster',pet_name='harry')

---
I have a hamster.
My hamster's name is Harry.
```

下面两个函数调用是等效的

```
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')
```

### 默认值

编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。

因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。

>例如，如果发现调用`describe_pet()`时，描述的大多是小狗，就可将形参`animal_type`的默认值设置为`'dog'`。这样，调用`describe_pet()`来描述小狗时，就可不提供这种信息：

```
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(pet_name='willie')

---
I have a dog.
My dog's name is Willie.
```
> 给形参`animal_type`指定了默认值`'dog'`，调用这个函数时，如果没有给`animal_type`指定值，Python就将把这个形参设置为`'dog'`。

### 等效的函数调用

```
def describe_pet(pet_name, animal_type='dog'):
```
>基于这种定义，在任何情况下都必须给`pet_name`提供实参。指定该实参时可采用位置方式，也可采用关键字方式。
>如果要描述的动物不是小狗，还必须在函数调用中给`animal_type`提供实参。同样，指定该实参时可以采用位置方式，也可采用关键字方式。

下面对这个函数的所有调用都可行：

```
# 一条名为Willie的小狗。 
describe_pet('willie') 
describe_pet(pet_name='willie') 
# 一只名为Harry的仓鼠。 
describe_pet('harry', 'hamster') 
describe_pet(pet_name='harry', animal_type='hamster') 
describe_pet(animal_type='hamster', pet_name='harry')
```

### 避免实参错误

提供的实参多于或少于函数完成工作所需的信息时，将出现实参不匹配错误。

## 返回值

函数可以处理一些数据，并返回一个或一组值。函数返回的值称为**返回值**。在函数中，可使用`return`语句将值返回到调用函数的代码行。
返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

### 返回简单值

```
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

---
Jimi Hendrix
```

### 让实参变成可选的

>扩展函数`get_formatted_name()`，使其同时处理中间名：

```
def get_formatted_name(first_name,middle_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

---
John Lee Hooker
```
>只要同时提供名、中间名和姓，这个函数就能正确运行。

并非所有的人都有中间名，但如果调用这个函数时只提供了名和姓，它将不能正确运行。

为了让中间名变成可选的，可给形参`middle_name`指定一个空的默认值，并在用户没有提供中间名时不使用这个形参。

为让`get_formatted_name()`在没有提供中间名时依然可行，可将形参`middle_name`的默认值设置为空字符串，并将其移到形参列表的末尾：

```
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

---
Jimi Hendrix
John Lee Hooker
```
调用这个函数时，如果只想指定名和姓，调用起来将非常简单。

如果还要指定中间名，就必须确保它是最后一个实参，这样Python才能正确地将位置实参关联到形参。

### 返回字典

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。

```
def build_person(first_name,last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name,'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

---
{'first': 'jimi', 'last': 'hendrix'}
```

>下面的修改让你能存储年龄：

```
def build_person(first_name,last_name,age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name,'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=27)
print(musician)

---
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
```

### 结合使用函数和while循环

>结合使用函数`get_formatted_name()`和`while`循环，以更正式的方式问候用户：

```
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 这是一个无限循环！
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello,{formatted_name}!")
```    
> 但这个`while`循环存在一个问题：没有定义退出条件。使用`break`语句提供退出循环的简单途径：

```
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello,{formatted_name}!")
    
---
    Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello,Eric Matthes!
Please tell me your name:
(enter 'q' at any time to quit)
First name: q
```

## 传递列表

将列表传递给函数后，函数就能直接访问其内容。

>示例：将包含名字的列表传递给一个名为`greet_users()`的函数，这个函数问候列表中的每个人：

```
def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello,{name.title()}!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

---
Hello,Hannah!
Hello,Ty!
Hello,Margot!
```

### 在函数中修改列表

将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的。

>举例：需要打印的设计存储在一个列表中，打印后将移到另一个列表中。下面是在不使用函数的情况下模拟这个过程的代码：

```
# 首先创建一个列表，其中包含一些需要打印的设计。
unpriented_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

# 模拟打印每个设计，知道没有未打印的设计为止。
# 打印每个设计后，都将其移到列表completed_models中。
while unpriented_designs:
    current_design = unpriented_designs.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型。
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

这个程序首先创建一个需要打印的设计列表，以及一个名为`completed_models`的空列表，每个设计打印后都将移到其中。

只要列表`unprinted_designs`中还有设计，`while`循环就模拟打印设计的过程：从该列表末尾删除一个设计，将其赋给变量`current_design`，并显示一条消息指出正在打印当前的设计，然后将该设计加入到列表`completed_models`中。循环结束后，显示已打印的所有设计：

```
Printing model:dodecahedron
Printing model:robot pendant
Printing model:phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```

重新组织这些代码，可编写两个函数，第一个函数负责处理打印设计的工作，第二个概述打印了哪些设计：

```
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都讲其移到列表completed_models中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
```

>函数`print_models()`，包含两个形参：一个需要打印的设计列表和一个打印好的模型列表。
>给定这两个列表，该函数模拟打印每个设计的过程：将设计逐个从未打印的设计列表中取出，并加入打印好的模型列表中。

>函数`show_completed_models()`，包含一个形参：打印好的模型列表。
>给定这个列表，函数`show_completed_models()`显示打印出来的每个模型的名称。

>主程序：

```
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
```

>创建一个未打印的设计列表，还创建一个空列表，用于存储打印好的模型。由于已经定义了两个函数，只需调用它们并传入正确的实参即可。
>调用print_models()并向它传递两个列表，print_models()模拟打印设计的过程。
>调用show_completed_models()，将打印好的模型列表传递给它，让其能够指出打印了哪些模型。

### 禁止函数修改列表

有时候，需要禁止函数修改列表。例如，假设像前一个示例那样，你有一个未打印的设计列表，并编写了一个函数将这些设计移到打印好的模型列表中。你可能会做出这样的决定：即便打印好了所有设计，也要保留原来的未打印的设计列表，以供备案。

但由于将所有的设计都移出了`unprinted_designs`，这个列表变成了空的，原来的列表没有了。为解决这个问题，可向函数传递列表的副本而非原件。这样，函数所做的任何修改都只影响副本，而原件丝毫不受影响。

要将列表的副本传递给函数，可以像下面这样做：

```
function_name(list_name_[:])
```

**切片表示法[:]创建列表的副本。** 如果不想清空未打印的设计列表，可像下面调用`print_models()`：

```
print_models(unpriented_designs[:],completed_models)
```
这样函数`print_models()`依然能够完成工作，因为它获得了所有未打印的设计的名称，但使用的是列表`unprinted_designs`的副本，而不是列表`unprinted_designs`本身。

像以前一样，列表`completed_models`也将包含打印好的模型的名称，但函数所做的修改不会影响到列表`unprinted_designs`。

虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由，否则还是应该将原始列表传递给函数。

这是因为让函数使用现成的列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。

## 传递任意数量的实参

Python允许函数从调用语句中收集任意数量的实参。

>例如：一个制作比萨的函数，它需要接受很多配料，但无法预先确定顾客要多少种配料。下面的函数只有一个形参`*toppings`，不管调用语句提供了多少实参，这个形参会将它们统统收入囊中：

```
def make_pizza(*toppings):
    """打印顾客点的所有配料。"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
```
**形参名`*toppings`中的星号让Python创建一个名为`toppings`的空元组，并将收到的所有值都封装到这个元组中。**

函数体内的函数调用`print()`通过生成输出，证明Python能够处理使用一个值来调用函数的情形，也能处理使用三个值来调用函数的情形。它以类似的方式处理不同的调用。注意，Python将实参封装到一个元组中，即便函数只收到一个值：

>将函数调用`print()`替换为一个循环，遍历配料列表并对顾客点的比萨进行描述：

```
def make_pizza(*toppings):
    """概述要制作的比萨。"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
```

不管收到一个值还是三个值，这个函数都能妥善处理：
```
Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushroom
- green peppers
- extra cheese
```

### 结合使用位置实参和任意数量实参

如果要让函数接受不同类型的实参，***必须在函数定义中将接纳任意数量实参的形参放在最后。***

Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

>例如，如果前面的函数还需要一个表示比萨尺寸的形参，必须将其放在形参`*toppings`的前面：

```
def make_pizza(size,*toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')
```

Python将收到的第一个值赋给形参size，并将其他所有值都存储在元组toppings中。在函数调用中，首先指定表示比萨尺寸的实参，再根据需要指定任意数量的配料：

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushroom
- green peppers
- extra cheese
```

### 使用任意数量的关键字实参

示例：创建用户简介：将收到有关用户的信息，但不确定会是什么样的信息。
在下面的示例中，函数`build_profile()`接受名和姓，还接受任意数量的关键字实参：

```
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
```

函数`build_profile()`的定义要求提供名和姓，同时允许根据需要提供任意数量的名称值对。

形参`**user_info`中的两个星号让Python创建一个名为`user_info`的空字典，并将收到的所有名称值对都放到这个字典中。

在这个函数中，可以像访问其他字典那样访问`user_info`中的名称值对。 

在`build_profile()`的函数体内，将名和姓加入了字典`user_info`中，因为总是会从用户那里收到这两项信息，而这两项信息没有放到这个字典中。接下来，将字 典user_info 返回到函数调用行。 我们调用build_profile() ，向它传递名（'albert' ）、姓 （'einstein' ）和两个键值对（location='princeton' 和 field='physics' ），并将返回的user_info 赋给变量 user_profile ，再打印该变量：

```
{'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```
