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

#meter_scaling = 2.33570373e3
meter_scaling = s_length**(1/3)
#meter_scaling =  1.0
print (f"*** {meter_scaling}\n")

# New values
c_new          =          c_old / meter_scaling
meter_new      =              1 * meter_scaling
mass_new       =       mass_old / s_mass
wavelength_new = wavelength_old / meter_scaling
h_new          =              1 / c_new  # This sets h to 1/c in the new units

# Calculate energy and frequency with new values
energy_new    = calculate_energy    (mass_new, c_new)
frequency_new = calculate_frequency (energy_new, h_new)

# Print results
print()

print(f"       Meter        c         Wavelength           Mass            Energy            Freq            h")

print(f"  old: {meter_old:<10.3} {c_old:<10.3e} {wavelength_old:<16.10} {mass_old:<16.10} {energy_old:<16.10} {frequency_old:<16.10} {h_old:<16.10}")
print(f"  new: {meter_new:<10.3} {c_new:<10.3e} {wavelength_new:<16.10} {mass_new:<16.10} {energy_new:<16.10} {frequency_new:<16.10} {h_new:<16.10}")

print(f"ratio: {meter_new/meter_old:10.3} {c_new/c_old:10.3e} {wavelength_new/wavelength_old:16.10} {mass_new/mass_old:16.10} {energy_new/energy_old:16.10} {frequency_new/frequency_old:16.10} {h_new/h_old:16.10}")
print(f"fixed: {meter_new / s_length**(1/3):<10.3} {c_new* s_length**(1/3):<10.3e} {wavelength_new*(s_length**(1/3)):<16.10} {mass_new*s_mass:<16.10} {energy_new*c_new/c_old *(s_length*s_mass):<14.10} {frequency_new:<16.10} {h_new* c_new *s_length*s_mass/c_old:<16.10}")

print()
print ( f"{mass_old /s_mass} {mass_new} \n {c_new**2} {c_old**2} \n")
print ( f"1/(s_mass*s_length**2/3) = {1/(s_mass * (s_length**(1/3))**2 )} ")

print()
print ( f"Energy of the old wavelength {(h_old * c_old)/wavelength_old} ")
print ( f"Raw Inverse wavlength result: {1/wavelength_old}")

print()
print ( f"Energy of the new wavelength {1/wavelength_new} ")
print ( f"Frequency of the new wavelength: {c_new/wavelength_new}")
print ( f" the new ratio: {(energy_new/energy_old)/(mass_new/mass_old)}")

print()

print ( f"old vs new wl: {(wavelength_old/wavelength_new)}")

print()

print ( f"old s_length = {s_length}*{c_old**2} = {s_length*c_old**2}")
print ( f"old s_length = 1/{s_length}*{c_old**2} = {1/(s_length*c_old**2)}")
print ( f"old s_length = {c_old}*{0.327252244477045} = {c_old*0.327252244477045}")
print ( f"old s_length = {0.327252244477045}/{c_old} = {0.327252244477045/c_old}")
print()
print ("This one is very important")
print ("This shows that the ratio between  c**3/s_length is the inverse of the ratio between mass/s_mass")
print ("This ratio is set by needing to work with E=mc^2")
print ( f"old c**3/s_length = {c_old**3} / {s_length} = {c_old**3/s_length}")
print ( f"mass_old/s_mass   = {mass_old} / {s_mass} = {mass_old / s_mass}")
print (f" {c_old**3/s_length} * {mass_old / s_mass}  = {c_old**3/s_length * mass_old / s_mass}")
print()
print ( f"old s_length/c**3 = {s_length} / {c_old**3} = {s_length/c_old**3}")
print ( f"s_mass/mass_old   = {s_mass} / {mass_old} = {s_mass / mass_old}")
print ( f"new c^3 / 1       = {c_new**3} / {1}        = {c_new**3}")
