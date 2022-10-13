name = input("What is your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)