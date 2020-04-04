import numpy as np
import matplotlib.pyplot as plt


file_name = 'log-232713.txt'

M = np.loadtxt(file_name , delimiter=',' , encoding='utf-8')
#x = M[:,0].astype('int').astype('str')
#co2 = M[:,1].astype('int')

x = M[:,0].astype(str)
co2 = M[:,1]
T1 = M[:,2]
T2 = M[:,3]

print(x)
print(co2)
print(T1)
print(T2)

# Plotting

plt.plot(x,co2)
plt.grid(which='both', color='grey')
plt.show()
