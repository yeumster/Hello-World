import numpy as np

scores = np.array([
    [7, 6, 5, 6, 10, 8, 8, 7],
    [5, 7, 7, 6, 9, 6, 8, 8],
    [9, 9, 9, 9, 8, 8, 10, 10],
    [5, 6, 6, 5, 10, 4, 5, 6],
    [8, 7, 7, 3, 7, 7, 8, 9]])

def mean(ascores):
    return np.mean(ascores)

def winsorize(ascores):
    sortscores = np.sort(ascores)
    sortscores[0] = sortscores[1]
    sortscores[-1] = sortscores[-2]
    return np.mean(sortscores)

for i in range(len(scores)):    
    print('Regular mean for athlete ' + str(i + 1) + ': '+ str(mean(scores[i])))
    print('Winsorized mean for athlete ' + str(i + 1) +  ': ' + str(winsorize(scores[i])) + '\n')

