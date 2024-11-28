s = set()

n = s.add(10)
n = s.add(10.0) # and if i change 10.0 to 10.1 his lenght is 3
n = s.add("10")

print(len(s))  # output is 2

s = {}  # is not type set this type is dictionary 

print(type(s)) # output is dict 
s = set()  #  this type is Dictonary 

print(type(s)) # output is set 