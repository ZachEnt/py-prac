# Takes in information and tells user how long till they die

name = input("Enter your name: ")
age = int(input("Enter your age: "))

yearsLeft = 100 - age

print("Hello " + name + ", you have", yearsLeft, "till you die!")
