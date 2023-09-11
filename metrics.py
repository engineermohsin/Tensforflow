import numpy as np
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import f1_score



arr1=np.array([1,3,4])
arr2=np.array([1,3,65])

print(f1_score(arr1, 'f1_nano'))

