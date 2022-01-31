# Mic Recording Script
#HEY BRYCE!

from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1x15 import Mode
import adafruit_ads1x15.ads1115 as ADS

from time import time, sleep
import datetime
import board
import busio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.fft import rfft, rfftfreq

i2c = busio.I2C(board.SCL, board.SDA, frequency = 1000000)

ads = ADS.ADS1115(i2c)
ads.data_rate = 475
ads.gain = 1
ads.mode = Mode.CONTINUOUS

#change data_rate and gain if using ADS1115 package (should be)
# also investiage PGA (making custom gain based on analog input we havee
#adc.mode = Mode.CONTINUOUS   BW
chan = AnalogIn(ads, ADS.P0, ADS.P1) #differential voltage, channels 0 & 1 specified by JFA on his Github
s = 20 # seconds of recording

launch_time = datetime.datetime.now()
#timestr = launch_time.strftime("%Y_%m_%d_%H_%M_%S")
#micPath = "/home/pi/infrasound/dataFiles/micData" + timestr + ".csv"
#f = open(micPath,'a+')
dat = []
#looptime = time()
    #try:
print('Reading...\n')
start = time()
act_duration = 0.0000

while act_duration < s:
	time_oftrial = time()-start
	print(time(), chan.voltage)
	dat.append([time(), chan.voltage])
	act_duration = time_oftrial
	sleep(0.004)		# sleep set to make a sampling rate of 1/.004 = 250
data = pd.DataFrame(dat,columns = ['Time','Signal'])
print(data)
data.to_csv("testingmic.csv",header=['Time (s)','Signal (V)'])

# the rest of this is for printing natively in Python if needed (I don't use this really)
#print(data)
#time_BL = data['Time'].values
#sig_BL_ugly = data['Signal'].values
#sig_BL = sig_BL_ugly - np.mean(sig_BL_ugly)
#len_time = len(time_BL)


#last_time = time_BL[len_time-1]
#sample_rate = len_time/last_time
#N = int(sample_rate * last_time)


#yf = rfft(sig_BL)
#xf = rfftfreq(N, 1/sample_rate)

#plt.plot(time_BL, sig_BL_ugly)
#plt.show()

#plt.plot(time_BL, sig_BL)
#plt.show()

#plt.plot(xf, np.abs(yf))
#plt.grid()
#plt.show()

