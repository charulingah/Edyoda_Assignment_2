'''Write a Python program to print a dictionary whose keys should be the alphabet from a-z and 
the value should be corresponding ASCII values'''

#solution

as_dict= dict()
ascii_value = range(97,123)
for i in ascii_value:
    as_dict[chr(i)] =  i
print(as_dict)
