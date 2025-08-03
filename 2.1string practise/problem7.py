""" Reverse A String in Python
Problem Statement
We need to write a Python program that takes a string s and prints the reverse of that string. For example:

Input: "geek"
Output: "keeg"

Input: "abcd"
Output: "dcba"

Input: "a"
Output: "a" """

s='abcd'
rev=""


# approach: 1
""" for i in s:
    rev=i+rev

print(rev) """

print(s[::-1]) #using slice operation


