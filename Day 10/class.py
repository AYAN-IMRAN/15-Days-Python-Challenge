class employee:
    languege = "Typescript" # This is a class attribute
    Salary = "120,000"

ayan = employee()
ayan.name = "Ahmed" # This is an Instance attribute

print(ayan.languege,ayan.name,ayan.Salary)

Aman = employee()
Aman.name = "Aman raza" # This is an Instance attribute
print(Aman.name,Aman.languege,Aman.Salary)


# Here name is instance attribute and salary and language are class attributes as they directly belong to the class