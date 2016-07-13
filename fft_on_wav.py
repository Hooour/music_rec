import numpy as np;
import scipy as sp;
import scipy.io.wavfile as wav;
import matplotlib.pyplot as plt;

wav_file_list = 'wav_list.txt';

r = 44100;
b = 10;

wav_list = open(wav_file_list);
M = np.zeros((1,r/2));
for file_name in wav_list:
	rate, data = wav.read(file_name.split('\n')[0]);
	print rate;
	print data.shape;
	data = np.sum(data, axis = 1)/data.shape[0];
	feature = np.fft.fft(data,r);
	feature[0] = 0;
	#temp = feature[range(r/2)];
	#feature[range(r/2)]=feature[range(r/2,r)];
	#feature[range(r/2,r)]=temp;
	#feature[range(r/2-b,r/2+b)]=0;
	feature = (feature[range(r/2)]+feature[range(r-1,r/2-1,-1)])/2;
	M = np.vstack((M,feature));
	#plt.plot(range(-r/2,r/2),np.real(feature));
	#plt.plot(range(-r/2,r/2),np.imag(feature));
	#plt.show();
M = M[1:];
print M.shape;
np.savetxt('wav_features.csv',M,delimiter=',');

