"""
2. Write a program to fill in a letter template given below with name and date.
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
''' 
"""
letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
''' 
print(letter.replace("<|Name|>","imran").replace("<|Date|>","12 dec,2025"))

# .replace chaining

