#below application demonstate cretion series using pandas there are different way in which we can create series using pandas

import pandas as pd
import numpy as np

S=pd.Series()
print(S)

data=np.array(['a','b','c','d'])
S=pd.Series(data,index=[100,101,102,103])
print(S[100])

data={'a':0.1,'b':1.1,'c':2.1}
S=pd.Series(data)
print(S)

S=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(S['a'])