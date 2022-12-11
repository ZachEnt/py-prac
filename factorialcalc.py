# Input a number and recieve the factorial

userIn = int(input("Enter a number: "))

# Loop to achieve all factorial numbers
factorial = str(userIn) + ""
number = userIn
while number > 1:
    number = number - 1
    factorial = str(factorial) + " * " + str(number)


print("Factorial of", userIn, "is " + factorial)
