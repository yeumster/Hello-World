last5Num = ['5463', '3342', '0980', '3342', '0021']

while True:
    newNum = int(input('Please enter a 4-digit extension: '))
    # casting as int ensure no non-digit numbers are inputted 
    if newNum == 0000:
        break
    
    strNum = str(newNum)
    # ensures input is 4 digits long
    if len(strNum) != 4:
        print('Invalid input.')
    else: 
        del last5Num[0]
        last5Num.append(strNum)
        print('Updated list: ')
        print(last5Num)

print('\nList: ')
print(last5Num) 
