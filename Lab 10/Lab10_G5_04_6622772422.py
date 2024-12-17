import numpy as np

data = np.loadtxt("TSV/sales.tsv", delimiter="\t", dtype=int)

mat = data[:,1:]

s = np.sum(mat, axis=1)
# print(s)

asd_ind = np.argsort(s)
# print(asd_ind)

asd_val = s[asd_ind]
# print(asd_val)

for i in range(1,len(s)+1):
    print(data[asd_ind[-i],0],s[asd_ind[-i]])