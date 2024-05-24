import string
import cmath
str = "Life is what you make of it"
print(str[:])
print(str[-10:])
print(str[:-10])
print(str[-6:-1])
print(str[6:])
print(str[4:10:2])
print(str[:6])
print(str[3:9])
print(str[-1::-1])  #print(str[::-1])



a = int(input("Enter a number for A : "))
b = int(input("Enter a number for B : "))
c = int(input("Enter a number for C : "))
# calculating discriminant using formula.
dis = b * b - 4 * a * c
dis_val = cmath.sqrt(dis)
# checking condition for discriminant.
if(dis > 0):
    print("The root are Real and Distinct.")
    print((-b + dis_val) / (2 * a))
    print((-b - dis_val) / (2 * a))
elif(dis == 0):
    print("The Root are Real and Equal.")
    print(-b / (2 * a))
    # when discriminant is less than 0.
else:
    print("The Root are Imaginary and Complex.")
    print(-b / (2 * a), " +i", dis_val)
    print(-b / (2 * a), " -i", dis_val)


# Write in the File.
# file = open("Operation.txt",'x')
# file = open("Operation.txt",'a')
file = open("Operation.txt",'w')
file.write("Reva unniversity in bangalore.")
file.close()
# READING NUMBER OF LINES IN A FILE.
print("\nAfter Appending\n")
# APPENDING A DATA IN A FILE
file = open("Operation.txt", "a")
data = file.writelines("\n python programming \n perl programming \n web programming")
file.close()
# Read the File.
file = open("Operation.txt",'r')
data = file.read()
print(data)
print("The Number of Character is {}".format(len(data)))
file.close()
#Read the Lines.
file = open("Operation.txt", "r")
data = file.readlines()
print("Number of Lines in a File is {}".format(len(data)))
file.close()

dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'july', 8: 'August',9: 'September', 10: 'October', 11: 'November', 12: 'December'}
dict.update({13: 'Alex'})
dict.pop(13)
dict[13] = "Java"
print(dict)
dict.clear()
print(dict.keys())
print(dict.values())
print(dict.items())







