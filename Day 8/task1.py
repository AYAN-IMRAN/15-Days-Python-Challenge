
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c


a = int(input("Enter num 1 :"))
b = int(input("Enter num 2 :"))
c = int(input("Enter num 3 :"))

print(greatest(a,b,c))