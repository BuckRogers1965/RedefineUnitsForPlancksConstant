import math
'''
Shows an impractial unit definition that makes hc=G=1 and examines most of the properties of a photon at 1Hz
Also does a lot of different calculations afterward.
'''

# Define constants and scaling factors
c_old = 299792458.0  # m/s
h_old = 6.62607015e-34  # J*s
G_old = 6.67430e-11  # m^3 kg^-1 s^-2

s_length = 3.64117228161056598231271787236294544974398351386797e-18  # m
s_mass   = 5.45551186133462083261573179563841219265538485514282e-8  # kg

# Function to calculate energy
def calculate_energy(m, c):
    return m * c**2

# Function to calculate frequency
def calculate_frequency(E, h):
    return E / h

# Old values
f = 1e0 # Hz
mass_old = h_old * f/c_old**2  # kg
meter_old = 1.0
wavelength_old =  c_old/f
# hf = mc^2
# c/f = c/(mc^2/h)
# wavelength = ch/mc^2

# Calculate energy and frequency with old values
energy_old = calculate_energy(mass_old, c_old)
frequency_old = calculate_frequency(energy_old, h_old)

# New values

#set hc = 1
meter_scaling = 1/s_length**(1/3)
mass_scaling  = 1/s_mass


# set hc = 2*10^-25
#meter_scaling = 0.997735853701971098
#mass_scaling  = 1.0136931846243198

# Our current system
#meter_scaling = 1.0
#mass_scaling  = 1.0

s_length_new = s_length * meter_scaling**3
s_mass_new   = s_mass * mass_scaling

c_new          =          c_old / meter_scaling
meter_new      =              1 * meter_scaling
mass_new       =       (f * s_length_new * s_mass_new)/c_new**3
wavelength_new = wavelength_old / meter_scaling

h_new          =  s_length_new * s_mass_new / c_new  # This sets h to 1/c in the new units

# Calculate energy and frequency with new values
energy_new    = calculate_energy    (mass_new, c_new)
frequency_new = calculate_frequency (energy_new, h_new)

# Print results
print(f"meter_scaling : {meter_scaling}")
print(f"kg scaling    : {mass_scaling}")


print()

print(f"       Freq   Meter      c          Wavelength       Mass              Momentum        Energy           h")

print(f"  old: {frequency_old:<6.3} {meter_old:<10.3} {c_old:<10.3e} {wavelength_old:<16.10} {mass_old:<16.10} {energy_old/c_old:<16.10} {energy_old:<16.10e} {h_old:<16.10}")
print(f"  new: {frequency_new:<6.3} {meter_new:<10.3} {c_new:<10.3e} {wavelength_new:<16.10} {mass_new:<16.10} {energy_new/c_new:<16.10} {energy_new:<16.10e} {h_new:<16.10e}")
print(f"ratio: {frequency_new/frequency_old:<6.3} {meter_new/meter_old:<10.3} {c_new/c_old:<10.3e} {wavelength_new/wavelength_old:<16.10} {mass_new/mass_old:<16.10} {(energy_new/c_new)/(energy_old/c_old):<16.10} {energy_new/energy_old:<16.10} {h_new/h_old:<16.10e}")

print()
print ( f"          old                    new")
print ( f" s_length {s_length}  {s_length_new} \n   s_mass {s_mass}  {s_mass_new}")
print ( f"       hc {h_old * c_old} {s_length_new * s_mass_new}")
print ( f"        h {h_old:<22.10} {(s_length_new * s_mass_new)/c_new}")

print()
print (f" c_new              1/c_new              1/c_new^2            1/c_new^3              2/c_new")
print (f" {c_new} {1/c_new} {1/c_new**2} {1/c_new**3} {2/c_new} ")

print()
print (f"                             mass_old/mass_new : {mass_old/mass_new}\n mass_old/mass_new * s_length_new * s_mass_new : {mass_old/mass_new * s_length_new * s_mass_new}\n             (s_length_new * s_mass_new)/c_new : {(s_length_new * s_mass_new)/c_new} ")
