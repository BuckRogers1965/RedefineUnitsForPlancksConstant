from decimal import Decimal, getcontext, Context, ROUND_DOWN
from dataclasses import dataclass
from typing import Dict, Tuple

'''
    This program calculates the individual unit scaling
    factors for length, mass, temperature, and charge.

    These scaling factors are assigned to constants.

    Then these constants are used to recreate all the
    other constants using these basic scaling factors 
    and other counting constants. 

    The scaling factors themselve are just half the equation.
    How the scaling factors relate to each other and the
    counting constants inside the constant is as important 
    as the presence of the scaling factor. 

    Counting constants are things that are counts of other thing.
    How many meters fit inside the distance light travels in a second?
    How many atoms are in a mole?
    How many electrons are in a coulomb? 
    These counting constants are used with the value they have in this framework. 
    
    This is a new field of Unit System Science. The ability to predict 
    the values that a new constant would have from how the units relate
    to each other upgrade unit analysis from descriptive to predictive.


    Author: James Rogers, SE Ohio, 26 Nov 2024 1824

'''

# Set precision to 50 decimal places
getcontext().prec = 50

#def decimal_pow(base, exp):
#    return base ** exp

def calculate_unit_scaling():
    """
    Analyze how hc and G relate when we scale kg to make their ratio 1
    """
    # Set the precision to 50 digits
    getcontext().prec = 50

    # Original constants
    h = Decimal('6.62607015e-34')
    c = Decimal('299792458')
    G = Decimal('6.67430e-11')
    k_B = Decimal('1.380649e-23')  # Boltzmann constant in J/K
    e0 = Decimal('8.854187817e-12')

    # Calculate original hc
    hc_original = h * c

    # Calculate the kg scaling factor from sqrt(hc/G)
    kg_scale = (hc_original / G).sqrt()

    # Calculate new hc with scaled kg so that hc = G
    hc_new = hc_original / kg_scale  # Dividing by kg_scale because hc has kg in numerator

    # Define scaling for meter) based on kg_scale and original constants
    # this scaled the meter so that hc = G = 1
    alpha = hc_new
    beta  = kg_scale
    gamma = (alpha * beta) / k_B
    delta = (alpha * beta * e0).sqrt()

    return alpha, beta, gamma, delta

@dataclass
class PhysicsConstants:
    c: Decimal = Decimal('299792458.0')
    epsilon_0: Decimal = Decimal('8.854187817e-12')
    k_B: Decimal = Decimal('1.380649e-23')
    e: Decimal = Decimal('1.602176634e-19')
    mol: Decimal = Decimal('6.02214076e23')
    m_e: Decimal = Decimal('9.1093837139e-31')  # kg electron mass
    m_p: Decimal = Decimal('1.67262192595e-27') # kg proton mass
    N_A: Decimal = Decimal('6.02214076e23')     # mol^−1 Avogadro constant

    # the following 4 are set in main from the output of the 
    # calculate_unit_scaling() funtion above

    # alpha length (m)
    # beta  mass (kg)
    # gamma temperature (K)
    # delta charge (C)

def decimal_pow(base: Decimal, exponent: Decimal) -> Decimal:
    """Raise a Decimal to a power using high-precision arithmetic."""
    if base == 0 and exponent == 0:
        raise ValueError("0**0 is undefined")
    elif base < 0:
        raise ValueError("Negative bases with fractional exponents are not supported.")
    else:
        # Using `ln()` and `exp()` to perform precise power calculation
        return (base.ln() * exponent).exp()

