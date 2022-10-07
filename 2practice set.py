letter=''' Dear <|NAME|>
You are selected
Greetings from ABC Code House. I am Happy to tell you about your selection .
Have a great day..!!
Thanks and Regard,
Alex

DATE:<|DATE|>
'''
name=input("Enter Your Name\n")
date=input("Enter Date\n")

letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>",date)
print(letter)