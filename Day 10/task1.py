class Programmer :
    company = "Microsoft"
    def __init__(self ,name ,salary,code):
        self.name = name
        self.salary = salary
        self.code = code


p = Programmer("Ayan",120000,5674)
print(f"your name is {p.name} and Salary is ,{p.salary},and your pin is {p.code} and Company is ,{p.company}")
