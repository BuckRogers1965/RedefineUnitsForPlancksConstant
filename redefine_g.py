import numpy as np

# Initial constants
initial_G = 6.67430e-11   # Gravitational constant in m³/(kg·s²)
initial_c = 299792458     # Speed of light in m/s
current_Gc = initial_G * initial_c  # Gc product

def adjust_m_and_calculate(initial_G, initial_c, target_Gc):
    meter_adjustment = np.power(current_Gc / target_Gc, 1/4)  # Adjust meter factor
    #meter_adjustment = np.cbrt(current_Gc / target_Gc)  # Adjust meter factor
    new_c = initial_c / meter_adjustment                # New speed of light (c)
    new_G = initial_G / meter_adjustment**3             # New gravitational constant (G)
    return meter_adjustment, new_G, new_c

def adjust_kg_and_calculate(initial_G, initial_c, target_Gc):
    kg_adjustment = current_Gc / target_Gc             # Adjust kilogram factor 
    new_G = initial_G / kg_adjustment                  # New gravitational constant (G)
    return kg_adjustment, new_G, initial_c

def adjust_s_and_calculate(initial_G, initial_c, target_Gc):
    second_adjustment = np.cbrt(current_Gc / target_Gc)  # Adjust second factor
    new_c = initial_c / second_adjustment             # New speed of light (c)
    new_G = initial_G / second_adjustment**2             # New gravitational constant (G)
    return second_adjustment, new_G, new_c

def run_Gc_calculations(target_Gc_values):
    results = []
    units = ['m','kg','s']
    unit_functions = {
        'm': adjust_m_and_calculate,
        'kg': adjust_kg_and_calculate,
        's': adjust_s_and_calculate
    }

    for unit in units:
        print(f"\n\nRedefining units of {unit} to match specific values of Gc\n")
        for target_Gc in target_Gc_values:
            print(f"\nCalculating for target Gc = {target_Gc:.12e}")
            
            if (current_Gc == target_Gc):
                unit_adjustment = 1
                final_G = initial_G
                final_c = initial_c
            else:
                if unit in unit_functions:
                    unit_adjustment, final_G, final_c = unit_functions[unit](initial_G, initial_c, target_Gc)
            final_Gc = final_G * final_c

            results.append({
                "target_Gc": target_Gc,
                "final_c": final_c,
                "final_G": final_G,
                "final_Gc": final_Gc,
                "relative_difference": abs(final_Gc - target_Gc) / target_Gc
            })

            print(f"Results for target Gc = {target_Gc:.12e}")
            print(f"  new {unit}: {unit_adjustment:.12e} old {unit}")
            print(f"Final c: {final_c:.12e} m/s")
            print(f"Final G: {final_G:.12e} m³/(kg·s²)")
            print(f"    1/c: {1/final_c:.12e} s/m")
            print(f"     Gc: {final_G * final_c:.12e} m⁴/(kg·s³)")
            print(f"Relative difference from target Gc: {abs(final_Gc - target_Gc) / target_Gc:.12e}")

# List of target Gc values to calculate
target_Gc_values = [1.0]  # Example target Gc values
#target_Gc_values = [initial_G * initial_c,1.0]  # Example target Gc values

# Run the calculations for each target Gc value
run_Gc_calculations(target_Gc_values)
