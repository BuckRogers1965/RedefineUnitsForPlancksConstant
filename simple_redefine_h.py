import numpy as np

# this program demonstrates that h is just a constant K =hc  so that h = K/c
# No K is not a constant either.

# This is all just unit scaling as this program demostrates by scaling m, kg, and s.
 
# Initial constants
initial_h = 6.62607015e-34  # Planck's constant in J·s
initial_c = 299792458       # Speed of light in m/s
current_hc = initial_h * initial_c

def adjust_m_and_calculate(initial_h, initial_c, target_hc):
    meter_adjustment = np.cbrt(current_hc / target_hc) # Adjust meter factor
    new_c = initial_c / meter_adjustment               # New speed of light (c)
    new_h = initial_h / meter_adjustment**2            # New Planck's constant (h)
    return meter_adjustment,new_h, new_c

def adjust_kg_and_calculate(initial_h, initial_c, target_hc):
    kg_adjustment = current_hc / target_hc   # Adjust kilogram factor 
    new_h = initial_h / kg_adjustment        # New Planck's constant (h)
    return kg_adjustment,new_h, initial_c

def adjust_s_and_calculate(initial_h, initial_c, target_hc):
    second_adjustment = np.sqrt(current_hc /target_hc) # Adjust second factor
    new_c = initial_c / second_adjustment                  # New speed of light (c)
    new_h = initial_h / second_adjustment                  # New Planck's constant (h)
    return second_adjustment,new_h, new_c

def run_hc_calculations(target_hc_values):
    results = []
    units = ['m','kg','s']
    unit_functions = {
        'm': adjust_m_and_calculate,
        'kg': adjust_kg_and_calculate,
        's': adjust_s_and_calculate
    }

    for unit in units:
        print(f"\n\nRedefining units of {unit} to match specific values of hc\n")
        for target_hc in target_hc_values:
            print(f"\nCalculating for target hc = {target_hc:.12e}")
            
            if (current_hc == target_hc):
                unit_adjustment = 1
                final_h = initial_h
                final_c = initial_c
            else :
                if unit in unit_functions:
                    unit_adjustment, final_h, final_c = unit_functions[unit](initial_h, initial_c, target_hc)
            final_hc = final_h * final_c

            results.append({
                "target_hc": target_hc,
                "final_c": final_c,
                "final_h": final_h,
                "final_hc": final_hc,
                "relative_difference": abs(final_hc - target_hc) / target_hc
            })

            print(f"Results for target hc = {target_hc:.12e}")
            print(f"  new {unit}: { unit_adjustment:.12e} old {unit}")
            print(f"Final c: {final_c:.12e} m/s")
            print(f"Final h: {final_h:.12e} J·s")
            print(f"    1/c: {1/final_c:.12e} m/s")
            print(f"     hc: {final_h * final_c:.12e} J·m")
            print(f"Relative difference from target hc: {abs(final_hc - target_hc) / target_hc:.12e}")

# List of target hc values to calculate
#target_hc_values = [current_hc, 2e-25, 1e-25, 1e-24, 1.0]  # Example target hc values
target_hc_values = [1.0]  # Example target hc values

# Run the calculations for each target hc value
run_hc_calculations(target_hc_values)
