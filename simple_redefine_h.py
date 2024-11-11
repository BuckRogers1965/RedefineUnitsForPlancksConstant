import numpy as np

# this program demonstrates that h is just a constant K =hc  so that h = K/c
# No K is not a constant either.
# This is all just unit scaling as this program demostrates by scaling both m and kg.

# I realized that hc would change as the cube root of the change to the meter 
# and everything got much easier. 

# Also now showing how changing the unit definiton of the kg would directly change h and hc togeher. 

# Initial constants
initial_h = 6.62607015e-34  # Planck's constant in J·s
initial_c = 299792458       # Speed of light in m/s
initial_hc = initial_h * initial_c

def adjust_meter_and_calculate(initial_h, initial_c, target_hc):
    # Calculate current hc
    current_hc = initial_h * initial_c
    
    # Adjust meter factor based on the cube root of the difference
    meter_adjustment = np.cbrt(current_hc / target_hc)
    
    # New speed of light (c)
    new_c = initial_c / meter_adjustment
    
    # New Planck's constant (h)
    new_h = target_hc / new_c
    
    return meter_adjustment,new_h, new_c

def run_hc_calculations(target_hc_values):
    results = []
    print(f"Redefining the meter to match specific values of hc\n")
    for target_hc in target_hc_values:
        print(f"\nCalculating for target hc = {target_hc:.12e}")
        
        meter_adjustment, final_h, final_c = adjust_meter_and_calculate(initial_h, initial_c, target_hc)
        final_hc = final_h * final_c
        
        results.append({
            "target_hc": target_hc,
            "final_c": final_c,
            "final_h": final_h,
            "final_hc": final_hc,
            "relative_difference": abs(final_hc - target_hc) / target_hc
        })
        
        print(f"Results for target hc = {target_hc:.12e}")
        print(f"  new m: { meter_adjustment:.12e} m/s")
        print(f"Final c: {final_c:.12e} m/s")
        print(f"Final h: {final_h:.12e} J·s")
        print(f"    1/c: {1/final_c:.12e} m/s")
        print(f"     hc: {final_h * final_c:.12e} J·m")
        print(f"Relative difference from target hc: {abs(final_hc - target_hc) / target_hc:.12e}")
    
    return results

def adjust_kg_and_calculate(initial_h, initial_c, target_hc):
    # Calculate current hc
    current_hc = initial_h * initial_c

    # Calculate the difference
    difference = current_hc / target_hc

    # Adjust meter factor based on the cube root of the difference
    kg_adjustment = difference

    # New speed of light (c)
    new_h = initial_h / kg_adjustment

    return kg_adjustment,new_h, initial_c

def run_hc_calculations_kg(target_hc_values):
    results = []
    print(f"\n\nRedefining the kilogram to match specific values of hc\n")
    for target_hc in target_hc_values:
        print(f"\nCalculating for target hc = {target_hc:.12e}")

        kg_adjustment, final_h, final_c = adjust_kg_and_calculate(initial_h, initial_c, target_hc)
        final_hc = final_h * final_c

        results.append({
            "target_hc": target_hc,
            "final_c": final_c,
            "final_h": final_h,
            "final_hc": final_hc,
            "relative_difference": abs(final_hc - target_hc) / target_hc
        })

        print(f"Results for target hc = {target_hc:.12e}")
        print(f"  new kg: { kg_adjustment:.12e} m/s")
        print(f"Final c: {final_c:.12e} m/s")
        print(f"Final h: {final_h:.12e} J·s")
        print(f"    1/c: {1/final_c:.12e} m/s")
        print(f"     hc: {final_h * final_c:.12e} J·m")
        print(f"Relative difference from target hc: {abs(final_hc - target_hc) / target_hc:.12e}")

    return results

# List of target hc values to calculate
target_hc_values = [initial_h * initial_c, 2e-25, 1e-25, 1e-24, 1.0]  # Example target hc values

# Run the calculations for each target hc value
results = run_hc_calculations(target_hc_values)
results = run_hc_calculations_kg(target_hc_values)
