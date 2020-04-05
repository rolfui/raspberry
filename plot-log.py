import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


file_name = 'log-135146.txt'

M = np.loadtxt(file_name , delimiter=',' , encoding='utf-8')

x = M[:,0].astype('str')
x = [ i[8:14] for i in x]
#x = M[:,0].astype('int').astype('str')
#co2 = M[:,1].astype('int')

#x = M[:,0].astype(str)
co2 = M[:,1]
T1 = M[:,2]
T2 = M[:,3]
T3 = M[:,4]

# print(x)
# print(co2)
# print(T1)
# print(T2)

# Plotting

# Figure 1
fig1, axs = plt.subplots(2,2)
fig1.suptitle(file_name)

axs[0,0].plot(x,co2,'tab:green')
axs[0,0].set_title('CO2')
axs[0,0].set(ylabel='CO2 in ppm')

axs[0,1].plot(x,T1,'tab:red')
axs[0,1].set_title('Temperature 1')
axs[0,1].set(ylabel='degrees Celsius')

axs[1,0].plot(x,T2,'tab:orange')
axs[1,0].set_title('Temperature 2')
axs[1,0].set(ylabel='degrees Celsius')

axs[1,1].plot(x,T2,'tab:blue')
axs[1,1].set_title('Temperature 3')
axs[1,1].set(ylabel='degrees Celsius')

for ax in axs.flat:
    ax.xaxis.set_major_locator(ticker.LinearLocator(10))
    ax.xaxis.grid(which='both', color='grey')
    ax.yaxis.grid(which='both', color='grey')
    ax.set(xlabel='time')

# Figure 2
fig2, axs2 = plt.subplots(1,1)
fig2.suptitle(file_name + " CO2")

axs2.plot(x,co2, 'tab:green')
axs2.xaxis.set_major_locator(ticker.LinearLocator(10))
axs2.xaxis.grid(which='both', color='grey')
axs2.yaxis.grid(which='both', color='grey')
axs2.set(xlabel='time')
axs2.set(ylabel='CO2 in ppm')

# Figure 3
fig3, axs3 = plt.subplots(1,1)
fig3.suptitle(file_name + " Temperatures")

axs3.plot(x,T1,'tab:red')
axs3.plot(x,T2,'tab:orange')
axs3.plot(x,T3,'tab:blue')

axs3.xaxis.set_major_locator(ticker.LinearLocator(10))
axs3.xaxis.grid(which='both', color='grey')
axs3.yaxis.grid(which='both', color='grey')
axs3.set(xlabel='time')
axs3.set(ylabel='degrees Celsius')

# Showing the plots
fig1.show()
fig2.show()
fig3.show()
input()
plt.close('all')
