import numpy as np
import pandas as pd


# This program generates a table of frequencies, their corresponding inverse wavelengths (frequency / c),
# and their energy equivalents scaled by hc. Traditionally, the product hc and the appearance of discrete
# energy values have been interpreted as evidence of intrinsic quantization in atomic and subatomic processes.
#
# However, this calculation highlights an alternative interpretation: the apparent "quantization"  
# in energy results from the scaling factor hc applied in reciprocal (hyperbolic) space 
# of 1/wavelength rather than any intrinsic, indivisible energy steps. The non-linear increments in energy 
# arise due to the reciprocal relationship between frequency and wavelength (1/frequency), which projects 
# continuous frequencies into hyperbolic space in a manner that appears quantized when scaled by hc.
#
# Consequently, this perspective suggests that quantization may be an artifact of how energy values are
# represented and scaled within our unit system, rather than an inherent property of energy itself. This 
# program, therefore, offers a different lens for understanding quantum mechanics, where the appearance of 
# discrete energy levels is a result of unit scaling in hyperbolic space.

# Constants
c = 299792458       # Speed of light in m/s
h = 6.62607015e-34  # Planck's constant in J·s
hc = h * c

# Parameters
start_frequency = 1.0e12  # Starting frequency in Hz
step = 0.1e12             # Step size in Hz
num_steps = 10            # Number of steps (you can adjust this as needed)

# Create lists to store the values
frequencies = []
wavelengths = []
f_over_c_values = []
f_over_c_hc_values = []
hf_energies = []
diffs = []

prev = 0
# Generate the table data
for i in range(num_steps):
    frequency = start_frequency + i * step
    f_over_c = frequency / c
    w = c/frequency
    f_over_c_hc = f_over_c * hc
    hf_energy = h * frequency
    diff = prev -f_over_c_hc
    prev = f_over_c_hc
    
    frequencies.append(frequency)
    wavelengths.append(w)
    f_over_c_values.append(f_over_c)
    f_over_c_hc_values.append(f_over_c_hc)
    hf_energies.append(hf_energy)
    diffs.append(diff)

# Set display precision globally for the DataFrame
pd.options.display.float_format = '{:.8e}'.format

# Create a DataFrame for easier viewing
table = pd.DataFrame({
    'Frequency (Hz)': frequencies,
    'λ (m)': wavelengths,
    '1/λ': "1 / λ =",
    'f / c (1/m)': f_over_c_values,
    '(f / c) * K (J)': f_over_c_hc_values,
    '(E = hf (J))': hf_energies,
    'diffs': diffs
})

# Print the table
print (f"K = ratio between h and c, taken as hc with units J m")
print(table)

# --------------------------------------------------------------------------------
# Results:

#K = ratio between h and c, taken as hc with units J m
#   Frequency (Hz)          λ (m)      1/λ    f / c (1/m)  (f / c) * K (J)   (E = hf (J))           diffs
#0  1.00000000e+12 2.99792458e-04  1 / λ = 3.33564095e+03   6.62607015e-22 6.62607015e-22 -6.62607015e-22
#1  1.10000000e+12 2.72538598e-04  1 / λ = 3.66920505e+03   7.28867716e-22 7.28867716e-22 -6.62607015e-23
#2  1.20000000e+12 2.49827048e-04  1 / λ = 4.00276914e+03   7.95128418e-22 7.95128418e-22 -6.62607015e-23
#3  1.30000000e+12 2.30609583e-04  1 / λ = 4.33633324e+03   8.61389119e-22 8.61389119e-22 -6.62607015e-23
#4  1.40000000e+12 2.14137470e-04  1 / λ = 4.66989733e+03   9.27649821e-22 9.27649821e-22 -6.62607015e-23
#5  1.50000000e+12 1.99861639e-04  1 / λ = 5.00346143e+03   9.93910522e-22 9.93910522e-22 -6.62607015e-23
#6  1.60000000e+12 1.87370286e-04  1 / λ = 5.33702552e+03   1.06017122e-21 1.06017122e-21 -6.62607015e-23
#7  1.70000000e+12 1.76348505e-04  1 / λ = 5.67058962e+03   1.12643193e-21 1.12643193e-21 -6.62607015e-23
#8  1.80000000e+12 1.66551366e-04  1 / λ = 6.00415371e+03   1.19269263e-21 1.19269263e-21 -6.62607015e-23
#9  1.90000000e+12 1.57785504e-04  1 / λ = 6.33771781e+03   1.25895333e-21 1.25895333e-21 -6.62607015e-23
