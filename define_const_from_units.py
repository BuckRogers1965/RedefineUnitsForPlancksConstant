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

h = 6.62607015e-34
c = 299792458
G = 6.6743015e-11

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
    'gamma_p': 2.675221874e8,  # Proton gyromagnetic ratio (rad·s⁻¹·T⁻¹)
}

def calculate_base_units(h, c, G):
    """Calculate base units from fundamental constants."""
    hc = h * c
    kg = np.sqrt(hc / G)

                       # define second value
    s = ((G**(3/2) * kg**(5/2)) / hc)**(3/2)

    m_cubed = G * kg * (s**2)
    m = m_cubed**(1/3)
    
    scale = 1.17476068e-10
    m = m / scale       # define meter value
    
    K = 2.81809817e-34  # define Kelvin value
    
    return kg, s, m, K

def calculate_derived_constants(kg, s, m, K):
    """Calculate derived constants from base units."""
    constants = {}
    
    # Basic constants
    constants['hc'] = m**3 * kg / s**2 * (1.17476068e-10)**3
    constants['G'] = m**3 / (kg * s**2) * (1.17476068e-10)**3
    constants['c'] = m / s
    constants['k'] = kg * m**2 * K / s**2 / 1.00080553745694328382e-01
    constants['sigma'] = kg / (s**3 * K**4 * 2.63394301e+173)

    # Electromagnetic constants
    constants['epsilon_0'] = 1 / (kg * m**3) * s**4 * 1.56140418156780126208e+20
    constants['mu_0'] = kg * m / s**2 / 1.56140418156780126208e+20
    constants['e'] = np.sqrt(4 * np.pi * constants['epsilon_0'] * constants['hc']) / 2.93431860926347312102e+01
    constants['alpha'] = constants['e']**2 / (2 * constants['epsilon_0'] * constants['hc'])
    
   
    # Quantum constants
    constants['h'] = constants['hc'] / constants['c']
    constants['hbar'] = constants['h'] / (2 * np.pi)
    
    # Atomic constants - need scaling factors
    constants['me'] = kg / 5.98889170448846013071e+22 
    constants['mp'] = kg / 3.26165236209272954880e+19
    constants['mn'] = kg / 3.25716262624836771840e+19
    
    # Length scales
    constants['a0'] = m  / 4.72226689504315145314e+05
    constants['rc'] = m   / 8.86788127280288887024e+09
    constants['lambda_C'] = m  /1.02992436203389391303e+07 
    
    # Magnetic constants
    constants['Phi_0'] = constants['h'] / (2 * constants['e']) 
    constants['mu_B'] = constants['e'] * constants['hbar'] / (2 * constants['me']) 
    constants['mu_N'] = constants['e'] * constants['hbar'] / (2 * constants['mp']) 
    
    # Thermodynamic
    constants['R'] = constants['k'] * 6.02214076e23
    
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
    
    kg, s, m, K = calculate_base_units(h, c, G)
    
    print("Base units:")
    print(f"kg: {kg:.8e} kg")
    print(f"s: {s:.8e} seconds")
    print(f"m: {m:.8e} meters")
    print(f"K: {K:.8e} Kelvin")
    
    constants = calculate_derived_constants(kg, s, m, K)
    
    print("\nCalculated constants:")
    for name, value in constants.items():
        print(f"{name:<12} {value:.8e}")
    
    validate_constants(constants)

if __name__ == "__main__":
    main()
