# skip value in string
s1="abcdefghijklmnopqrstuvwxyz"
print(s1[0:26:2])

word="amazing"
print(word[:7])
print(word[0:])

# common escape sequence
st='welcome to geek\'s course'
print(st)
st1='hi\nwelcome to the course'
print(st1)
st2='hi\twelcome to the course'
print(st2)
st3="he said, \"welcome to the course\""
print(st3)

# creating raw string
sx=r'C:\project\name.py'
print(sx)
# Raw strings are created by prefixing 
# the string with r or R. This tells Python to treat backslashes as literal characters, not as escape characters.