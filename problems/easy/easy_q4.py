# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
 
def check_number(num):
 
 
 
num = int(input("Enter the Number : "))
    if num < 0:
        print("Negative") 
        exit()
    elif num > 0:
        print("Positive")
        exit()  
    else:
        print("Number is negative")   
        exit()
 
  