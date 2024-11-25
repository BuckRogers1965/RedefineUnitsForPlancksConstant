import math

# Constants
hbar = 1.0545718e-34  # Reduced Planck constant in J·s
c = 299792458          # Speed of light in m/s
G = 6.67430e-11       # Gravitational constant in m^3/(kg·s^2)

# Calculate Planck momentum
planck_momentum = math.sqrt((hbar * c**3) / G)

# Output the result
print(f"Planck Momentum: {planck_momentum:.5e} kg·m/s")
