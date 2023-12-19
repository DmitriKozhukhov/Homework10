import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI1': lst})
rbt = []
hmn = []
for item in lst:
    if item == 'robot':
        rbt.append(1)
        hmn.append(0)
    else:
        rbt.append(0)
        hmn.append(1)
data['robot'] = rbt
data['human'] = hmn

print(data)



