import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.fft import rfft, rfftfreq
# just seeing if this shows up as a change



#df_imported = pd.read_csv("~/Documents/OneDrive - Oklahoma A and M System/Research/Infrasound/GLINDA and Brandons work/testingmic.csv")
df_imported = pd.read_csv("~/Documents/Github/GLINDA2_testing/testing_misc_archived/testingmic.csv")
#df_imported = pd.read_csv("~/Documents/Github/GLINDA2_testing/testing_misc_archived/SYRINGE_attaching_initial8ml.csv")
mic_gain = 107  # gain-no units
mic_sensitivity = .000022   #V/Pa

# uncomment this if dealing with actual GLINDA data (doesnt have column titles)
#df_imported.columns = ['Time (s)', 'Signal (V)']

time = df_imported['Time (s)'].values
signal_ugly = df_imported['Signal (V)'].values
# signal = signal_ugly-np.mean(signal_ugly)
signal = signal_ugly
pressure_signal = signal*mic_gain/(mic_sensitivity)

firsttime = time[1]
lasttime = time[-1]
totaltime = lasttime-firsttime
N = int(len(time))
sample_rate = len(time)/(lasttime - firsttime)
print(sample_rate)
yf = rfft(signal)
xf = rfftfreq(N, 1/sample_rate)

# fig, (ax1, ax2) = plt.subplots(2)
# ax1.plot(time, signal)
# ax1.set_title('Raw Voltage vs Time')
# ax2.plot(time, pressure_signal)
# ax2.set_title('Pressure (Pa) (assuming sensitivity used is right) vs Time')



plt.plot(time, signal)
plt.show()

plt.semilogx(xf, np.abs(yf))
#plt.plot(xf[100:-1], np.abs(yf)[100:-1])
plt.grid()
plt.show()

# does this show?

#os.system('cd ~/Documents/Github/GLINDA2_testing; git add .; git commit -m "auto push from Pycharm code"; git push')

