12
#Second Python Program
##Created to UMGC DATA 620 by Dr. George Cross
# George Cross
#This program computes gross pay
##
print("My second program to calculate the gross pay")
print ("Ask the user to enter values:")
print() #blank
hours=input("Enter number of hours: ")
#convert input from default string value to integer
intHours=int(hours)
rate=input("Enter rate of Pay: ")
#convert input from default string value to float
floatRate=float(rate)
#round the computation to two decimal places
grossPay=round((intHours * floatRate),2)
#Print the result for Gross Pay
print("Gross Pay is (No Overtime): $" + str(grossPay))
print() # blank
print("See data types:")
print(type(hours))
print(type(intHours))
print(type(rate))
print(type(floatRate))
print(type(grossPay))