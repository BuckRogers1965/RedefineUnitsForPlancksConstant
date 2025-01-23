import math
'''
Shows an impractial unit definition that makes hc=G=1 and examines most of the properties of a photon at 1Hz
Also does a lot of different calculations afterward.
  came from y9.py
'''

# Define constants and scaling factors
c_old = 299792458.0  # m/s
h_old = 6.62607015e-34  # J*s
G_old = 6.67430e-11  # m^3 kg^-1 s^-2

s_length = 3.64117228161056598231271787236294544974398351386797e-18  # m
print (f" cube of s_va is {s_length**(1/3)} m")
s_mass   = 5.45551186133462083261573179563841219265538485514282e-8  # kg
pi = 3.141592653589793238462643383279502884197169399375105820974944592

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
g= 32.1740188643502078564005

# imperial
meter_scaling = 3.28084
mass_scaling  = 2.20462 /g

meter_scaling = 6.50009330403e+5 
mass_scaling  = 1.83300857081e+7 

s_length_new   = s_length * meter_scaling**3
s_mass_new     = s_mass   * mass_scaling
c_new          = c_old * meter_scaling
h_new          = s_length_new * s_mass_new / c_new   # This sets h to 1/c in the new units 

meter_new      = 1 * meter_scaling
mass_new       = h_new/c_new**2 * g
wavelength_new = wavelength_old  * meter_scaling

# Calculate energy and frequency with new values
energy_new    = h_new
frequency_new = calculate_frequency (energy_new, h_new)

# Print results
print()
print(f" meter_scaling : {meter_scaling}")
print(f" kg scaling    : {mass_scaling*g}")
print()

print(f"         Freq   Meter      c            Wavelength       Mass              Momentum        Energy           h")

print(f"   old: {frequency_old:<6.3} {meter_old:<10.3} {c_old:<12.10} {wavelength_old:<16.10} {mass_old:<16.10} {energy_old/c_old:<16.10} {energy_old:<16.10e} {h_old:<16.10}")
print(f"   new: {frequency_new:<6.3} {meter_new:<10.3} {c_new:<12.10} {wavelength_new:<16.10} {mass_new:<16.10} {energy_new*g/c_new:<16.10} {energy_new:<16.10e} {h_new:<16.10e}")
print(f" ratio: {frequency_new/frequency_old:<6.3} {meter_new/meter_old:<10.3} {c_new/c_old:<12.10} {wavelength_new/wavelength_old:<16.10} {(mass_new)/mass_old:<16.10} {(energy_new*g/c_new)/(energy_old/c_old):<16.10} {energy_new/energy_old:<16.10} {h_new/h_old:<16.10e}")

print()
print ( f"          old                    new                    ratio")
print ( f" s_va {s_length}  {s_length_new}   {s_length/s_length_new}\n   m_P {s_mass}  {s_mass_new}   {s_mass/s_mass_new}")
print ( f"       hc {h_old * c_old} {s_length_new * s_mass_new}   {(h_old * c_old)/(s_length_new * s_mass_new)}")
print ( f"        h {h_old:<22.10} {(s_length_new * s_mass_new)/c_new}  {(h_old)/((s_length_new * s_mass_new)/c_new)}")
print ( f"        G {s_length/s_mass:<22.10} {(s_length_new / s_mass_new)}  {(s_length/s_mass)/((s_length_new / s_mass_new))}")
print()

G = (s_length/s_mass)
new_G = G * 0.22480894387096  * 10.76  / 0.00469
h_new = h_old * 0.737562
new_m_P  = ((h_new * c_new) / new_G)**(1/2)
new_s_va  = ((h_new * c_new) * new_G)**(1/2)

print ( f" m_P  {s_mass:14.11e} {new_m_P:14.11e}  {s_mass/new_m_P:14.11f}   ")
print ( f" s_va {s_length:14.11e} {new_s_va:14.11e}  {new_s_va/s_length:14.11f}  ")
print ( f"l^1/3 {s_length**(1/3):14.11e} {new_s_va**(1/3):14.11e}  {(new_s_va/s_length)**(1/3):14.11f}  ")
print()

