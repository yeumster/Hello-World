import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('fev.csv')

female = data[data.sex==0].drop('sex', axis=1)
male = data[data.sex==1].drop('sex', axis=1)

def plot(genderdata, gender):
    x = plt.figure()
    smoke = genderdata[genderdata.smoke==1]
    nosmoke = genderdata[genderdata.smoke==0]
    plt.scatter(smoke.age, smoke.fev, c='r', label='Smoker', marker='v')
    plt.scatter(nosmoke.age, nosmoke.fev, c='b', label='Non Smoker', marker='.')
    plt.xlabel('Age')
    plt.ylabel('FEV')
    plt.title('FEV Data For ' + gender)
    plt.legend(loc=2)
    x.show()

plot(female, 'Female')
plot(male, 'Male')
