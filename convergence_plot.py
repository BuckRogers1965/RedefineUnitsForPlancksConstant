import numpy as np
import matplotlib.pyplot as plt

# Define the range of c values from 3e8 down to 1:
c_values = np.linspace(3e8, 1, 500)  # 500 points for a smooth curve

# Keep mass constant (let's set it to 1 for simplicity):
mass = 1

# Calculate h, p, and hc for each c value:
h_values = mass * c_values**2
p_values = mass * c_values
hc_values = h_values * c_values

# Create the plot:
plt.figure(figsize=(10, 6))

# Plot mass (constant)
plt.plot(c_values, [mass]*len(c_values), label='m', color='black', linewidth=3)

# Plot p = mc
plt.plot(c_values, p_values, label='p (momentum)', color='blue')

# Plot h = mc^2
plt.plot(c_values, h_values, label='h (Planck\'s constant)', color='red')

# Plot hc
plt.plot(c_values, hc_values, label='hc', color='green')


# Customize the plot:
plt.xlabel('Speed of Light (c)')
plt.ylabel('Value')
plt.title('Convergence of Photon Properties to Mass as c Approaches 1')
plt.xscale('log')  # Use logarithmic scale for x-axis for better visualization
plt.yscale('log') # use log scale for y-axis
plt.grid(True)
plt.legend()
#plt.show()
plt.savefig('convergence_plot.png')


# Print some data points to see numeric convergence
print("Sample Data Points:")
print("------------------")
for i in [0, 250, 499]: #first, middle and last value in c_values array
    print(f"c: {c_values[i]:.2e}, h: {h_values[i]:.2e}, p: {p_values[i]:.2e}, hc: {hc_values[i]:.2e}, m: {mass}")
