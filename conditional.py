# else is written only one time in the last
# indentation is very important in python it is also known as proper spacing and works as using of {}
# nesting in python is done through proper spacing aka indentation

gpa = float(input("Enter your GPA:"))
iq = int(input("Enter your iq:"))

if(iq >= 200):
    if(gpa == 4.0):
        print("Your application is selected")
    else:
        print("Better luck next time")  
else:
    print("Increase your iq to minimum of 200")
    