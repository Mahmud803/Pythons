# Checking Substrings using in Operator
s1="imran mahmud"
s2="imr"
print(s2 in s1)
print(s2 not in s1)

# String Concatenation using + Operator
s1="imran "
s2="mahmud"

s3=s1+s2
s4='welcome to ' + s3
print(s4)

print(s4)

print(s4)

# Finding Substring Position using index() Method

st="american_donkey"
st1="donkey"

print(st.index(st1))

print(st.index(st1,1))

print(st.index(st1,1,15))


# Finding Substring Position using rindex() Method

string="geeksforgeeks"

last_oc=string.rindex("geeks")
print(last_oc)

last_e=string.rindex('e')
print(last_e)

# 3. Find 'forge' starting from index 2
last_forge=string.rindex('forge',2)

# 4. Find 'ks' between index 0 and -2 (which is index 11)
last_ks=string.rindex("ks",0,-2)
print(last_ks)

# split() and join() Methods

sx="imran mahmud nothing"
print(sx.split())
print(sx.split(","))

l = ["geeksforgeeks", "python", "course"]
print(" ".join(l))
print(", ".join(l))


# strip(), lstrip(), and rstrip() Methods

s="---geeksforgeeks---"
print(s.strip("-"))
print(s.lstrip("-"))
print(s.rstrip("-"))