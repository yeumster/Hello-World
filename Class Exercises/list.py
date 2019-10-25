##nameList = ['Sarah', 'Paul', 'Jill', 'Robert']
##
##while True:
##    name = input('Enter your name (enter End to stop program): ')
##
##    if name == 'End':
##        break
##    if name in nameList:
##        print('You are on the list.')
##    else:
##        print('You are added to the list')
##        nameList.append(name)
##
##print(nameList)

##mammal = ['cat', 'dog', 'cat', 'cat', 'tiger']
##print(mammal)
##print('Replace cat with lion: ')
##
##for i in range(len(mammal)):
##    if mammal[i] == 'cat':
##        mammal[i] = 'lion'
##
##print(mammal)

def update(cList):
    aList = cList.copy()

    while 'C' in aList: 
        aList[aList.index('C')] = 'A'
    return aList

exp1 = ['A','B','C','A','B','A','C','B','C','A','B']
exp2 = ['C','B','C','B','A','B']
exp3 = ['A','C','B','B','C','C','B','A','B','B']

print(update(exp1)) 
print(update(exp2)) 
print(update(exp3)) 

