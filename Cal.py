# Calculating Using Class And Object.
class Cal:
    def __init__(self,x,y):
        self.a = x
        self.b = y
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
print(" : Calculator : ")
print("\n Choose Your Choice : \n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exit")
a = int(input("Enter 1 Number : "))
b = int(input("Enter 2 Number : "))
obj = Cal(a,b)
while(True):
    choice = int(input("Enter Your Choice : "))
    if(choice == 1):
        print("Addition is : ",obj.add())
    elif(choice == 2):
        print("Substraction is : ",obj.sub())
    elif(choice == 3):
        print("Addition is : ",obj.mult())
    elif(choice == 4):
        print("Addition is : ",obj.div())
        if(b != 0):
            print("Division is : ",round(obj.div()))
        else:
            print("Divison by zero is not Possible !")
    elif(choice == 5):
        print("Exited")
        break
    else:
        print("Invalid Choice !")