print (f"old values c  {c_old}  1/c {1/c_old} s_va {s_length**(1/3)}")
print(f"{c_old/s_length**(1/3):14.11e} {c_new/new_s_va**(1/3):14.11e} {(c_old/s_length**(1/3))/(c_new/new_s_va**(1/3)):14.11f}")
print(f"{s_length**(1/3)/c_old:14.11e} {new_s_va**(1/3)/c_new:14.11e} {(s_length**(1/3)/c_old)/(new_s_va**(1/3)/c_new):14.11f} ")
print(f"{s_length**(1/3)*c_old:14.11e} {new_s_va**(1/3)*c_new:14.11e} {(s_length**(1/3)*c_old)/(new_s_va**(1/3)*c_new):14.11f}")
print(f"{1/(s_length**(1/3)*c_old):14.11e}")

print (f"old values")
print(f"{c_old/s_length:14.11e} {c_new/new_s_va:14.11e} {(c_old/s_length)/(c_new/new_s_va):14.11f}")
print(f"{s_length/c_old:14.11e} {new_s_va/c_new:14.11e} {(s_length/c_old)/(new_s_va/c_new):14.11f} ")
print(f"{s_length*c_old:14.11e} {new_s_va*c_new:14.11e} {(s_length*c_old)/(new_s_va*c_new):14.11f}")
print(f"{1/(s_length*c_old):14.11e}")

print ( f"           Δlength {meter_scaling:14.11e} cubed {meter_scaling**3:14.11f}")
print ( f"  m/l {s_mass/s_length:14.11e} {new_m_P/new_s_va:14.11e} {(s_mass/s_length)/(new_m_P/new_s_va):14.11f}")
print ( f"    c {c_old:14.11e} {c_new:14.11e}  {c_old/c_new:14.11f}  ")

print ( f"   G  {G:14.11e} {new_s_va/new_m_P:14.11e}  { new_G/G:14.11f}")
new_new_h = new_m_P * new_s_va / c_new
print ( f"   h  {h_old:14.11e} {new_new_h:14.11e}  {h_old / new_new_h:14.11f}")
print ( f" h/G  {h_old/G:14.11e} {h_new/new_G:14.11e} {(h_old/G)/(h_new/new_G):14.11f}" )
print ( f"   hc {s_length * s_mass:14.11e} {new_new_h*c_new:14.11e}  {(s_length * s_mass) / (new_new_h*c_new):14.11f}")
print ( f"   p  {h_old/c_old:14.11e} {new_new_h / c_new *g:14.11e} { (h_old/c_old)/(new_new_h / c_new  * g):14.11f}")
print ( f"   m  {h_old/c_old**2:14.11e} {new_new_h / c_new**2 *g:14.11e}  { (new_new_h / c_new**2) / ( energy_old/c_old**2):14.11f}  ")

print()
print (f"  Δh = 1/ ((Δlength^3 / Δmass) / Δc) = {1/((s_mass/new_m_P) / (new_s_va/s_length) / (c_old/c_new) )}")
print (f"  Δh = (Δc * Δlength^3 / Δmass) = {(c_old/c_new) * (new_s_va/s_length) / (s_mass/new_m_P) }")
print (f"  Δh = (Δlength^2 / Δmass) = { (meter_scaling**2) / ((s_mass/new_m_P)) }")

#print(f" trying to see the relationship:  (h * c) / (new_h * new c) = {(h_old*c_old)/(new_new_h*c_new ) :14.11e}")
print (f" planck length with c = {(h_old*G/ c_old**3)**(1/2)}")

