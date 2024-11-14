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

# Generate the table data
for i in range(num_steps):
    frequency = start_frequency + i * step
    f_over_c = frequency / c
    w = c/frequency
    f_over_c_hc = f_over_c * hc
    
    frequencies.append(frequency)
    wavelengths.append(w)
    f_over_c_values.append(f_over_c)
    f_over_c_hc_values.append(f_over_c_hc)

# Create a DataFrame for easier viewing
table = pd.DataFrame({
    'Frequency (Hz)': frequencies,
    'Wavelength (m)': wavelengths,
    'Frequency / c (1/m)': f_over_c_values,
    '(Frequency / c) * hc (J)': f_over_c_hc_values
})

# Print the table
print(table)

# --------------------------------------------------------------------------------
# Results:

#    Frequency (Hz)  Wavelength (m)  Frequency / c (1/m)  (Frequency / c) * hc (J)
#0    1.000000e+12        0.000300          3335.640952              6.626070e-22
#1    1.100000e+12        0.000273          3669.205047              7.288677e-22
#2    1.200000e+12        0.000250          4002.769142              7.951284e-22
#3    1.300000e+12        0.000231          4336.333238              8.613891e-22
#4    1.400000e+12        0.000214          4669.897333              9.276498e-22
#5    1.500000e+12        0.000200          5003.461428              9.939105e-22
#6    1.600000e+12        0.000187          5337.025523              1.060171e-21
#7    1.700000e+12        0.000176          5670.589618              1.126432e-21
#8    1.800000e+12        0.000167          6004.153714              1.192693e-21
#9    1.900000e+12        0.000158          6337.717809              1.258953e-21
