# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hrs = float(input('Input Hours : '))
rate = float(input('Input Rate : '))
if hrs < 40 :
    pay = hrs * rate
if hrs > 40 :
    increasedRate = 1.5 * rate
        pay = 40*rate + (hrs-40)*increasedRate
print('Pay : ',pay)
