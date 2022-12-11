# Input a sentance and reverse it

words = input("Enter a word or sentance: ")

reverseWord = ""

for i in words:
    reverseWord = i + reverseWord

print(reverseWord)
