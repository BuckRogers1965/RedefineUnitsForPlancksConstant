from decimal import Decimal as D, getcontext, Context, ROUND_DOWN
from typing import Dict, Tuple

'''
    This program calculates the individual unit scaling
    factors for length, mass, temperature, and charge.

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
c   = D('299792458.0')     # speed of light
e_0 = D('8.854187817e-12') # epsilon_0
k_B = D('1.380649e-23')    # Boltzmann constant in J/K
pi  = D('3.141592653589793238462643383279502884197169399375105820974944592')

# Set precision to 50 D places
getcontext().prec = 100

def calculate_unit_scaling():

    # isolate all the base scaling factors

    # Original constants
    h = D('6.62607015e-34')
    G = D('6.67430e-11')

    # Calculate original hc
    hc = h * c

    # this scales the kg and meter so that hc = G = 1
    s_mass   = (hc / G).sqrt()                  # Calculate new hc with scaled kg so that hc = G
    s_length =  hc / s_mass                      # Dividing by kg_scale because hc has kg in numerator

   # exploring a more geometric basis for these factors
    isl = 1/s_length
    factor1 = isl/ c**2
    #print (f" *** {pi-factor}")
    #print (f" *** {pi/factor}")
    #print (f" *** {factor/pi}")
    #print (f" *** {pi -(4-pi)/10}")
    #print (f" *** factor1 = {factor1}")
    #factor = pi -(4-pi)/10 
    #x = factor-factor1
    #print (f" *   factor  = {factor}")
    #print (f" *   f-f1    = {factor-factor1}")
    #print (f" ***    x    = {x}")
    #factor = pi -(4-pi)/10 - x
    #s_length = (1/ (factor * c**2))
    #s_mass   = hc / s_length                  # Calculate new hc with scaled kg so that hc = G
    #print()
 
    # what happens if we scale the meter or the mass to make these scaling factors1?
    # We would also have to scale all the units that use the meter or kg to rescale them as well. 
    #s_length = D(1.0000000000000001)
    #s_mass  = D(1.0000000000000001)

    # convert to american measuremetns
    #s_length = s_length * D(39.3701) #inches
    #s_mass   = s_mass   * D(2.20462) # pounds


    # solve for the unknowns
    s_temp   = (s_length * s_mass) / k_B     
    s_charge = (s_length * s_mass * e_0).sqrt() 

    return s_length, s_mass, s_temp, s_charge

# Decimal_power
def d_p(base: D, exponent: D) -> D:
    """Raise a D to a power using high-precision arithmetic."""
    if base == 0 and exponent == 0:
        raise ValueError("0**0 is undefined")
    elif base < 0:
        raise ValueError("Negative bases with fractional exponents are not supported.")
    else:
        # Using `ln()` and `exp()` to perform precise power calculation
        return (base.ln() * exponent).exp()

def validate_planck_units(s_length, s_mass, s_temp, s_charge) -> Dict[str, Tuple[D, D, D]]:
    e         = D('1.602176634e-19')
    m_e       = D('9.1093837139e-31')  # kg electron mass
    m_p       = D('1.67262192595e-27') # kg proton mass
    N_A       = D('6.02214076e23')     # mol^−1 Avogadro constant

    # the following 4 are set in main from the output of the calculate_unit_scaling() funtion above

    # s_length length (m)
    # s_mass  mass (kg)
    # s_temp temperature (K)
    # s_charge charge (C)
    
    hc_calc      = (s_length * s_mass)
    h_calc       = (s_length * s_mass) / c
    h_bar_calc   = (s_length * s_mass) / (D(2) * pi * c)
    G_calc       =  s_length / s_mass
    length_calc  =  s_length / (d_p(D(2) * pi, D('0.5')) * d_p(c, D(2)))
    time_calc    =  s_length / (d_p(D(2) * pi, D('0.5')) * d_p(c, D(3)))
    charge_calc  =  s_charge * d_p(D(2), D('0.5'))
    temp_calc    =  d_p(c, D(2)) * s_temp / (d_p(D(2) * pi, D('0.5')) * s_length)
    angular_momentum_calc = h_calc / (D(2) * pi)
    mass_calc      = s_mass                            / d_p(D(2) * pi, D('0.5'))
    #momentun_calc = d_p(((h_bar_calc * c* c* c)       /G_calc), D(0.5))
    #momentun_calc = d_p((((s_length * s_mass) / (D(2) * pi * c) * c* c* c)/(s_length / s_mass)), D(0.5))
    momentun_calc  = s_mass * c                        / d_p((D(2) * pi ), D(0.5))
    energy_calc    = s_mass * d_p(c, D(2))             / d_p((D(2) * pi), D(0.5))
    force_calc     = s_mass * d_p(c, D(4))             / s_length
    power_calc     = s_mass * d_p(c, D(5))             / s_length
    density_calc   = s_mass * d_p(c, D(6)) * D(2) * pi / d_p(s_length, D(3))
    pressure_calc  = s_mass * d_p(c, D(8)) * D(2) * pi / d_p(s_length, D(3))
    area_calc      = d_p(length_calc, D(2))
    volume_calc    = d_p(length_calc, D(3))
    acceleration_calc = d_p(c, D(2)) / length_calc

    alpha_calc   = d_p(e, D(2)) / (D(2) * d_p(s_charge, D(2)))
    boltzmann_calc = s_length * s_mass / s_temp
    Phi_0_calc   =  (s_length * s_mass)     / (c *D(2) * e)
    Z_0_calc     =  (s_length * s_mass)     / (c * d_p(s_charge, D(2)) )
    qof_calc     =  (s_length * s_mass)     / (c*D(2) * m_e)
    mu_B_calc    =  (s_length * s_mass) * e / (D(4) * pi * c * m_e)
    mu_N_calc    =  (s_length * s_mass) * e / (D(4) * pi * c * m_p)
    r_e_calc     =  (s_length * s_mass) * alpha_calc / (m_e * c * D(2) * pi * c)
    r_gas_calc   =   s_length * s_mass * N_A / s_temp
    RK_calc      =   s_length * s_mass       / (d_p(e, D(2)) * c)
    a_0_calc     =  (s_length * s_mass * d_p(s_charge, D(2))) / ( pi *d_p(c * e, D(2)) * m_e)
    e0_calc      = d_p(s_charge, D(2))       / (s_length * s_mass)
    Kb_calc      = d_p(pi, D(5)) * D(2) * (s_length * s_mass / d_p(s_temp, D(4))) * c / D(15)
    R_inf_calc  = (d_p(e, D(4)) * d_p(c, D(2)) * m_e)/(D(8) * s_length * s_mass *  d_p(s_charge, D(4)) )
    K_J_calc    = (D(2) * e*c)/(s_mass*s_length)     # 2e/h
    c_1_calc    =  D(2) * pi * s_length * s_mass * c
    c_1L_calc   =  D(2) * s_length * s_mass * c
    #c_2_calc   =     (h_calc * c)  / (boltzmann_calc)
    #c_2_calc   = s_length * s_mass / (s_length * s_mass / s_temp)
    c_2_calc    =  s_temp
    G_0_calc    = (D(2) * d_p(e, D(2)) * c) / (s_length * s_mass)       # 2 e^2 / h
    mu_0_calc   =  D(2) *  alpha_calc * s_length * s_mass / (d_p(e, D(2)) * c *  c)
    #sigma_e_calc = (D(8) * pi/ D(3))* d_p(r_e, D(2))
    E_h_calc      = d_p(e, D(4)) * m_e* d_p(c, D(2))/ (D(4) * d_p(s_charge, D(4)))

    # This works, but the 9.8 seems to be arbitrary
    cosmo_calc    = d_p(s_length, D(3) )/( s_temp * pi* D(9.8))

    '''
    Ry_calc = R_inf ((s_length * s_mass) / c) c = E_h/2}
        'Rydberg unit of energy': Ry_calc,
        'Rydberg unit of energy':         D('2.1798723611030e−18'), # J

    fcc_calc = G_F / (((s_length * s_mass) / (D(2) * pi * c)) c)^3
        'Fermi coupling constant': fcc_calc,
        'Fermi coupling constant':         D('1.1663787e−5'), # GeV−2	
    '''

    expected = {
        'hc':                      D('1.9864458571489287e-25'),
        'Planck constant':         D('6.62607015e-34'),
        'h_bar':                   D('1.054571817e-34'),
        'Gravitational constant':  D('6.67430e-11'),
        'Planck Length':           D('1.616255e-35'),
        'Planck Time':             D('5.391247e-44'),
        'Planck Mass':             D('2.176434e-8'),
        'Planck Charge':           D('1.875545e-18'),
        'Planck Temperature':      D('1.416784e32'),
        "Planck angular momentum": D('1.054571817e-34'),
        'Planck momentum':         D('6.5249'),
        'Planck energy':           D('1.9561e+09'),
        'Planck force':            D('1.2103e+44'),
        'Planck power':            D('3.6283e+52'),
        'Planck density':          D('5.1550e+96'),
        'Planck area':             D('2.6121e-70'),
        'Planck volume':           D('4.2217e-105'),
        'Planck acceleration':     D('5.5608e+51'),
        'Planck pressure':         D('4.6332e+113'),
        'Bolzmann Temperature':    D('1.380649e-23'),
        'Epsilon_0 Temperature':   D('8.854187817e-12'),
        'Fine Structure Constant': D('0.0072973525693'),
        'Gas Constant R':          D('8.31446261815324'),
        'Stefan-Boltzmann':        D('5.670374419e-8'),
        'von Klitzing RK':         D('25812.807'),
        'Josephson constant':      D('483597.8484e9'), 
        'conductance quantum':     D('7.748091729e-5'), # S
        'first radiation':         D('3.741771852e-16'), # W⋅m
        'first radiation sr':      D('1.191042972e-16'), # W⋅m2⋅sr−1	
        'second radiation':        D('1.438776877e-2'), # m⋅K
        'magnetic flux quantum':   D('2.067833848e-15'), # Wb
        'Rydberg constant':         D('10973731.568157'), # m^−1
        'vacuum magnetic permeability':  D('1.25663706127e-6'), # N⋅A−2
        'character impedance vacuum': D('376.730313412'), # Ω
        'quantum of circulation':   D('3.6369475467e-4'), # m2⋅s−1	
        'Bohr magneton':            D('9.2740100657e-24'), # J⋅T−1
        'nuclear magneton':         D('5.0507837393e-27'), # J⋅T−1
        'classical electron radius':D('2.8179403205e-15'), # m
        #'Thomson cross section':   D('6.6524587051e-29'), # m^2
        'Bohr radius':              D('5.29177210544e-11'), # m
        'Hartree energy':           D('4.3597447222060e-18'), # J

   #in-progress
        'cosmological' :           D('1.089e-52'),
    }

    calcs = {
        'hc': hc_calc,
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
        'Fine Structure Constant': alpha_calc,
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
        'character impedance vacuum': Z_0_calc,
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
        #ratio = ( exp_val / calc_val)
        results[name] = (exp_val, calc_val, rel_error)
        #results[name] = (exp_val, calc_val, rel_error, ratio)

    return results

if __name__ == "__main__":
    s_length, s_mass, s_temp, s_charge  = calculate_unit_scaling()
    # Print the result with high precision
    print(f"s_length: {s_length:.50e} m    length unit scaling")
    print(f"s_mass  : {s_mass:.50e} kg   mass unit scaling")
    print(f"s_temp  : {s_temp:.50e} K^-1 temperature unit scaling")
    print(f"s_charge: {s_charge:.50e} C   charge unit scaling")

    
    # Validate Planck units
    planck_results = validate_planck_units(s_length, s_mass, s_temp, s_charge)
    
    print("\nPlanck Units Validation:")
    print(f"{'Name':<28} | {'Expected':<20} | {'Calculated':<22} | {'Rel Error'}")
    print("-" * 108)
    
    for name, (expected, calculated, error) in planck_results.items():
    #for name, (expected, calculated, error, ratio) in planck_results.items():
        print(f"{name:<28} | {expected:<20} | {calculated:<22.16e} | {error:<12.6e} ")
        #print(f"{name:<28} | {expected:<20} | {calculated:<22.16e} | {error:<12.6e} | {ratio:.6e}")
