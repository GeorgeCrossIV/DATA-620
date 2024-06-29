#Second Python Program
##Created to UMGC DATA 620 by Dr. George Cross
# George Cross
#This program computes gross pay with while
##
import sys
print("My second program to calculate the gross pay with LOOP and Try")
print() #blank
## Re-write with try and except
while True:
    hours=input("Enter number of hours: or done ")
    if hours == 'done':
        break
    else:
        try:
            print("My program to calculate the gross pay with Try")
            print() #blank
            #convert input from default string value to integer
            intHours=int(hours)
            rate=input("Enter rate of Pay: ")
            #convert input from default string value to float
            floatRate=float(rate)
            #round the computation to two decimal places
            grossPay=round((intHours * floatRate),2)
            #Print the result for Gross Pay
            #print(f"Gross Pay is (No Overtime): ${grossPay:,.2f}")
            print("Gross Pay is (No Overtime): ${0:,.2f}".format(grossPay))
            print() # blank
        except ValueError as err:
            print('Input must be numeric\n' + str(err))
            print() # blank