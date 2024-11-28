class employee:
    language = "Typescript" # This is a class attribute
    Salary = "120,000"

    def getdetail(self): # argument is important like a self without this is not work
        print(f"this is employee work language {self.language} and this is Salary {self.Salary}")

     @staticmethod
    def greet():
        print("Good morning")

ayan = employee()
ayan.language = "C++" # This is an Instance attribute
ayan.greet
ayan.getdetail()

# print(ayan.languege,ayan.Salary)
