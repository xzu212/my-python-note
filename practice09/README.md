- [练习1：Python学习笔记](https://github.com/xzu212/my-python-note/blob/main/practice09/learning_python.py)

> 在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，其中每一行都以“In Python you can”打头。将这个文件命名为	 learning_python.txt，并存储到为完成本章练习而编写的程序所在的目录中。编写一个程序，它读取这个文件，并将你所写的内容打印三次：第一次打	 印时读取整个文件；第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with代码块外打印它们。

- [练习2：C语言学习笔记](https://github.com/xzu212/my-python-note/blob/main/practice09/practice2.py)

> 你可使用方法 `replace()` 将字符串中的特定单词都替换为另一个单词。下面是一个简单的示例，演示了如何将句子中的 'dog' 替换为 'cat' ：
> ```
> >>> message = "I really like dogs."
> >>> message.replace('dog', 'cat')
> 'I really like cats.'
> ```
>读取你刚创建的文件 learning_python.txt 中的每一行，将其中的 Python 都替换为另一门语言的名称，如 C。将修改后的各行都打印到屏幕上。

- [练习3：访客](https://github.com/xzu212/my-python-note/blob/main/practice09/practice3.py)

> 编写一个程序，提示用户输入其名字；用户做出响应后，将其名字写入到文件 guest.txt 中。

- [练习4：访客名单](https://github.com/xzu212/my-python-note/blob/main/practice09/practice4.py)

> 编写一个 while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印问候语，并将一条到访记录添加到文件 guest_book.txt 中。确保这个文件中的每条记录都独占一行。

- [练习5：调查](https://github.com/xzu212/my-python-note/blob/main/practice09/practice5.py)

> 编写一个 while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。

- [练习6：加法运算](https://github.com/xzu212/my-python-note/blob/main/practice09/practice6.py)

> 提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。在这种情况下，当你尝试将输入转换为整数时，将引发 ValueError 异常。编写一个程序，提示用户输入两个数，再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获 ValueError 异常，并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数，再输入一些文本而不是数。

- [练习7：加法计算器](https://github.com/xzu212/my-python-note/blob/main/practice09/practice7.py)

> 将你为完成练习6而编写的代码放在一个 while 循环中，让用户犯错（输入的是文本而不是数）后能够继续输入数。

- [练习8：猫和狗](https://github.com/xzu212/my-python-note/blob/main/practice09/practice8.py)

>创建两个文件 cats.txt 和 dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不存在时捕获 FileNotFound错误，并打印一条友好的消息。将文件之一移到另一个地方，并确认 except 代码块中的代码将正确地执行。

- [练习9：静默的猫和狗](https://github.com/xzu212/my-python-note/blob/main/practice09/practice9.py)

>修改你在练习 8 中编写的 except 代码块，让程序在文件不存在时静默失败。

- [练习10：常见单词](https://github.com/xzu212/my-python-note/blob/main/practice09/practice10.py)

> 访问古登堡计划(http://gutenberg.org/) ，并找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。你可使用方法 count() 来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算 'row' 在一个字符串中出现了多少次：
> ```
> >>> line = "Row, row, row your boat"
> >>> line.count('row')
> 2
> >>> line.lower().count('row')
> 3
> ```
> 请注意，通过使用 lower() 将字符串转换为小写，可捕捉要查找的单词的各种外观，而不管其大小写格式如何。
>编写一个程序，它读取你在古登堡计划中获取的文件，并计算单词'the'在每个文件中分别出现了多少次。这里计算得到的结果并不准确，因为将诸如'then'和'there'等单词也计算在内了。请尝试计算'the '（包含空格）出现的次数，看看结果相差多少。

- 练习11：喜欢的数[11-1](https://github.com/xzu212/my-python-note/blob/main/practice09/practice11-1.py)/[11-2](https://github.com/xzu212/my-python-note/blob/main/practice09/practice11-2.py)

> 编写一个程序，提示用户输入他喜欢的数，并使用 json.dump() 将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It’s _____.”。

- [练习12：记住喜欢的数](https://github.com/xzu212/my-python-note/blob/main/practice09/practice12.py)

>将练习 11 中的两个程序合而为一。如果存储了用户喜欢的数，就向用户显示它；否则提示用户输入他喜欢的数并将其存储到文件中。运行这个程序两次，看看它是否像预期的那样工作。

- [练习13：验证用户](https://github.com/xzu212/my-python-note/blob/main/practice09/practice13.py)

>最后一个 remember_me.py 版本假设用户要么已输入其用户名，要么是首次运行该程序。应修改这个程序，以应对这样的情形：当前和最后一次运行该程序的用户并非同一个人。为此，在greet_user() 中打印欢迎用户回来的消息前，询问他用户名是否是对的。如果不对，就调用 get_new_username() 让用户输入正确的用户名。
