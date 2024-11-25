import math

# Constants
c = 299792458  # Speed of light in m/s
m_P = 2.176434e-8  # Planck mass in kg

# Calculate Planck momentum
planck_momentum = m_P * c / math.sqrt(2)

# Output the result
print(f"Planck Momentum: {planck_momentum:.5e} kg·m/s")
