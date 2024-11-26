from decimal import Decimal, getcontext, Context, ROUND_DOWN
from dataclasses import dataclass
from typing import Dict, Tuple

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
    alpha = decimal_pow(hc_new, Decimal(Decimal('1')/Decimal('3')))
    beta  =  kg_scale
    gamma = (alpha ** 3 * beta) / k_B
    delta = (alpha ** 3 * beta * e0).sqrt()

    return alpha, beta, gamma, delta

@dataclass
class PhysicsConstants:
    c: Decimal = Decimal('299792458.0')
    epsilon_0: Decimal = Decimal('8.854187817e-12')
    k_B: Decimal = Decimal('1.380649e-23')
    e: Decimal = Decimal('1.602176634e-19')
    mol: Decimal = Decimal('6.02214076e23')

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
    
    h_calc = (decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / constants.c
    h_bar_calc = (decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)
    G_calc = decimal_pow(constants.alpha, Decimal(3)) / constants.beta
    length_calc = decimal_pow(constants.alpha, Decimal(3)) / (decimal_pow(Decimal('2') * pi, Decimal('0.5')) * decimal_pow(constants.c, Decimal(2)))
    time_calc = decimal_pow(constants.alpha, Decimal(3)) / (decimal_pow(Decimal('2') * pi, Decimal('0.5')) * decimal_pow(constants.c, Decimal(3)))
    mass_calc = constants.beta / decimal_pow(Decimal('2') * pi, Decimal('0.5'))
    charge_calc = constants.delta * decimal_pow(Decimal('2'), Decimal('0.5'))
    temp_calc = decimal_pow(constants.c, Decimal(2)) * constants.gamma / (decimal_pow(Decimal('2') * pi, Decimal('0.5')) * decimal_pow(constants.alpha, Decimal(3)))

    boltzmann_calc = decimal_pow(constants.alpha, Decimal(3)) * constants.beta / constants.gamma
    e0_calc = decimal_pow(constants.delta, Decimal(2)) / (decimal_pow(constants.alpha, Decimal(3)) * constants.beta)
    Kb_calc = Decimal('2') * decimal_pow(pi, Decimal(5)) * (decimal_pow(constants.alpha, Decimal(3)) * constants.beta / decimal_pow(constants.gamma, Decimal(4))) * constants.c / Decimal('15')
    alphafine_calc = decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))

    r_gas_calc = constants.beta * decimal_pow(constants.alpha, Decimal(3)) * constants.mol / constants.gamma

    RK_calc = constants.beta * decimal_pow(constants.alpha, Decimal(3)) / (decimal_pow(constants.e, Decimal(2)) * constants.c)
    # 2e/h
    K_J_calc = (Decimal('2') * constants.e*constants.c)/(constants.beta*decimal_pow(constants.alpha,Decimal(3)))

    angular_momentum_calc = h_calc / (Decimal('2') * pi)
    energy_calc = constants.beta * decimal_pow(constants.c, Decimal(2)) / decimal_pow((Decimal('2') * pi), Decimal(0.5))
    force_calc = constants.beta * decimal_pow(constants.c, Decimal(4)) / decimal_pow(constants.alpha, Decimal(3))
    power_calc = constants.beta * decimal_pow(constants.c, Decimal(5)) / decimal_pow(constants.alpha, Decimal(3))
    density_calc = constants.beta * decimal_pow(constants.c, Decimal(6)) * Decimal('2') * pi / decimal_pow(constants.alpha, Decimal(9))
    area_calc = decimal_pow(length_calc, Decimal(2))
    volume_calc = decimal_pow(length_calc, Decimal(3))
    acceleration_calc = decimal_pow(constants.c, Decimal(2)) / length_calc
    pressure_calc = constants.beta * decimal_pow(constants.c, Decimal(8)) * Decimal('2') * pi / decimal_pow(constants.alpha, Decimal(9))

    c_1_calc = Decimal('2') * pi * decimal_pow(constants.alpha, Decimal(3)) * constants.beta * constants.c
    c_1L_calc  = (Decimal('2') * decimal_pow(constants.alpha, Decimal(3)) * constants.beta * constants.c)
    #c_2_calc = (h_calc * constants.c) / (boltzmann_calc)
    #c_2_calc = ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) )
             # / (decimal_pow(constants.alpha, Decimal(3)) * constants.beta / constants.gamma)
    c_2_calc =  constants.gamma

    # G_0 = 2 e^2 / h
    G_0_calc = (Decimal('2') * decimal_pow(constants.e, Decimal(2)) * constants.c)/(decimal_pow(constants.alpha, Decimal(3)) * constants.beta)

    Phi_0_calc = (decimal_pow(constants.alpha, Decimal(3)) * constants.beta)/(constants.c *Decimal('2') * constants.e)

    #inprogress
    #cosmo_calc = decimal_pow(constants.alpha, Decimal(9) ) / Decimal(9) * pi**3

    '''
    b_e
        'Wien wavelength displacement': 
        'Wien wavelength displacement':         Decimal('2.897771955e-3'), # m⋅K

    b_f
        'Wien frequency displacement':
        'Wien frequency displacement':         Decimal('5.878925757e10'), # Hz⋅K−1

    b_{\text{entropy}}}
        'Wien entropy displacement':
        'Wien entropy displacement':         Decimal('3.002916077e−3'), # m⋅K



    mu_0 = 4pi (decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))
) ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)) /e^2c}
        'vacuum magnetic permeability':
        'vacuum magnetic permeability':         Decimal('1.25663706127e−6'), # N⋅A−2

    Z_0=4pi (decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))
) ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)) /e^2
        'characteristic impedance of vacuum':
        'characteristic impedance of vacuum':         Decimal('376.730313412'), # Ω

    epsilon_0 = e^2/4pi (decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))
) ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)) c}
        'vacuum electric permittivity':
        'vacuum electric permittivity':         Decimal('8.8541878188e−12'), # F⋅m−1


    ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / constants.c)/2m_e
        'quantum of circulation':
        'quantum of circulation':         Decimal('3.6369475467'), # m2⋅s−1	

    mu_B=e ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)) 2m_e
        'Bohr magneton':
        'Bohr magneton':         Decimal('9.2740100657e−24'), # J⋅T−1

    mu_N = e ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)) / 2m_p
        'nuclear magneton':
        'nuclear magneton':         Decimal('5.0507837393e−27'), # J⋅T−1

    r_e = (decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))
) ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)) / (m_e c)
        'classical electron radius':
        'classical electron radius':         Decimal('2.8179403205e−15'), # m

    sigma_e = (8pi/3)r_e^2
        'Thomson cross section':
        'Thomson cross section':         Decimal('6.6524587051e−29'), # m^2

    a_0 = ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)) / (decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))
 ) m_e c
        'Bohr radius':
        'Bohr radius':         Decimal('29177210544e−11'), # m

    R_inf = ((decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))
)^2 m_e c) / (2 ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / constants.c) )
        'Rydberg constant':
        'Rydberg constant':         Decimal('10973731.568157'), # m^−1

    Ry = R_inf ((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / constants.c) c = E_h/2}
        'Rydberg unit of energy':
        'Rydberg unit of energy':         Decimal('2.1798723611030e−18'), # J

    E_h = decimal_pow(constants.e, Decimal(2)) / (Decimal('2') * decimal_pow(constants.delta, Decimal(2)))
^2 m_e c^2
        'Hartree energy':
        'Hartree energy':         Decimal('4.3597447222060e−18'), # J

    G_F / (((decimal_pow(constants.alpha, Decimal(3)) * constants.beta) / (Decimal('2') * pi * constants.c)) c)^3
        'Fermi coupling constant':
        'Fermi coupling constant':         Decimal('1.1663787e−5'), # GeV−2	

    N_A
        'Avogadro constant':
        'Avogadro constant':         Decimal('6.02214076e23'), # mol^−1	

    R=N_A k_B
        'molar gas constant':
        'molar gas constant':         Decimal('8.31446261815324 '), # J⋅mol−1⋅K−1

    F=N_A e
        'Faraday constant':
        'Faraday constant':         Decimal('96485.3321233100184'), # C⋅mol−1	

    N_A h
        'molar Planck constant':
        'molar Planck constant':         Decimal('3.9903127128934314e−10'), # J⋅s⋅mol−1

    M(12C)=N_A m (12 C)
        'molar mass of carbon-12':
        'molar mass of carbon-12':         Decimal('12.0000000126e−3'), # kg⋅mol−1

    m_u=m(12 C)/12
        'atomic mass constant':
        'atomic mass constant':         Decimal('1.66053906892e−27'), # kg

    M_u=M(12 C)/12
        'molar mass constant':
        'molar mass constant':         Decimal('1.00000000105e−3'), # kg⋅mol−1	

    V_m(Si)
        'molar volume of silicon':
        'molar volume of silicon':         Decimal('1.205883199e−5'), # m3⋅mol−1

    Delta nu _Cs
        'hyperfine transition frequency of 133Cs':
        'hyperfine transition frequency of 133Cs':         Decimal('9192631770'), # Hz

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
        'Planck energy':           Decimal('1.95611259e+09'),
        'Planck force':            Decimal('1.21065905e+44'),
        'Planck power':            Decimal('3.62831546e+52'),
        'Planck density':          Decimal('5.15500742e+96'),
        'Planck area':             Decimal('2.61205695e-70'),
        'Planck volume':           Decimal('4.22419000e-105'),
        'Planck acceleration':     Decimal('5.55995869e+51'),
        'Planck pressure':         Decimal('4.63324611e+113'),
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

   #in-progress
        # 'cosmological' :           Decimal('1.089e-52'),
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

   #in-progress
        #'cosmological' : cosmo_calc,
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

