import numpy as np
import pandas as pd

# Constants
alpha = 1.53843951260968407858e-6  
beta = 5.45551124829157414485e-8
c = 299792458  # Speed of light (m/s)
epsilon_0 = 8.854187817e-12  # Vacuum permittivity (C^2/N·m^2)
k_B = 1.380649e-23  # Boltzmann constant (J/K)

# Planck Unit Formulas

# Planck Length
def planck_length(alpha, c):
    return (alpha ** 3) / ((2 * np.pi)**(1/2) * c ** 2)

# Planck Time
def planck_time(alpha, c):
    return (alpha ** 3) / ((2 * np.pi)**(1/2) * c ** 3)

# Planck Mass
def planck_mass(beta):
    return beta / (2 * np.pi)**(1/2)

# Planck Charge
def planck_charge(alpha, beta, epsilon_0):
    return (2 * (alpha ** 3) * beta * epsilon_0)**(1/2)

# Planck Temperature
def planck_temperature(beta, k_B):
    return (c**2 * beta ) / ((2 * np.pi)**(1/2) * k_B)

# Known values for comparison
known_values = {
    'Planck Length (m)': 1.616255e-35,
    'Planck Time (s)': 5.391247e-44,
    'Planck Mass (kg)': 2.176434e-8,
    'Planck Charge (C)': 1.875545e-18,
    'Planck Temperature (K)': 1.416784e32,
}

# Testing function
def test_planck_units(alpha, beta, c, epsilon_0, k_B, known_values):
    results = []

    # Planck Length
    calculated_length = planck_length(alpha, c)
    error_length = abs(calculated_length - known_values['Planck Length (m)'])
    results.append(('Planck Length (m)', known_values['Planck Length (m)'], calculated_length, error_length))

    # Planck Time
    calculated_time = planck_time(alpha, c)
    error_time = abs(calculated_time - known_values['Planck Time (s)'])
    results.append(('Planck Time (s)', known_values['Planck Time (s)'], calculated_time, error_time))

    # Planck Mass
    calculated_mass = planck_mass(beta)
    error_mass = abs(calculated_mass - known_values['Planck Mass (kg)'])
    results.append(('Planck Mass (kg)', known_values['Planck Mass (kg)'], calculated_mass, error_mass))

    # Planck Charge
    calculated_charge = planck_charge(alpha, beta, epsilon_0)
    error_charge = abs(calculated_charge - known_values['Planck Charge (C)'])
    results.append(('Planck Charge (C)', known_values['Planck Charge (C)'], calculated_charge, error_charge))

    # Planck Temperature
    calculated_temperature = planck_temperature(beta, k_B)
    error_temperature = abs(calculated_temperature - known_values['Planck Temperature (K)'])
    results.append(('Planck Temperature (K)', known_values['Planck Temperature (K)'], calculated_temperature, error_temperature))

    return results

# Run the test
test_results = test_planck_units(alpha, beta, c, epsilon_0, k_B, known_values)

# Print the results as an ASCII table
print(f"{'Unit':<30} {'Known Value':<20} {'Calculated Value':<20} {'Absolute Error':<20}")
print("="*90)

for result in test_results:
    unit, known, calculated, error = result
    print(f"{unit:<30} {known:<20} {calculated:<20} {error:<20}")

