subject1 = int(input("enter your english marks: "))
subject2 = int(input("enter your Math marks: "))
subject3 = int(input("enter your Computer marks: "))


percentage = (100*(subject1 + subject2 + subject3 ))/300

if(percentage>= 40 and subject1>=33 and subject2>=33 and  subject3>=33):
    print("you are Certified ", percentage)

else:
    print("you are fail try Next time", percentage)
    