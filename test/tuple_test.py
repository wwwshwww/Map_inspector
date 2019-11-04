import numpy as np

t = np.zeros([5,2])
for i in range(len(t)):
    t[i] = (i,i*2)

print(t)

print(t[:,1])

tup = [(1,1), (2,2)]

tu = np.zeros_like(tup)
tu[1] = [3,3]
print(tu)