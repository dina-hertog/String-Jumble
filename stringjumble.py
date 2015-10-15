"""
stringjumble.py
Author: Dina
Credit: Me and Jazzy and Anoushka

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text = input("Please enter a string of text (the bigger the better): ")
print('You entered "' + text + '". Now jumble it: ')

#part 1 (in reverse)
print(text[::-1])

#part 2 (words right)
words = text.split(" ")
print (' '.join(words[::-1]))

#part 3
a= len(words)
b= 0
while int(b) < int(a):
    word = words[int(b)]
    print(word[::-1], end= " ")
    b = int(b)+1


