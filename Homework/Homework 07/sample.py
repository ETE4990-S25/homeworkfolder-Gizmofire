import matplotlib.pyplot as plt
import mplcursors
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Add interactive cursors
mplcursors.cursor(ax, hover=True)

# Add title and labels
plt.title('Interactive Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
