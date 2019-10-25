##subject = {'age':23, 'hand':'right','glasses':'yes'}
##
##subject['RT'] = 235
##del subject['hand'] 
##print(subject)


respTime = {'congruent':132, 'incongruent':250, 'mixed':189}

avg = 0.0

for values in respTime.values():
    avg += values
avg /= len(respTime)

respTime['average'] = avg

print(respTime)

##
##inventory = {
## 'computer': 5,
## 'centrifuge': 4,
## 'freezer': 1,
## 'incubator': 2,
## 'microscope': 2
##}
##unitPrice = {
## 'computer': 1800,
## 'centrifuge': 2000,
## 'freezer': 1300,
## 'microscope': 4500,
## 'refrigerator': 1800,
## 'incubaror': 500,
## 'scale': 400,
## 'spectrometer': 2100
##}
##
##totalEstValue = {}
##
##for item in unitPrice.keys():
##    totalEstValue.setdefault(item, unitPrice[item])
##    if item in inventory:
##        totalEstValue[item] *= inventory[item]
##
##print(totalEstValue)
