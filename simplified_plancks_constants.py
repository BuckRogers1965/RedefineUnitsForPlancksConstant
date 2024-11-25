import numpy as np
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class PhysicsConstants:
    c: float     = 299792458.0                 # Speed of light (m/s)
    epsilon_0: float = 8.854187817e-12         # Vacuum permittivity (C^2/N·m^2)
    k_B: float   = 1.380649e-23                # Boltzmann constant (J/K)
    e : float     = 1.602176634e-19  # Elementary charge (Coulombs)
    mol: float    = 6.02214076e23    # Avogadro's number

    alpha: float  = 1.53843945498419101549e-06  # length unit scaling
    beta: float   = 5.45551186133462110058e-08  # mass unit scaling
    gamma: float  = 1.43877687750393716548e-02  # K⁻¹ (temperature scaling) 
    delta: float  = 1.32621132205611221308e-18  # C (charge scaling)

def validate_planck_units(constants: PhysicsConstants) -> Dict[str, Tuple[float, float, float]]:
    """
    Validates that the scaling factors correctly reproduce Planck units
    """
    # Calculate Planck units using simplified formulas
    h_calc = (constants.alpha**3 * constants.beta) / constants.c
    h_bar_calc = (constants.alpha**3 * constants.beta) /(2 * np.pi * constants.c)
    G_calc = constants.alpha**3 / constants.beta
    length_calc = (constants.alpha**3) / ((2 * np.pi)**(1/2) * constants.c**2)
    time_calc = (constants.alpha**3) / ((2 * np.pi)**(1/2) * constants.c**3)
    mass_calc = constants.beta / (2 * np.pi)**(1/2)
    charge_calc = constants.delta * (2)**(1/2)
    temp_calc = (constants.c**2 * constants.gamma) / ((2 * np.pi)**(1/2) * constants.alpha**3)

    boltzmann_calc = (constants.alpha**3 * constants.beta) / constants.gamma
    e0_calc = constants.delta**2 / (constants.alpha**3 * constants.beta) 
    Kb_calc =  2 * np.pi**5 * ((constants.alpha**3 * constants.beta) / constants.gamma**4)* constants.c / 15   
    alphafine_calc = constants.e**2  / (2 *(constants.delta**2))

    # J⋅mol ^−1 ⋅ K^−1  The unit definition says mol is on bottom
    r_gas_calc =  constants.beta *constants.alpha**3  * constants.mol / (constants.gamma )

    RK_calc =   (constants.beta * constants.alpha**3) / (constants.e**2 * constants.c)

    #mag flux = (alpha^3 * beta)/ (2ec)
    #mag flux = (2ec)*(alpha^3 * beta)

    # Planck angular momentum (ℏ)
    angular_momentum_calc = h_calc / (2 * np.pi)
    
    # Planck energy (√(hc⁵/G))
    energy_calc = ((constants.beta**2 * constants.c**4)/(2 * np.pi))**(1/2) 
    
    # Planck force (c⁴/G)
    force_calc = constants.beta * constants.c**4 / constants.alpha**3
    
    # Planck power (c⁵/G)
    power_calc = constants.beta * constants.c**5 / constants.alpha**3
    
    # Planck density (c⁵/(hG²))
    density_calc = (constants.beta * constants.c**6 * 2 * np.pi)/(constants.alpha**9)
    
    # Planck area (length²)
    area_calc = length_calc**2
    
    # Planck volume (length³)
    volume_calc = length_calc**3
    
    # Planck acceleration (c²/length)
    acceleration_calc = constants.c**2 / length_calc
    
    # Planck pressure (force/area = c⁷/(hbarG²))
    pressure_calc = (constants.beta * constants.c**8 *2*np.pi) / ( constants.alpha**9)
    
    # Known values
    expected = {
        'Planck constant': 6.62607015e-34,
        'h_bar': 1.054571817e-34,
        'Gravitational constant': 6.67430e-11, 
        'Planck Length': 1.616255e-35,
        'Planck Time': 5.391247e-44,
        'Planck Mass': 2.176434e-8,
        'Planck Charge': 1.875545e-18,
        'Planck Temperature': 1.416784e32,
        "Planck angular momentum": 1.054571817e-34,
        'Planck energy': 1.9561125933147e+09,
        'Planck force': 1.2106590585939e+44,
        'Planck power': 3.6283154625583e+52,
        'Planck density': 5.1550074220287e+96,
        'Planck area': 2.6120569573458e-70,
        'Planck volume': 4.2241900034916e-105,
        'Planck acceleration': 5.5599586942113e+51,
        'Planck pressure': 4.63324611732735e+113,
        'Bolzmann Temperature': 1.380649e-23,
        'Epsilon_0 Temperature': 8.854187817e-12,
        'Fine Structure Constant': 0.0072973525693,
        'Gas Constant R': 8.31446261815324,
        'Stefan-Boltzmann': 5.670374419e-8,
        'von Klitzing RK': 25812.807,
    }
    
    # Calculate relative errors and return results
    results = {}
    calcs = {
        'Planck constant': h_calc,
        'h_bar': h_bar_calc,
        'Gravitational constant': G_calc, 
        'Planck Length': length_calc,
        'Planck Time'  : time_calc,
        'Planck Mass'  : mass_calc,
        'Planck Charge': charge_calc,
        'Planck Temperature': temp_calc,
        "Planck angular momentum": angular_momentum_calc,
        "Planck energy": energy_calc,
        "Planck force": force_calc,
        "Planck power": power_calc, 
        "Planck density": density_calc,
        "Planck area":  area_calc,
        "Planck volume": volume_calc,
        "Planck acceleration": acceleration_calc,
        "Planck pressure": pressure_calc,
 
        'Bolzmann Temperature': boltzmann_calc,
        'Epsilon_0 Temperature': e0_calc,
        'Fine Structure Constant': alphafine_calc,
        'Gas Constant R': r_gas_calc,
        'Stefan-Boltzmann': Kb_calc,
        'von Klitzing RK': RK_calc,
    }
    

    for name, exp_val in expected.items():
        calc_val = calcs[name]
        rel_error = abs((calc_val - exp_val) / exp_val)
        results[name] = (exp_val, calc_val, rel_error)
    
    return results

# Example usage and validation
if __name__ == "__main__":
    constants = PhysicsConstants()
    
    # Validate Planck units
    planck_results = validate_planck_units(constants)
    print("\nPlanck Units Validation:")
    print(f"Name                       | Expected        | Calculated      | Rel Error")
           #Planck constant            | 6.62607015e-34  | 6.62607015e-34  | 2.4524958
    print("-" * 80)
    for name, (expected, calculated, error) in planck_results.items():
        print(f"{name:<25}  | {expected:<15.8e} | {calculated:<15.8e} | {error:.20e}")
