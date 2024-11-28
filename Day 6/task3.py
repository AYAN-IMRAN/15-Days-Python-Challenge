msg1 = "Make a lot Money"
msg2 = "buy now"
msg3 = "Subscribe this"
msg4 = "like this"
msg5 = "click this"

User_msg  = input("enter your Sentence ;")

if((msg1 in User_msg) or (msg2 in User_msg) or (msg3 in User_msg) or (msg4 in User_msg) or (msg5 in User_msg)):
    print("This Sentence is Spam")
else:
        print("This Sentence is not Spam")