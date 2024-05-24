file = open("Op.txt","w")
data = file.write("My name is prince kumar, i am from bihar patna.")
file.close()

file = open("Op.txt","r")
data = file.read()
print(data)
file.close()

file = open("Op.txt","a")
data = file.writelines("\nPython\nJava\nC\nC++\nPerl\nPHP")
print(data)
file.close()

file = open("Op.txt","r")
data = file.read()
print(data)
file.close()

file = open("Op.txt","r")
data = file.readline()
print(data)
file.close()

file = open("Op.txt","r")
data = file.readlines()
print(data)
file.close()

file = open("Op.txt","r")
data = file.read()
print(len(data))
file.close()

file = open("Op.txt","r")
data = file.readline()
print(len(data))
file.close()

file = open("Op.txt","r")
data = file.readlines()
print(len(data))
file.close()

file = open("Op.txt","r")
data = file.read()
words = data.split("p")
print(words)
print(len(words))
file.close()

"""

file = open("Op1.txt","w+")
data = file.write("i love programming language.")
print(data)
file = open("Op1.txt","r+")
data = file.read()
print(data)

"""