##import matplotlib.pyplot as plt
##x = list(range(13))
##plt.plot(x,[y**2 for y in x])
##plt.title('Some plot')
##plt.show()

##
##import matplotlib.pyplot as plt
##import numpy as np
##
##t = np.linspace(0, 4*np.math.pi,64)
##y = np.sin(t)
##
##plt.plot(t, y)
##plt.show()

##import matplotlib.pyplot as plt
##import numpy as np
##
##cond = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3])
##x = np.array([ 20, 40, 60, 80, 100, 20, 40, 60, 80, 100, 20, 40,
##60, 80, 100, 120])
##y = np.array([109, 98, 121, 88, 109, 115, 133, 117, 122, 131,
##133, 163, 153, 131, 159, 144])
##
##plt.plot(x[cond==1], y[cond==1],'b-', label = 'Cond 1')
##plt.plot(x[cond==2], y[cond==2],'m-', label = 'Cond 2')
##plt.plot(x[cond==3], y[cond==3],'k-', label = 'Cond 3')
##
##plt.title('Response time by condition')
##plt.xlabel('Onset time (s)')
##plt.ylabel('Response time (ms)')
##plt.axis([10,130,85,175])
##plt.legend(loc=4)
##
##plt.show()

##import numpy as np
##import matplotlib.pyplot as plt
##
##meanData = np.array([20, 35, 30, 35, 27])
##stdData = np.array([2, 3, 4, 1, 2])
##x = np.arange(1,6)
##
### just plotting bars
##plt.bar(x, meanData, 0.4, yerr=stdData, color='m')
##plt.xlabel('Groups')
##plt.ylabel('Scores')
##plt.title('Scores by groups')
##plt.xticks(x, ['Patients', 'Controls', 'Parents', 'Siblings', 'Placebo'])
##plt.show()

import numpy as np
import matplotlib.pyplot as plt

# data to be plotted
meanCong = np.array([33, 44, 52, 48])
sdCong = np.array([8, 9.1, 10.1, 8.8])
meanIncong = np.array([28, 48, 51.3, 46.5])
sdIncong = np.array([7.2, 9.2, 9.6, 8.4])
meanMixed = np.array([31.3, 40.8, 47.8, 47.2])
sdMixed = np.array([7.8, 8.3, 9.1, 7.8])


# paramters
bar_width = 0.2
x = np.arange(len(meanCong))

# plotting bars
plt.bar(x, meanCong, bar_width, yerr=sdCong, color='r', label='Congruent')
plt.bar(x+bar_width, meanIncong, bar_width, yerr=sdIncong, color='b', label='Incongruent')
plt.bar(x+2*bar_width, meanMixed, bar_width, yerr=sdMixed, color='m', label='Mixed')

# formatting and labeling the axes and title
plt.xlabel('Task')
plt.ylabel('Scores')
plt.title('Scores by tasks')
plt.xticks(x+bar_width, ['Task 1', 'Task 2', 'Task 3', 'Task4'])
plt.legend(loc=2)

# and we are done!
plt.show()
