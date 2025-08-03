""" Pattern Searching in Python
Problem Statement
Given a large text and a smaller pattern, our task is to find all the indexes where the pattern occurs within the text. For example, if our text is "geeks for geeks" and our pattern is "geeks", the pattern appears at indexes 0 and 10. Therefore, our output should be [0, 10]. """

txt="geeks for geeks"
pat="geeks"

pos=txt.find(pat)

while pos>=0:
    print(pos)
    pos=txt.find(pat,pos+1)