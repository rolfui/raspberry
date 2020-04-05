import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


file_name = 'log-135146.txt'

M = np.loadtxt(file_name , delimiter=',' , encoding='utf-8')

t = M[:,0].astype('str')
t = [ i[8:14] for i in t]

co2 = M[:,1]
T1 = M[:,2]
T2 = M[:,3]
T3 = M[:,4]

# Plotting

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(t,co2)
plt.subplot(2,2,2)
plt.plot(t,T1)
plt.subplot(2,2,3)
plt.plot(t,T2)
plt.subplot(2,2,4)
plt.plot(t,T3)


plt.show()
