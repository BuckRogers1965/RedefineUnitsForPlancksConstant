from decimal import Decimal, getcontext, Context, ROUND_DOWN
from dataclasses import dataclass
from typing import Dict, Tuple

# Set precision to 50 decimal places
getcontext().prec = 50

@dataclass
class PhysicsConstants:
    c: Decimal = Decimal('299792458.0')
    epsilon_0: Decimal = Decimal('8.854187817e-12')
    k_B: Decimal = Decimal('1.380649e-23')
    e: Decimal = Decimal('1.602176634e-19')
    mol: Decimal = Decimal('6.02214076e23')

    #alpha: Decimal = Decimal('1.53843945498419101549e-06')
    alpha: Decimal = Decimal('1.53843945498418988525651584231678083324584755185780e-6')
    #beta: Decimal = Decimal('5.45551186133462110058e-08')
    beta: Decimal = Decimal('5.45551186133462083261573179563841219265538485514280e-8')
    gamma: Decimal = Decimal('1.43877687750393380214667160154391159519906942314870e-2')
    #gamma: Decimal = Decimal('1.43877687750393716548e-02')
    delta: Decimal = Decimal('1.32621132205611059057563089920041186351594040760140e-18')
    #delta: Decimal = Decimal('1.32621132205611221308e-18')

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

    angular_momentum_calc = h_calc / (Decimal('2') * pi)
    energy_calc = decimal_pow(constants.beta, Decimal(2)) * decimal_pow(constants.c, Decimal(4)) / (Decimal('2') * pi)
    force_calc = constants.beta * decimal_pow(constants.c, Decimal(4)) / decimal_pow(constants.alpha, Decimal(3))
    power_calc = constants.beta * decimal_pow(constants.c, Decimal(5)) / decimal_pow(constants.alpha, Decimal(3))
    density_calc = constants.beta * decimal_pow(constants.c, Decimal(6)) * Decimal('2') * pi / decimal_pow(constants.alpha, Decimal(9))
    area_calc = decimal_pow(length_calc, Decimal(2))
    volume_calc = decimal_pow(length_calc, Decimal(3))
    acceleration_calc = decimal_pow(constants.c, Decimal(2)) / length_calc
    pressure_calc = constants.beta * decimal_pow(constants.c, Decimal(8)) * Decimal('2') * pi / decimal_pow(constants.alpha, Decimal(9))

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
    }

    results = {}
    for name, exp_val in expected.items():
        calc_val = calcs[name]
        rel_error = abs((calc_val - exp_val) / exp_val)
        results[name] = (exp_val, calc_val, rel_error)

    return results

if __name__ == "__main__":
    constants = PhysicsConstants()
    
    # Validate Planck units
    planck_results = validate_planck_units(constants)
    
    print("\nPlanck Units Validation:")
    print(f"{'Name':<25} | {'Expected':<20} | {'Calculated':<30} | {'Rel Error'}")
    print("-" * 108)
    
    for name, (expected, calculated, error) in planck_results.items():
        print(f"{name:<25} | {expected:<20} | {calculated:<30.20e} | {error:.10e}")