def validate_planck_units(constants: PhysicsConstants) -> Dict[str, Tuple[Decimal, Decimal, Decimal]]:
    pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592')
    
    h_calc = (constants.alpha * constants.beta) / constants.c
    h_bar_calc = (constants.alpha * constants.beta) / (Decimal('2') * pi * constants.c)
    G_calc = constants.alpha / constants.beta
    length_calc = constants.alpha / (decimal_pow(Decimal('2') * pi, Decimal('0.5')) * decimal_pow(constants.c, Decimal(2)))
    time_calc = constants.alpha / (decimal_pow(Decimal('2') * pi, Decimal('0.5')) * decimal_pow(constants.c, Decimal(3)))
    mass_calc = constants.beta / decimal_pow(Decimal('2') * pi, Decimal('0.5'))
    charge_calc = constants.delta * decimal_pow(Decimal('2'), Decimal('0.5'))
    temp_calc = decimal_pow(constants.c, Decimal(2)) * constants.gamma / (decimal_pow(Decimal('2') * pi, Decimal('0.5')) * constants.alpha)

    angular_momentum_calc = h_calc / (Decimal('2') * pi)

    #momentun_calc = decimal_pow(((h_bar_calc * constants.c* constants.c* constants.c)/G_calc), Decimal(0.5))
    #momentun_calc = decimal_pow((((constants.alpha * constants.beta) / (Decimal('2') * pi * constants.c) * constants.c* constants.c* constants.c)/(constants.alpha / constants.beta)), Decimal(0.5))
    momentun_calc=(constants.beta * constants.c) / decimal_pow((Decimal('2') * pi ), Decimal(0.5))
    energy_calc  = constants.beta * decimal_pow(constants.c, Decimal(2)) / decimal_pow((Decimal('2') * pi), Decimal(0.5))
    force_calc   = constants.beta * decimal_pow(constants.c, Decimal(4)) / constants.alpha
    power_calc   = constants.beta * decimal_pow(constants.c, Decimal(5)) / constants.alpha
    density_calc = constants.beta * decimal_pow(constants.c, Decimal(6)) * Decimal('2') * pi / decimal_pow(constants.alpha, Decimal(3))
    area_calc = decimal_pow(length_calc, Decimal(2))
    volume_calc = decimal_pow(length_calc, Decimal(3))
    acceleration_calc = decimal_pow(constants.c, Decimal(2)) / length_calc
    pressure_calc = constants.beta * decimal_pow(constants.c, Decimal(8)) * Decimal('2') * pi / decimal_pow(constants.alpha, Decimal(3))

    boltzmann_calc = constants.alpha * constants.beta / constants.gamma
    e0_calc = decimal_pow(constants.delta, Decimal(2)) / (constants.alpha * constants.beta)
    Kb_calc = Decimal('2') * decimal_pow(pi, Decimal(5)) * (constants.alpha * constants.beta / decimal_pow(constants.gamma, Decimal(4))) * constants.c / Decimal('15')
    alphafine_calc = decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))

    r_gas_calc = constants.beta * constants.alpha * constants.mol / constants.gamma

    RK_calc = constants.beta * constants.alpha / (decimal_pow(constants.e, Decimal(2)) * constants.c)
    R_inf_calc = (decimal_pow(constants.e, Decimal(4)) * decimal_pow(constants.c, Decimal(2)) * constants.m_e)/(Decimal('8') * constants.alpha * constants.beta *  decimal_pow(constants.delta, Decimal(4)) )
    # 2e/h
    K_J_calc = (Decimal('2') * constants.e*constants.c)/(constants.beta*constants.alpha)
    c_1_calc = Decimal('2') * pi * constants.alpha * constants.beta * constants.c
    c_1L_calc  = Decimal('2') * constants.alpha * constants.beta * constants.c
    #c_2_calc = (h_calc * constants.c) / (boltzmann_calc)
    #c_2_calc = ((constants.alpha * constants.beta) )
             # / (constants.alpha * constants.beta / constants.gamma)
    c_2_calc =  constants.gamma

    # G_0 = 2 e^2 / h
    G_0_calc = (Decimal('2') * decimal_pow(constants.e, Decimal(2)) * constants.c)/(constants.alpha * constants.beta)

    Phi_0_calc = (constants.alpha * constants.beta)/(constants.c *Decimal('2') * constants.e)


    #mu_0_calc =  Decimal('4') * pi *  alphafine_calc*  h_bar_calc/(decimal_pow(constants.e, Decimal(2)) * constants.c)
    mu_0_calc =  Decimal('4') * pi *  alphafine_calc* (constants.alpha * constants.beta) / (decimal_pow(constants.e, Decimal(2)) * constants.c * Decimal('2') * pi * constants.c)

    Z_0_calc = (constants.alpha * constants.beta) / (constants.c * decimal_pow(constants.delta, Decimal(2)) )

    qof_calc =  (constants.alpha * constants.beta) / (constants.c*Decimal('2') * constants.m_e)

    mu_B_calc = constants.e * (constants.alpha * constants.beta) / (Decimal('4') * pi * constants.c * constants.m_e)
    mu_N_calc = constants.e * (constants.alpha * constants.beta) / (Decimal('4') * pi * constants.c *constants.m_p)
    r_e_calc =  alphafine_calc * (constants.alpha * constants.beta) / (constants.m_e * constants.c * Decimal('2') * pi * constants.c)
    #r_e_calc = (decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))) ((constants.alpha * constants.beta) / (Decimal('2') * pi * constants.c)) / (m_e c)

    #sigma_e_calc = (Decimal('8') * pi/ Decimal('3'))* decimal_pow(constants.r_e, Decimal(2))
    a_0_calc = (constants.alpha * constants.beta * decimal_pow(constants.delta, Decimal(2))) / ( pi *decimal_pow(constants.c * constants.e, Decimal(2)) * constants.m_e)

    E_h_calc = decimal_pow(constants.e, Decimal(4)) * constants.m_e* decimal_pow(constants.c, Decimal(2))/ (Decimal('4') * decimal_pow(constants.delta, Decimal(4)))

    # This works, but the 9.8 seems to be arbitary
    cosmo_calc = decimal_pow(constants.alpha, Decimal(3) )/( constants.gamma * pi* Decimal('9.8'))

    '''
    Ry_calc = R_inf ((constants.alpha * constants.beta) / constants.c) c = E_h/2}
        'Rydberg unit of energy': Ry_calc,
        'Rydberg unit of energy':         Decimal('2.1798723611030e−18'), # J

    fcc_calc = G_F / (((constants.alpha * constants.beta) / (Decimal('2') * pi * constants.c)) c)^3
        'Fermi coupling constant': fcc_calc,
        'Fermi coupling constant':         Decimal('1.1663787e−5'), # GeV−2	
    '''

    expected = {
        'Planck constant':         Decimal('6.62607015e-34'),
        'h_bar':                   Decimal('1.054571817e-34'),
        'Gravitational constant':  Decimal('6.67430e-11'),
        'Planck Length':           Decimal('1.616255e-35'),
        'Planck Time':             Decimal('5.391247e-44'),
        'Planck Mass':             Decimal('2.176434e-8'),
        'Planck Charge':           Decimal('1.875545e-18'),
        'Planck Temperature':      Decimal('1.416784e32'),
        "Planck angular momentum": Decimal('1.054571817e-34'),
        'Planck momentum':         Decimal('6.5249'),
        'Planck energy':           Decimal('1.9561e+09'),
        'Planck force':            Decimal('1.2103e+44'),
        'Planck power':            Decimal('3.6283e+52'),
        'Planck density':          Decimal('5.1550e+96'),
        'Planck area':             Decimal('2.6121e-70'),
        'Planck volume':           Decimal('4.2217e-105'),
        'Planck acceleration':     Decimal('5.5608e+51'),
        'Planck pressure':         Decimal('4.6332e+113'),
        'Bolzmann Temperature':    Decimal('1.380649e-23'),
        'Epsilon_0 Temperature':   Decimal('8.854187817e-12'),
        'Fine Structure Constant': Decimal('0.0072973525693'),
        'Gas Constant R':          Decimal('8.31446261815324'),
        'Stefan-Boltzmann':        Decimal('5.670374419e-8'),
        'von Klitzing RK':         Decimal('25812.807'),
        'Josephson constant':      Decimal('483597.8484e9'), 
        'conductance quantum':     Decimal('7.748091729e-5'), # S
        'first radiation':         Decimal('3.741771852e-16'), # W⋅m
        'first radiation sr':      Decimal('1.191042972e-16'), # W⋅m2⋅sr−1	
        'second radiation':        Decimal('1.438776877e-2'), # m⋅K
        'magnetic flux quantum':   Decimal('2.067833848e-15'), # Wb
        'Rydberg constant':         Decimal('10973731.568157'), # m^−1
        'vacuum magnetic permeability':  Decimal('1.25663706127e-6'), # N⋅A−2
        'characteristic impedance of vacuum': Decimal('376.730313412'), # Ω
        'quantum of circulation':   Decimal('3.6369475467e-4'), # m2⋅s−1	
        'Bohr magneton':            Decimal('9.2740100657e-24'), # J⋅T−1
        'nuclear magneton':         Decimal('5.0507837393e-27'), # J⋅T−1
        'classical electron radius':Decimal('2.8179403205e-15'), # m
        #'Thomson cross section':   Decimal('6.6524587051e-29'), # m^2
        'Bohr radius':              Decimal('5.29177210544e-11'), # m
        'Hartree energy':           Decimal('4.3597447222060e-18'), # J

   #in-progress
        'cosmological' :           Decimal('1.089e-52'),
    }

    calcs = {
        'Planck constant': h_calc,
        'h_bar': h_bar_calc,
        'Gravitational constant': G_calc,
        'Planck Length': length_calc,
        'Planck Time': time_calc,
        'Planck Mass': mass_calc,
        'Planck Charge': charge_calc,
        'Planck Temperature': temp_calc,
        "Planck angular momentum": angular_momentum_calc,
        'Planck momentum': momentun_calc,
        "Planck energy": energy_calc,
        "Planck force": force_calc,
        "Planck power": power_calc,
        "Planck density": density_calc,
        "Planck area": area_calc,
        "Planck volume": volume_calc,
        "Planck acceleration": acceleration_calc,
        "Planck pressure": pressure_calc,
        'Bolzmann Temperature': boltzmann_calc,
        'Epsilon_0 Temperature': e0_calc,
        'Fine Structure Constant': alphafine_calc,
        'Gas Constant R': r_gas_calc,
        'Stefan-Boltzmann': Kb_calc,
        'von Klitzing RK': RK_calc,
        'Josephson constant': K_J_calc,
        'conductance quantum': G_0_calc,
        'first radiation': c_1_calc,
        'first radiation sr': c_1L_calc,
        'second radiation': c_2_calc,
        'magnetic flux quantum': Phi_0_calc,
        'Rydberg constant': R_inf_calc,
        'vacuum magnetic permeability': mu_0_calc,
        'characteristic impedance of vacuum': Z_0_calc,
        'quantum of circulation': qof_calc,
        'Bohr magneton': mu_B_calc,
        'nuclear magneton': mu_N_calc,
        'classical electron radius': r_e_calc, 
        #'Thomson cross section': sigma_e_calc,
        'Bohr radius': a_0_calc,
        'Hartree energy': E_h_calc,

   #in-progress
        'cosmological' : cosmo_calc,
    }

    results = {}
    for name, exp_val in expected.items():
        calc_val = calcs[name]
        rel_error = abs((calc_val - exp_val) / exp_val)
        results[name] = (exp_val, calc_val, rel_error)

    return results

if __name__ == "__main__":
    alpha, beta, gamma, delta  = calculate_unit_scaling()
    # Print the result with high precision
    print(f"alpha: {alpha:.50e} m    length unit scaling")
    print(f"beta : {beta:.50e} kg   mass unit scaling")
    print(f"gamma: {gamma:.50e} K^-1 temperature unit scaling")
    print(f"delta: {delta:.50e} C   charge unit scaling")

    constants = PhysicsConstants()

    # Update the PhysicsConstants class with calculated values
    PhysicsConstants.alpha = alpha # length (m)
    PhysicsConstants.beta  = beta  # mass (kg)
    PhysicsConstants.gamma = gamma # temperature (K)
    PhysicsConstants.delta = delta # charge (C)

    
    # Validate Planck units
    planck_results = validate_planck_units(constants)
    
    print("\nPlanck Units Validation:")
    print(f"{'Name':<25} | {'Expected':<20} | {'Calculated':<30} | {'Rel Error'}")
    print("-" * 108)
    
    for name, (expected, calculated, error) in planck_results.items():
        print(f"{name:<25} | {expected:<20} | {calculated:<30.20e} | {error:.10e}")
