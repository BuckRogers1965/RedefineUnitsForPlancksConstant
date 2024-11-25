import numpy as np

# Fundamental constants with high precision
c = 299792458.0  # Speed of light in m/s
hbar = 1.054571817e-34  # Reduced Planck constant in J⋅s
G = 6.67430e-11  # Gravitational constant in m³/(kg⋅s²)

# Calculate Planck pressure
planck_pressure = (c**7)/(hbar * G**2)

print(f"Planck pressure = {planck_pressure:.15e} Pa")

# Known value to compare
known_value = 4.633129e113
print(f"actual value    = {known_value:.15e} Pa")

# Calculate relative difference
rel_diff = abs(planck_pressure - known_value)/known_value
print(f"Relative difference = {rel_diff:.15e}")
