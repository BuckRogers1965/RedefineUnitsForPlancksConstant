import numpy as np
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class PhysicsConstants:
    alpha: float = 1.53843951260968407858e-6  # length unit scaling
    beta: float  = 5.45551124829157414485e-8  # mass unit scaling
    c: float     = 299792458.0                # Speed of light (m/s)
    epsilon_0: float = 8.854187817e-12        # Vacuum permittivity (C^2/N·m^2)
    k_B: float   = 1.380649e-23               # Boltzmann constant (J/K)
    gamma        = 1.438776877504e-02         # K⁻¹ (temperature scaling) 
    delta        = 1.32621132205611221308e-18 # C (charge scaling)

def validate_planck_units(constants: PhysicsConstants) -> Dict[str, Tuple[float, float, float]]:
    """
    Validates that the scaling factors correctly reproduce Planck units
    """
    # Calculate Planck units using simplified formulas
    h_calc = (constants.alpha**3 * constants.beta) / constants.c
    G_calc = constants.alpha**3 / constants.beta
    length_calc = (constants.alpha**3) / ((2 * np.pi)**(1/2) * constants.c**2)
    time_calc = (constants.alpha**3) / ((2 * np.pi)**(1/2) * constants.c**3)
    mass_calc = constants.beta / (2 * np.pi)**(1/2)
    charge_calc = (2 * (constants.alpha**3) * constants.beta * constants.epsilon_0)**(1/2)
    temp_calc = (constants.c**2 * constants.beta) / ((2 * np.pi)**(1/2) * constants.k_B)
    boltzmann_calc = (constants.alpha**3 * constants.beta) / constants.gamma
    e0_calc = constants.delta**2 / (constants.alpha**3 * constants.beta) 
    charge2_calc = constants.delta *(2)**(1/2)
    temp2_calc = (constants.c**2 * constants.gamma) / ((2 * np.pi)**(1/2) * constants.alpha**3)
    
    # Known values
    expected = {
        'Planck constant': 6.62607015e-34,
        'Gravitational constant': 6.67430e-11, 
        'Planck Length': 1.616255e-35,
        'Planck Time': 5.391247e-44,
        'Planck Mass': 2.176434e-8,
        'Planck Charge': 1.875545e-18,
        'Planck Temperature': 1.416784e32,
        'Bolzmann Temperature': 1.380649e-23,
        'epsilon_0 Temperature': 8.854187817e-12,
        'Planck Charge2': 1.875545e-18,
        'Planck Temperature2': 1.416784e32,
    }
    
    # Calculate relative errors and return results
    results = {}
    calcs = {
        'Planck constant': h_calc,
        'Gravitational constant': G_calc, 
        'Planck Length': length_calc,
        'Planck Time'  : time_calc,
        'Planck Mass'  : mass_calc,
        'Planck Charge': charge_calc,
        'Planck Temperature': temp_calc,
        'Bolzmann Temperature': boltzmann_calc,
        'epsilon_0 Temperature': e0_calc,
        'Planck Charge2': charge2_calc,
        'Planck Temperature2': temp2_calc,
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