print()
print ('''
Energy (E)  : 6.62607015  × 10⁻³⁴ J * 0.737562 ft-lb/J                  = 4.89161 × 10⁻³⁴ ft-lb
Momentum (p): 2.210219094 × 10⁻⁴² kg⋅m/s * 2.20462 lb/kg * 3.28084 ft/m = 1.59993 × 10⁻⁴¹ lb⋅ft/s
Mass (m)    : 7.372497324 × 10⁻⁵¹ kg * 2.20462 lb/kg                    = 1.62517 × 10⁻⁵⁰ lb
G ≈ 6.6743e-11 * (0.2248 lbf) * (10.76 ft²) / (0.00469 slug²)  ≈ 3.439e-8 lbf⋅ft²/slug²
''')
'''
Looking at those conversions and ratios, for the Energy (ft-lb to J) conversion factor of 0.737562, this should be derivable from base imperial-to-SI conversions:
1 foot = 0.3048 meters
1 pound = 0.45359237 kilograms
Thus 1 ft⋅lb should equal:
(0.3048 m)(0.45359237 kg)(9.80665 m/s²) = 1.355818 J
So 1 J = 1/1.355818 = 0.737562 ft⋅lb

Deriving the Conversion Factor for G
Start with SI Units: G in SI units is approximately 6.6743e-11 N⋅m²/kg².
Replace SI units with their imperial equivalents:
Replace N with lbf using the conversion factor: 1 N = 0.22480894387096  lbf.

Here's how the conversion factor is derived:
1. Definitions:
Newton (N): 1 N = 1 kg⋅m/s²
Pound-force (lbf): The force exerted by standard gravity (g) on a 1-pound (avoirdupois) mass.
2. Key Relationships:
Standard Gravity (g): g ≈ 9.80665 m/s² (This is a defined value)
Pound (lb) to Kilogram (kg): 1 lb = 0.45359237 kg (This is also a defined value)
3. Calculation:
We want to find out how many lbf are in 1 N.
Step 1: Express 1 lbf in terms of fundamental units:
1 lbf = 1 lb × g
1 lbf = (0.45359237 kg) × (9.80665 m/s²)
1 lbf = 4.4482216152605 kg⋅m/s²
Step 2: Recognize that 1 kg⋅m/s² is equal to 1 N:
1 lbf = 4.4482216152605 N
Step 3: Find out how many lbf are in 1 N (invert the relationship):
To find the conversion factor from N to lbf, we need to find how many lbf are equivalent to 1 N. We do this by dividing both sides of the equation by 4.4482216152605 N:
1 lbf / 4.4482216152605 N = 1 N /4.4482216152605 N
0.22480894387096 lbf/N = 1
Therefore: 1 N ≈ 0.22480894387096 lbf

Replace m² with ft²: 1 m = 3.281 ft, so 1 m² = (3.281 ft)² ≈ 10.76 ft²
Replace kg² with slug²: 1 kg = 0.0685 slug, so 1 kg² = (0.0685 slug)² ≈ 0.00469 slug²
Combine Conversions:
G ≈ 6.6743e-11 * (0.2248 lbf) * (10.76 ft²) / (0.00469 slug²)
G ≈ 3.439e-8 lbf⋅ft²/slug²

c_old = 299792458.0  # m/s
h_old = 6.62607015e-34  # J*s
s_length = 3.64117228161056598231271787236294544974398351386797e-18  # m
s_mass   = 5.45551186133462083261573179563841219265538485514282e-8  # kg

print()
l_scaling=1/s_length**(1/3)
m_scaling=1/s_mass
s_mass = s_mass * m_scaling
s_length = s_length * l_scaling**3
c_old = c_old  / l_scaling
print (f"old values c  {c_old}  1/c {1/c_old} s_va {s_length**(1/3)} length {l_scaling}  m_P {s_mass} mass {m_scaling}")
print(f"{c_old/s_length**(1/3):14.11e} ")
print(f"{s_length**(1/3)/c_old:14.11e} ")
print(f"{s_length**(1/3)*c_old:14.11e} ")
print(f"{1/(s_length**(1/3)*c_old):14.11e}")

print (f" h = {s_length * s_mass / c_old} ")
print (f" hc = {s_length * s_mass } ")
print (f" G = {s_length / s_mass } ")
'''
