# 文件和异常

## 从文件中读取数据

### 读取整个文件

要读取文件，需要一个包含几行文本的文件。下面首先创建一个文件，它包含精确到小数点后30位的圆周率值，且在小数点后每10位处换行：

- pi_digits.txt

```
3.1415926535
  8979323846
  2643383279
```

下面的程序打开并读取这个文件，再将其内容显示到屏幕上：

- file_reader.py

```
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
```

要以任何方式使用文件，都得先打开文件，才能访问它。函数`open()`接受一个参数：__要打开的文件的名称。__ 

Python在当前执行的文件所在的目录中查找指定的文件。当前运行的是`file_reader.py`，因此Python在`file_reader.py`所在的目录中查找`pi_digits.txt`。

函数`open()`返回一个表示文件的对象。在这里，`open('pi_digits.txt')`返回一个表示文件`pi_digits.txt`的对象，Python将该对象赋给`file_object`供以后使用。

关键字`with`在不再需要访问文件后将其关闭。在这个程序中，我们调用了`open()`，但没有调用`close()`。

也可以调用`open()`和`close()`来打开和关闭文件，但这样做时，如果程序存在bug导致方法close()未执行，文件将不会关闭。这看似微不足道，但未妥善关闭文件可能导致数据丢失或受损。如果在程序中过早调用`close()`，你会发现需要使用文件时它已关闭（无法访问），这会导致更多的错误。

并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可让Python去确定：你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。 

有了表示`pi_digits.txt`的文件对象后，使用方法`read()`读取这个文件的全部内容，并将其作为一个长长的字符串赋给变量contents。这样，通过打印`contents`的值，就可将这个文本文件的全部内容显示出来。

相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。因为`read()`到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。要删除多出来的空行，可在函数调用`print()`中使用`rstrip()`，`rstrip()`删除字符串末尾的空白。

```
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())
```

### 文件路径

将类似于`pi_digits.txt`的简单文件名传递给函数`open()`时，Python将在当前执行的文件（即.py程序文件）所在的目录中查找。

例如，你可能将程序文件存储在了文件夹`python_work`中，而该文件夹中有一个名为`text_files`的文件夹用于存储程序文件操作的文本文件。虽然文件夹`text_files`包含在文件夹`python_work`中，但仅向`open()`传递位于前者中的文件名称也不可行，因为Python只在文件夹`python_work`中查找，而不会在其子文件夹`text_files`中查找。

要让Python打开不与程序文件位于同一个目录中的文件，需要提供文件路径，让Python到系统的特定位置去查找。

由于文件夹`text_files`位于文件夹`python_work`中，可以使用相对文件路径来打开其中的文件。相对文件路径让Python到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。例如：

```
with open('text_files/filename.txt') as file_object:
```

这行代码让Python到文件夹`python_work`下的文件夹`text_files`中去查找指定的.txt文件。

__显示文件路径时，Windows系统使用反斜杠`\`而不是斜杠`/`，但在代码中依然可以使用斜杠。__

还可以将文件在计算机中的准确位置告诉Python，这样就不用关心当前运行的程序存储在什么地方了。这称为绝对文件路径。在相对路径行不通时，可使用绝对路径。例如，如果`text_files`并不在文件夹`python_work`中，而在文件夹`other_files`中，则向`open()`传递路径`text_files/filename.txt`行不通，因为Python只在文件夹`python_work`中查找该位置。为明确指出希望Python到哪里去查找，需要提供完整的路径。绝对路径通常比相对路径长，因此将其赋给一个变量，再将该变量传递给`open()`会有所帮助

```
file_path = '/home/ehmatthes/other_files/text_files/_filename_.txt' 
with open(file_path) as file_object:
```

通过使用绝对路径，可读取系统中任何地方的文件。就目前而言，最简单的做法是，要么将数据文件存储在程序文件所在的目录，要么将其存储在程序文件所在目录下的一个文件夹（如text_files）中。

__如果在文件路径中直接使用反斜杠，将引发错误，因为反斜杠用于对字符串中的字符进行转义。例如，对于路径`C:\path\to\file.txt`，其中的`\t`将被解读为制表符。如果一定要使用反斜杠，可对路径中的每个反斜杠都进行转义，如`C:\\path\\to\\file.txt`。__
