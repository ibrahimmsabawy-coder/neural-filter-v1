import numpy as np
import matplotlib.pyplot as plt
number=np.linspace(0, 10 , 500)
clean_signal=np.sin(number)
gaussian_noise=np.random.normal(0, 0.1, clean_signal.shape)
messy_signal = clean_signal + gaussian_noise
window_size=5
filtered_signal=np.zeros(messy_signal.shape[0])
messy_signal.shape[0]   
for i in range(0, messy_signal.shape[0]):
    start_index = max(0, i - window_size)
    end_index = min(messy_signal.shape[0], i + window_size + 1)
    current_window= messy_signal[start_index:end_index]
    filtered_signal[i]=np.mean(current_window) 
plt.style.use('dark_background')
plt.figure(figsize = (20,10)) 
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.plot(number,messy_signal,'r',label = 'messy_signal',alpha=0.5)
plt.plot(number,filtered_signal,'b',linewidth=3 ,label = 'filtered_signal')
plt.xlabel('time(s)', fontsize = 20)
plt.ylabel('Amplitude', fontsize = 20)
plt.legend(fontsize = 15)
plt.title("Neural Signal Noise Filter", fontsize=24)
plt.show()