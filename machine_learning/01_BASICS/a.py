import numpy as np
import matplotlib.pyplot as plt

# Define the time range (e.g., 0 to 2 seconds to show a few envelope cycles)
t = np.linspace(0, 2, 5000)

# Define the function
y = (2 + np.cos(10 * t)) * np.cos(1000 * t)
envelope_upper = 2 + np.cos(10 * t)
envelope_lower = -(2 + np.cos(10 * t))

# Plot the graph
plt.figure(figsize=(10, 4))
plt.plot(t, y, color='blue', alpha=0.7, label='y(t) = (2 + cos(10t))cos(1000t)')
plt.plot(t, envelope_upper, color='red', linestyle='dashed', linewidth=2, label='Envelope')
plt.plot(t, envelope_lower, color='red', linestyle='dashed', linewidth=2)

plt.title('Amplitude Modulation Graph')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
