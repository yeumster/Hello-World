##import os
##f = open(os.path.join('..','TestData','ExerciseData_OneLine.txt'), 'r')
##line = f.readline().strip()
##print(line)
##
##lineNumbers = line.split()
##
##inNumber = [int(i) for i in lineNumbers]
##
##trials = inNumber[0:3]
##onsetTime = inNumber[3:6]
##respTime = inNumber[6:9]
##score = inNumber[9:12]
##
##print(trials)
##print(onsetTime)
##print(respTime)
##print(score)
##f.close()

# state capital
##import os
##f = open(os.path.join('..', 'TestData', 'StateCapitalList.txt'), 'r')
##line = f.readline()
##while line:
##    location = line.strip().split(',')
##    print(location[1] + ' (' + location[0] + ')')
##    line = f.readline()
##
##f.close()

# id number
for i in range(1, 41):
    print('sub-%03d' % i) # or print('sub-' + '%03d' % i)

# state capitals revisited
##import os
##f = open(os.path.join('..', 'TestData', 'StateCapitalList.txt'), 'r')
##n = open('StateCapitals.txt', 'w')
##line = f.readline()
##print('Writing to new file StateCapitals.txt...')
##while line:
##    location = line.strip().split(',')
##    n.write(location[1] + ' (' + location[0] + ')\n')
##    line = f.readline()
##print('Finished writing to file.')
##
##f.close()
##n.close()
