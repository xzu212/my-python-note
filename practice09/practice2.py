filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()
for line in lines:
    # 删除行尾的换行符，再将 Python 替换为 C。
    line = line.rstrip()
    print(line.replace('Python', 'C'))