# Plotting A Sine Wave Using Matplotlib And Numpy
import numpy as np
import matplotlib.pyplot as plot
import math


# Get x values of the sine wave
time = np.arange(0, 0.01, 0.0001);

print(len(time))

freq = 500; # Freq in Hz

resolution = (2**12)-1; # 12 bits
print(resolution)
# Amplitude of the sine wave is sine of a variable like time
# amplitude = np.uint16 ( 4095*np.sin(2*np.pi*freq*time) )
# amplitude = 127*np.sin(2*np.pi*freq*time)
base_amp = 0.5*np.sin(2*np.pi*freq*time)+0.5 # Signed non-zero centered signwave

amplitude = np.uint16 (resolution*base_amp)

# Plot a sine wave using time  (nd amplitude obtained for the sine wave
plot.plot(time, amplitude)

# Give a title for the sine wave plot
plot.title('Sine wave')

# Give x axis label for the sine wave plot
plot.xlabel('Time')

# Give y axis label for the sine wave plot
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()
# Display the sine wave
plot.show()

# # Dump Audio File playing SINE Wave data
for i in range(len(time)):
    with open("sine_wave_v3.raw", "ab") as f:
        # f.write(bytes([amplitude[i]]))
        f.write(amplitude[i].tobytes())


# Audio_test = 32 bits signed Little Endian Fs = 8kHz Pre recorded data
# sine_wave_v1 = 8 bits unsigned 0-255 Fs = 10kHz Fm = 500Hz Td = 0.5
# sine_wave_v2 = 12 bits unsigned 0-4095 Fs = 10kHz Fm = 500Hz Td = 1
