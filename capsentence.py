# Input a sentence and capitalize every word.

sentence = input("Enter a sentence: ")

capSentence = ""
wordList = sentence.split()

for words in wordList:
    i = 0
    while i < len(words):
        if i == 0:
            capSentence = capSentence + " " + words[i].upper()
        else:
            capSentence = capSentence + words[i]
        i = i + 1


print(capSentence)
