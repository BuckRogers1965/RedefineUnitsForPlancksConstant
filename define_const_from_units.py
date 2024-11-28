#!/home/jrogers/Documents/ai/chat/ragserver/venv/bin/python3
import math
import numpy as np


'''

This program creates a framework to explore unit scaling. 

By assigning a value to each different unit this framework
allows you to recreate the constant from its units. 

If there is any difference left over, that is the true
constant that has been disguised by the unit scaling. 

This is natural units in reverse.  We are teasing out the
relationships between all these units one constant at a time.

James M. Rogers, SE Ohio, 21 Nov 2024 1400
'''

h   = 6.62607015e-34
c   = 299792458
G   = 6.6743015e-11
mol = 6.0221407600e+23 #2.63394301e+173
e = 1.602176634e-19     # Elementary charge (C)

# Known physical constants for validation - with units commented
KNOWN_VALUES = {
    # Electromagnetic Constants
    'c': 2.99792458e8,        # Speed of light (m/s)
    'e': 1.602176634e-19,     # Elementary charge (C)
    'epsilon_0': 8.8541878128e-12,  # Vacuum permittivity (F/m)
    'mu_0': 1.25663706212e-6,      # Vacuum permeability (H/m)
    'alpha': 7.297352569e-3,       # Fine structure constant (dimensionless)
    
    # Gravitational Constants
    'G': 6.67430150e-11,      # Gravitational constant (m³/kg·s²)
    
    # Quantum Constants
    'h': 6.62607015e-34,      # Planck constant (J·s)
    'hc': h*c,                # Planck constant times c (J·m)
    'hbar': 1.054571817e-34,  # Reduced Planck constant (J·s)
    'me': 9.1093837015e-31,   # Electron mass (kg)
    'mp': 1.67262192369e-27,  # Proton mass (kg)
    'mn': 1.67492749804e-27,  # Neutron mass (kg)
    
    # Thermodynamic Constants
    'k': 1.380649e-23,        # Boltzmann constant (J/K)
    'sigma': 5.670374419e-8,  # Stefan-Boltzmann constant (W/m²·K⁴)
    'R': 8.314462618,         # Gas constant (J/mol·K)
    'Na': 6.02214076e23,      # Avogadro constant (mol⁻¹)
    
    # Atomic & Nuclear Constants
    'Ry': 13.605693122994,    # Rydberg constant (eV)
    'a0': 5.29177210903e-11,  # Bohr radius (m)
    'rc': 2.8179403262e-15,   # Classical electron radius (m)
    'lambda_C': 2.42631023867e-12,  # Compton wavelength (m)
    
    # Electromagnetic Derived Constants
    'Kcd': 683,               # Luminous efficacy (lm/W)
    'Phi_0': 2.067833848e-15, # Magnetic flux quantum (Wb)
    'Kj': 483597.8484e9,      # Josephson constant (Hz/V)
    'Rk': 25812.80745,        # von Klitzing constant (Ω)
    
    # Nuclear Constants
    'mu_B': 9.2740100783e-24, # Bohr magneton (J/T)
    'mu_N': 5.0507837461e-27, # Nuclear magneton (J/T)
    'gamma_p': 2.675221874e8, # Proton gyromagnetic ratio (rad·s⁻¹·T⁻¹)

    'b': 2.897771955e-3,      # Wien displacement constant 
    'c₁': 3.741771852e-16,    # First radiation constant 
    'G₀': 7.748091729e-5,     # Conductance quantum 
    'mᵤ': 1.660539067e-27,    # Atomic mass constant 
    'Vm': 0.02271095464,      # Molar gas volume 
    'F': 96485.33212,         # Faraday constant 
    'nₑ': 2.686780111e25,     # Loschmidt constant 
    'Φ₀': 2.067833848e-15,    # Magnetic flux quantum 
    'h/2me': 3.636947552e-4,  # Quantum of circulation 
    'σₑ':  6.652458732e-29,   # Thomson cross section 
    'n₀': 2.686780111e25,     # Loschmidt constant 
}

def calculate_base_units(h, c, G):
    """Calculate base units from fundamental constants."""
    hc = h * c
    kg = np.sqrt(hc / G)
    s = ((G**(3/2) * kg**(5/2)) / hc)**(3/2) # define second value
    m_cubed = G * kg * (s**2)
    m = m_cubed**(1/3)
    K = 1/4.90108670499514355469e+12  # define Kelvin value
    C = (1/1.15967826341182373079e-05)**(.5)
    return kg, s, m, K, C

