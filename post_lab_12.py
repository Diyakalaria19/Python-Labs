#question 1
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs1 = 5
fs2 = 10
f = 1000
t = np.linspace(0, 1, f, endpoint=False)
sine_wave1 = np.sin(2 * np.pi * fs1 * t)
sine_wave2 = np.sin(2 * np.pi * fs2 * t)
combined_signal = sine_wave1 + sine_wave2
plt.plot(t, combined_signal)
plt.title('Combined Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


#question 2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs1 = 5
fs2 = 10
f = 500
t = np.linspace(0,2,2*f, endpoint=False)
sine_wave = np.sin(2 * np.pi * fs1 * t)
cos_wave = np.sin(2 * np.pi * fs2 * t)
combined_signal = sine_wave*cos_wave
plt.plot(t, combined_signal)
plt.title('Combined Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


#question 3
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs= 5
f = 1000
t = np.linspace(0, 1, f, endpoint=False)
sine_wave = np.sin(2*np.pi* fs* t)
sine_wave_shifted=np.sin(2*np.pi*fs*(t-0.1))
plt.plot(t, sine_wave,label="Original")
plt.plot(t, sine_wave_shifted,label="Shifted")
plt.title('Original vs shifted')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()


#question 4
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs= 10
f = 1000
t = np.linspace(0, 1, f, endpoint=False)
sine_wave = np.sin(2*np.pi* fs* t)
scaled_wave = 3*sine_wave
plt.plot(t, sine_wave,label="Original")
plt.plot(t, scaled_wave,label="Scaled wave")
plt.title('Original vs scaled')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()


#question 5
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs= 5
f = 1000
t = np.linspace(0, 1, f, endpoint=False)
sine_wave = np.sin(2*np.pi* fs* t)
reversed_wave = sine_wave[::-1]
plt.plot(t, sine_wave,label="Original")
plt.plot(t, reversed_wave,label="Reversed wave")
plt.title('Original vs reversed')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
