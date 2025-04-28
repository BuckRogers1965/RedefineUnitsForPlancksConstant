from decimal import Decimal as D, getcontext, Context, ROUND_DOWN
from typing import Dict, Tuple

'''
    This program calculates the individual unit scaling
    factors for length, mass, temperature, and charge.

    Then these constants are used to recreate all the
    other constants using these basic scaling factors 
    and other counting constants. 
    
    This framework introduces the concept of the
    Quantum of Relative Mass (Hz_kg) kg/J
    This is the physical mass of a photon at 1Hz.
    This constant directly relates mass to frequency.
    If you multiply Hz_kg by f you get a mass.
    If you divide a mass by Hz_kg you get an f.
    Both h and G encode this same value.

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

    # solve for the unknowns
    # Hz_kg    = G*(Hz_kg/(G_n).sqrt())/c^3 there are two ways to calcuate the same kg s value.
    Hz_kg    = h/c**2                      # kg/Hz
    K_Hz     =  k_B / (Hz_kg * c**2)       # Hz/K
    C_kg     =  1/c**2                     # kg/C
    s_grav   = (h*c/G)                     # kg^2

    # just exploring candela for now
    s_lum    = Hz_kg * D('540e12') * 683         # 683 lm/W @ 540e12 Hz

    return Hz_kg, K_Hz, C_kg, s_grav, s_lum

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

def validate_planck_units(Hz_kg, K_Hz, C_kg, s_grav, s_lum) -> Dict[str, Tuple[D, D, D]]:
    e         = D('1.602176634e-19')
    m_e       = D('9.1093837139e-31')  # kg electron mass
    m_pro     = D('1.67262192595e-27') # kg proton mass
    N_A       = D('6.02214076e23')     # mol^−1 Avogadro constant

    # the following 4 are set in main from the output of the calculate_unit_scaling() funtion above

    # K_Hz temperature (K)
    # C_kg charge (C)
    m_p =  d_p(s_grav, D('0.5'))
    amp_force = D('1e-7')  # N/A^2
    
    hc_calc      = Hz_kg * c**3
    h_calc       = Hz_kg * c**2
    h_bar_calc   = Hz_kg * c**2 / (2 * pi )
    p_calc       = Hz_kg * c
    m_calc       = Hz_kg 

    boltzmann_calc = K_Hz * Hz_kg * c**2
    sKb_calc       = 2 * pi**5 * K_Hz**4 * Hz_kg / 15 

    G = D('6.67430e-11')
    G_n          = G * Hz_kg / c**3
    G_calc       = G_n * c**3 / Hz_kg

    time_calc    = (G_n).sqrt() / d_p(2 * pi, D('0.5')) 
    time_calc_h  = (G_n).sqrt()  

    # the real unit scaling is non reduced planck time
    t_P          = time_calc_h     # s

    length_calc  = t_P * c   / d_p(2 * pi, D('0.5')) 
    length_calc_h= t_P * c         # m

    mass_calc    =  (Hz_kg/t_P) / d_p(2 * pi, D('0.5'))
    mass_calc_h  =  (Hz_kg/t_P)    # kg

    charge_calc   = d_p( Hz_kg * c / ( amp_force * 2 * pi) ,D('0.5'))
    charge_calc_h = d_p( Hz_kg * c /   amp_force           ,D('0.5'))

    temp_calc     = 1/(t_P *  K_Hz *  d_p( 2 * pi , D('.5')) ) 
    temp_calc_h   = 1/(t_P *  K_Hz ) 

    angular_momentum_calc = h_calc / (D(2) * pi)

    momentun_calc  = (Hz_kg / t_P) * c          / d_p((D(2) * pi ), D(0.5))
    momentun_calc_h= (Hz_kg / t_P) * c                        

    energy_calc    = Hz_kg * c**2 / (t_P * d_p((D(2) * pi), D(0.5)))
    energy_calc_h  = Hz_kg * c**2 / t_P              

    force_calc     = c    * Hz_kg / t_P**2
    power_calc     = c**2 * Hz_kg / t_P**2

    density_calc   = Hz_kg * D(2) * pi / (c**3 * t_P**4)
    density_calc_h = Hz_kg             / (c**3 * t_P**4)

    pressure_calc  = Hz_kg * D(2) * pi / (c * t_P**4)
    pressure_calc_h= Hz_kg             / (c * t_P**4)

    area_calc      = d_p(length_calc,   D(2))
    area_calc_h    = d_p(length_calc_h, D(2))

    volume_calc    = d_p(length_calc,   D(3))
    volume_calc_h  = d_p(length_calc_h, D(3))

    accel_calc   = c**2 / length_calc
    accel_calc_h = c**2 / length_calc_h

    e0_calc      = 1 / (D(4) * pi * amp_force * c**2)

    alpha_calc   = 2 * pi * e**2 * amp_force / (Hz_kg * c)

    Phi_0_calc   = Hz_kg * c**2 / (D(2) * e)

    Z_0_calc     = 4 * pi * amp_force * c 

    mu_N_calc    = Hz_kg * c**2 * e / (D(4) * pi  * m_pro)

    r_e_calc     = e**2  * amp_force / m_e 

    R_inf_calc   = e**4 * 2 * pi**2 * m_e  * amp_force**2/ (Hz_kg**3 * c**3  )

    a_0_calc     = Hz_kg**2 * c**2  / (e**2 * 4 * pi**2 * m_e  * amp_force)

    mu_0_calc    = 4 * pi * amp_force

    sigma_e_calc = D(8) * pi * e**4 * amp_force**2 / (m_e**2 * D('3')) 

    E_h_calc     = e**4 * 4 * pi**2 * m_e * amp_force**2/ Hz_kg**2 

    perm_calc    = C_kg / amp_force   

    k_e_calc     = c**2 * amp_force

    r_gas_calc   = N_A * K_Hz * Hz_kg * c**2 

    qof_calc     = Hz_kg * c**2 / (2 * m_e)

    mu_B_calc    = Hz_kg * c**2 * e / (D(4) * pi * m_e)

    RK_calc      = Hz_kg * c**2 / d_p(e, D(2))

    K_J_calc     = (D(2) * e)/(Hz_kg * c**2)     # 2e/h

    c_1_calc     = D(2) * pi * Hz_kg * c**4 # 2 pi h c*2

    c_1L_calc    = D(2) * Hz_kg * c**4

    c_2_calc     = c / K_Hz     # this is the frequency to wavelength formula

    G_0_calc     = (D(2) * d_p(e, D(2)) ) / (Hz_kg * c**2)       # 2 e^2 / h

    # I don't know what G_F is
    # G_F = D('417234426247025326870636.69797847952875786161157016416900')
    # fcc_calc = G_F / (m * c**3) / (D(2) * pi * c * c)**3
    # G_F / ( h_bar_calc * c)
    G_F = D('0.000011663787')/D('3.1630287251813683e+25')
    fcc_calc = G_F /( h_bar_calc * c)

    # Gravitational Coupling Constant 
    a_g_calc = m_e**2 *2 *pi *G_n / Hz_kg**2

    # This works, but seems to be arbitrary

    m_mu = D('1.883531627e-28')
    mu_N_MHz_per_T = D('7.622593229')
    ratio = (m_pro / m_mu) * mu_N_MHz_per_T  # Exact Decimal calculation

    #cosmo_calc    = Hz_kg  /D('67.69969994318372720770006537643662343702866096631202122886906444678266768354190691325562520461039036')
    cosmo_calc    = Hz_kg  /ratio
    #print (f"  D('{cosmo_calc/D('1.089E-52')}')")

    expected = {
        'Planck constant E at 1Hz':D('6.62607015e-34'),         # E at 1Hz': Joule-seconds (J⋅s)
        'hc':                      D('1.9864458571489287e-25'), # (J⋅m)
        'momentum at 1Hz':         D('2.2102190943042336e-42'), #'momentum at 1Hz': kilogram-meters per second (kg⋅m/s)
        'mass at 1Hz':             D('7.3724973238127079e-51'), # kilogram-seconds (kg⋅s)
        'h_bar':                   D('1.054571817e-34'),        # Joule-seconds (J⋅s)
        'Gravitational constant':  D('6.67430e-11'),            # meters cubed per kilogram per second squared (m³⋅kg⁻¹⋅s⁻²)
        'Gravitational Coupling':  D('1.752e-45'),              # (m³ kg⁻¹ s⁻²)*(kg²)/(kg⋅m²⋅s⁻¹)*(m⋅s⁻¹)=1 dimensionless

        '\nPlanck Length':           D('1.616255e-35'),           # meters (m)
        'Planck Length h':         D('4.05135054323e-35'),      # meters (m)
        'Planck Time':             D('5.391247e-44'),           # seconds (s)
        'Planck Time h':           D('1.3513850782846e-43'),    # seconds (s)
        'Planck Mass':             D('2.176434e-8'),            # kilograms (kg)
        'Planck Mass h':           D('5.45551186133E-8'),       # kilograms (kg)
        'Planck Charge':           D('1.875545e-18'),           # Coulombs (C)
        'Planck Charge h':         D('4.70129672995E-18'),      # Coulombs (C)
        'Planck Temperature':      D('1.416784e32'),            # Kelvin (K)
        'Planck Temperature h':    D('3.55135123991E+32'),      # Kelvin (K)
        "Planck angular momentum": D('1.054571817e-34'),        # Joule-seconds (J⋅s)
        'Planck momentum':         D('6.5249'),                 # kilogram-meters per second (kg⋅m/s)
        'Planck momentum h':       D('16.3552131056'),          # kilogram-meters per second (kg⋅m/s)
        'Planck energy':           D('1.9561e+09'),             # Joules (J)
        'Planck energy h':         D('4903169538.03'),             # Joules (J)
        'Planck force':            D('1.2103e+44'),             # Newtons (N) which is equivalent to kg⋅m/s²
        'Planck power':            D('3.6283e+52'),             # Watts (W) which is equivalent to J/s or kg⋅m²/s³
        'Planck density':          D('5.1550e+96'),             # kilograms per meter cubed ( kg/m ³)
        'Planck density h':        D('8.20419620181E+95'),             # kilograms per meter cubed ( kg/m ³)
        'Planck area':             D('2.6121e-70'),             # meters squared (m²)
        'Planck area h':           D('1.64134412242E-69'),             # meters squared (m²)
        'Planck volume':           D('4.2217e-105'),            # meters cubed (m³)
        'Planck volume h':         D('6.64966040199E-104'),            # meters cubed (m³)
        'Planck acceleration':     D('5.5608e+51'),             # meters per second squared (m/s²)
        'Planck acceleration h':   D('2.21840882231E+51'),             # meters per second squared (m/s²)
        'Planck pressure':         D('4.6332e+113'),            # Pascals (Pa) which is equivalent to N/m² or kg/(m ⋅s²)
        'Planck pressure h':       D('7.37356382375E+112'),            # Pascals (Pa) which is equivalent to N/m² or kg/(m ⋅s²)

        '\nBoltzmann Temperature':   D('1.380649e-23'),           # J/K
        'Gas Constant R':          D('8.31446261815324'),       # Joules per mole-Kelvin (J/(mol⋅K)) or (kg⋅m²)/(s²⋅mol⋅K)
        'Stefan-Boltzmann':        D('5.670374419e-8'),         # (W/(m²⋅K⁴)) or kg/(s ³⋅K⁴)
        'Rydberg constant':        D('10973731.568157'),        # m^−1
        'quantum of circulation':   D('3.6369475467e-4'),       # m2⋅s−1	
        'Bohr magneton':            D('9.2740100657e-24'),      # J⋅T−1
        'nuclear magneton':         D('5.0507837393e-27'),      # J⋅T−1
        'classical electron radius':D('2.8179403205e-15'),      # m
        'Bohr radius':              D('5.29177210544e-11'),     # m
        'Thomson cross section':    D('6.6524587051e-29'),      # m^2
        'cosmological' :            D('1.089e-52'),             # m⁻²
        'Fermi coupling constant':  D('1.1663787e-5'),          # GeV−2	

        '\nconductance quantum':     D('7.748091729e-5'),         # S
        'Hartree energy':           D('4.3597447222060e-18'),   # J
        'von Klitzing RK':         D('25812.807'),              # Ohms (Ω)
        'character impedance vacuum': D('376.730313412'),       # Ω
        'vacuum magnetic permeability':  D('1.25663706127e-6'), # N⋅A−2
        'permittivity':            D('1.112650056e-10'),       # F m−1
        'Josephson constant':      D('483597.8484e9'),          # Hertz per Volt (Hz/V) or s⁻¹/V
        'Epsilon_0 Charge':        D('8.854187817e-12'),        # C²⋅s²⋅kg⁻¹⋅m⁻³
        'magnetic flux quantum':   D('2.067833848e-15'),        # Wb
        'first radiation':         D('3.741771852e-16'),        # W⋅m
        'first radiation sr':      D('1.191042972e-16'),        # W⋅m2⋅sr−1	
        'second radiation':        D('1.438776877e-2'),         # m⋅K
        'Fine Structure Constant': D('0.0072973525693'),        # dimensionaless
        'electrostatic constant':  D('8.9875517862e9'),        # N m^2 C^-2
    }

    calcs = {
        'Planck constant E at 1Hz':h_calc,
        'hc':                     hc_calc,
        'momentum at 1Hz':        p_calc,
        'mass at 1Hz':            m_calc,
        'h_bar':                  h_bar_calc,
        'Gravitational constant': G_calc,
        'Gravitational Coupling': a_g_calc,

        '\nPlanck Length':        length_calc,
        'Planck Length h':        length_calc_h,
        'Planck Time':            time_calc,
        'Planck Time h':          time_calc_h,
        'Planck Mass':            mass_calc,
        'Planck Mass h':          mass_calc_h,
        'Planck Charge':          charge_calc,
        'Planck Charge h':        charge_calc_h,
        'Planck Temperature':     temp_calc,
        'Planck Temperature h':   temp_calc_h,
        "Planck angular momentum":angular_momentum_calc,
        'Planck momentum':        momentun_calc,
        'Planck momentum h':      momentun_calc_h,
        "Planck energy":          energy_calc,
        "Planck energy h":        energy_calc_h,
        "Planck force":           force_calc,
        "Planck power":           power_calc,
        "Planck density":         density_calc,
        "Planck density h":       density_calc_h,
        "Planck area":            area_calc,
        "Planck area h":          area_calc_h,
        "Planck volume":          volume_calc,
        "Planck volume h":        volume_calc_h,
        "Planck acceleration":    accel_calc,
        "Planck acceleration h":  accel_calc_h,
        "Planck pressure":        pressure_calc,
        "Planck pressure h":      pressure_calc_h,

        '\nBoltzmann Temperature':boltzmann_calc,
        'Gas Constant R':         r_gas_calc,
        'Stefan-Boltzmann':       sKb_calc,
        'quantum of circulation': qof_calc,
        'Bohr magneton':          mu_B_calc,
        'nuclear magneton':       mu_N_calc,
        'classical electron radius': r_e_calc, 
        'Bohr radius':            a_0_calc,
        'Thomson cross section':  sigma_e_calc,
        'cosmological' :          cosmo_calc,
        'Fermi coupling constant':fcc_calc,

        '\nconductance quantum':  G_0_calc,
        'Hartree energy':         E_h_calc,
        'von Klitzing RK':        RK_calc,
        'character impedance vacuum': Z_0_calc,
        'vacuum magnetic permeability': mu_0_calc,
        'permittivity':           perm_calc,
        'Josephson constant':     K_J_calc,
        'Epsilon_0 Charge':       e0_calc,      # C²⋅s²⋅kg⁻¹⋅m⁻³
        'Rydberg constant':       R_inf_calc,
        'magnetic flux quantum':  Phi_0_calc,
        'first radiation':        c_1_calc,
        'first radiation sr':     c_1L_calc,
        'second radiation':       c_2_calc,
        'Fine Structure Constant':alpha_calc,
        'electrostatic constant': k_e_calc,
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
    Hz_kg, K_Hz, C_kg, s_grav, s_lum  = calculate_unit_scaling()

    # Print the result with high precision
    print(f"Hz_kg    : {Hz_kg:.50e}  kg/Hz   mass of photon @ 1Hz Quanum of relative gravity")
    print(f"K_Hz     : {K_Hz:.50e}  Hz/K temperature unit scaling")
    print(f"C_kg     : {C_kg:.50e}  kg/C   charge unit scaling")
    print(f"s_grav   : {s_grav:.50e}  kg^2 unit of gravity scaling")
    print(f"s_lum    : {s_lum:.50e}  lm/W unit of candela scaling")
    
    # Validate Planck units
    planck_results = validate_planck_units(Hz_kg, K_Hz, C_kg, s_grav, s_lum)
    
    print("\nPlanck Units Validation:")
    print(f"{'Name':<28} | {'Expected':<20} | {'Calculated':<22} | {'Rel Error'}")
    print("-" * 108)
    
    for name, (expected, calculated, error) in planck_results.items():
        print(f"{name:<30} | {expected:<19.12} | {calculated:<19.12} | {error:<10.6e} ")
