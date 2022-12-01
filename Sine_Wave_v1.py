# Plotting A Sine Wave Using Matplotlib And Numpy
import numpy as np
import matplotlib.pyplot as plot
import math


# Get x values of the sine wave
time = np.arange(0, .01, 0.0001);

print(len(time))

freq = 500; # Freq in Hz

resolution = (2**12)-1; # 12 bits
print(resolution)
# Amplitude of the sine wave is sine of a variable like time
# amplitude = np.uint16 ( 4095*np.sin(2*np.pi*freq*time) )
# amplitude = 127*np.sin(2*np.pi*freq*time)
base_amp = 0.5*np.sin(2*np.pi*freq*time)+0.5 # Signed non-zero centered signwave

amplitude = resolution*base_amp

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
# for i in range(len(time)):
#     with open("sine_wave.raw", "ab") as f:
#         f.write(bytes([amplitude[i]]))