def calculate_derived_constants(kg, s, m, K, C):
    """Calculate derived constants from base units."""
    constants = {}
    print (f"*** {s/m}")
    
    # Basic constants
    constants['hc'] = m**3 * kg / s**2 
    constants['G'] = m**3 / (kg * s**2) 
    constants['k'] = kg * m**2 * K / s**2 
    constants['sigma'] = m * kg *mol / (s**3 * K ) / 1.43937911919058257853e+61
    #r_gas_calc   =   s_length * s_mass * N_A / s_temp

    constants['Vm'] =  1 / 4.40316145160510075129e+01
    constants['Na'] = mol 

    # Electromagnetic constants
    constants['epsilon_0'] = C**2 / (kg * m**2) * s**4 
    constants['mu_0'] = kg * m  / s**2   / 1.83427623809343376160e+10
    #constants['e'] = np.sqrt(4 * np.pi * constants['epsilon_0'] * constants['hc']) 
    constants['alpha'] = e**2 / (2 * C) / 5.98955035930460787984e-39
   
    # Quantum constants
    constants['h'] = constants['hc'] / c
    constants['hbar'] = constants['h'] / (2 * np.pi)

    # Atomic constants 
    constants['me'] = kg / 5.98889170448846013071e+22
    constants['mp'] = kg / 3.26165236209272954880e+19
    constants['mn'] = kg / 3.25716262624836771840e+19
    constants['mᵤ'] = kg / 3.28538566584147353600e+19
    
    # Length scales
    constants['a0'] = m       / 5.54753346876238134181e-05
    constants['rc'] = m       / 1.04176382341971884848e+00
    constants['lambda_C'] = m / 1.20991464389150356860e-03
    

    # Magnetic constants
    constants['Phi_0'] = constants['h'] / (2 * e) 
    constants['mu_B'] = e * constants['hbar'] / (2 * constants['me']) 
    constants['mu_N'] = e * constants['hbar'] / (2 * constants['mp']) 
    
    # Thermodynamic
    constants['R'] = constants['k'] * 6.02214076e23

    constants['b'] = m*K           / 2.06701902243347360058e-25
    constants['n₀'] = 1/m**3       / 1.47117617541269324800e+18
    constants['h/2me'] = m**2 / s  / 2.84272030908696081178e-13
    constants['nₑ'] = m**2         / 3.20752465462918465256e-55
    constants['c₁'] = 2*np.pi * h * c**2
    #constants['c₁'] = m**4 * kg * s**(-3) 

    '''
Conductance quantum 
G₀
S (siemens = A/V)

Faraday constant 
F
C/mol

Magnetic flux quantum 
Φ₀
Wb (weber = V⋅s)

'''
    
    return constants

def validate_constants(calculated, known=KNOWN_VALUES):
    """Compare calculated values with known values and compute ratios."""
    print("\nValidation Results:")
    print(f"{'Constant':<12} {'Calculated':<15} {'Known':<15} {'Ratio (Calc/Known)':<20} {'log10(|Ratio|)':<15}")
    print("-" * 77)
    
    for name, known_value in known.items():
        if name in calculated:
            calc_value = calculated[name]
            ratio = calc_value / known_value
            log_ratio = np.log10(abs(ratio)) if ratio != 0 else float('inf')
            
            print(f"{name:<12} {calc_value:.10e} {known_value:.10e} {ratio:.20e} {log_ratio:15.20f}")

def main():
    
    kg, s, m, K, C = calculate_base_units(h, c, G)
    
    print("Base units:")
    print(f"kg: {kg:.8e} kg")
    print(f"s: {s:.8e} seconds")
    print(f"m: {m:.8e} meters")
    print(f"K: {K:.8e} Kelvin")
    print(f"C: {C:.8e} Charge")
    
    constants = calculate_derived_constants(kg, s, m, K, C)
    
    #print("\nCalculated constants:")
    #for name, value in constants.items():
    #    print(f"{name:<12} {value:.8e}")
    
    validate_constants(constants)

if __name__ == "__main__":
    main()
