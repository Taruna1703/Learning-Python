#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
hrs = input('Input Hours : ')
try:
    hrs = float(hrs)
    rate = input('Input Rate : ')
    try:
        rate= float(rate)
        if hrs <= 40 :
            pay = hrs * rate
        if hrs > 40 :
            increasedRate = 1.5 * rate
            pay = 40*rate + (hrs-40)*increasedRate
        print('Pay : ',pay)
    except :
        print('Error.Please enter a numeric value')
except :
    print('Error.Please enter a numeric value')
