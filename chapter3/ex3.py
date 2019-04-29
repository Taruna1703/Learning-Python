#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
score = input('Enter the score between 0.00-1.00')
try:
    score = float(score)
    if score < 1:
        if score >= 0.9 :
            grade = 'A'
        elif score >= 0.8 :
            grade = 'B'
        elif score >= 0.7 :
            grade = 'C'
        elif score >= 0.6 :
            grade = 'D'
        elif score < 0.6 :
            grade = 'F'
        print('Grade : ',grade)
    else :
        print('Bad Score')    
except :
    print('Bad Score')
