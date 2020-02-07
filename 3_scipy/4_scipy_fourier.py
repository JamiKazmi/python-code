from scipy.fftpack import fft, ifft
import numpy as np

# fourier transform
x = np.array([1, 2, 3, 4])
y = fft(x)
print(y)

# inverse fourier transform
y = ifft(x)
print(y)
