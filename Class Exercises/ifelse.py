##truePassword = 'python is fun'
##attempt = str(input('Please input password: '))
##
##if(attempt == truePassword):
##    print('Correct password entered')
##else:
##    print('Invalid password')


weight = float(input('Enter weight in pounds: '))
height = float(input('Enter height in inches: '))

if (weight <= 300) and (height <= 78):
    print('Both requirements met')

elif weight <= 300:
    print('Weight requirement met')

elif height <= 78:
    print('Height requirement met')

else:
    print('Neither requirements met')
