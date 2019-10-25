##def repeatPhrase(phrase, num):
##    print((phrase + ' ')*int(num))
##
##repeatPhrase(input('Input a phrase: '), int(input('Input a number: ')))

##def metricConversion(feet, inches):
##    totalcm = float(feet)*30.48 + float(inches)*2.54
##    m = totalcm//100
##    cm = totalcm%100
##    return m, cm
##
##
##m, cm = metricConversion(float(input('Number of feet: ')), float(input('Number of inches: ')))
##print(str(m) + ' meters and ' + str(cm) + ' centimeters')
##


def randDice():
    from random import randint
    return randint(1,6), randint(1,6)

##print(str(randDice()))

one, two = randDice()
while(one != 1 or two != 1):
    print('(' + str(one) + ', ' + str(two) + ')')
    one,two = randDice()

print('(' + str(one) + ', ' + str(two) + ')')
