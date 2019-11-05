# Creating data frame 
import numpy as np
import pandas as pd

# version 1 
infile = np.load('cryotherapyData.npz')
age = infile['age']
time = infile['time']
area = infile['area']
success = infile['success']

expData = pd.DataFrame()
expData['age']=age
expData['time']=time
expData['area']=area
expData['success']=success

# version two 
infile = np.load('CryotherapyData.npz')
cryoData = pd.DataFrame()
for iArray in list(infile.keys()):
    cryoData[iArray] = infile[iArray]
