#module

def palin(s):
    if s.lower() == s[::-1].lower():
        print("The word is PALINDROME")
    else:
        print("Not PALINDROME!")

#main code

import Palindrome
str1 = input("Enter a string : ")
Palindrome.palin(str1)
