# Input a number and adds all the evens to the number

number = int(input("Enter a number: "))

answer = 0
i = 0
while i <= number:
    if i % 2 == 0:
        answer = answer + i
    i = i + 1

print(answer)
