##import numpy as np
##a = np.ones((5, 5))
##for i in range(1, 5):
##    a[i:, i:] = i+1
##print(a)

import numpy as np

RTMat = np.array([[111, 100,  86, 120,  91],
                  [ 92,  83, 105, 103, 112],
                  [117, 121, 124, 111, 110],
                  [111,  86, 113,  88, 105]])
scoreMat = np.array([[1, 0, 0, 0, 0],
                     [0, 1, 1, 0, 1],
                     [0, 1, 1, 0, 0],
                     [0, 0, 1, 1, 0]])

meanzero = np.mean(RTMat[scoreMat==0])
stdzero = np.std(RTMat[scoreMat==0])

meanone = np.mean(RTMat[scoreMat==1])
stdone = np.std(RTMat[scoreMat==1])


print('Score = 0: ')
print('Mean RT: ' + str(meanzero))
print('STD RT:' + str(stdzero))
print('\nScore = 1:')
print('Mean RT: ' + str(meanone))
print('STD RT: ' + str(stdone))
