#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
def computepay(hours,rate):
    hours=float(hours)
    rate=float(rate)
    if hours < 40 :
        pay = hours * rate
    if hours > 40 :
        increasedRate = 1.5 * rate
        pay = 40*rate + (hours-40)*increasedRate
    print(pay)
    return pay
x=input('Input hours')
y=input('Input rate')
computepay(x,y)
