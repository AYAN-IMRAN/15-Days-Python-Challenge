name = "ahmed"
 
nameshort = name[0:3]  # start from index 0 all the way till 3 (excluding 3)
print(nameshort)


name = "Ahmed"

print(name[0:3])

print(name[-4: -1])
print(name[1:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])


name = "Ahmed"

print(len(name))
print(name.endswith("med"))
print(name.startswith("Ah"))
print(name.capitalize())