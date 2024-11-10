import numpy as np

# Initial constants
initial_h = 6.62607015e-34  # Planck's constant in J·s
initial_c = 299792458       # Speed of light in m/s

# Function to adjust Planck's constant and speed of light based on the meter factor
def adjust_values(initial_h, initial_c, meter_factor):
    new_c = initial_c / meter_factor
    new_h = initial_h / (meter_factor**2)
    return new_h, new_c

# Function to perform the search for a specific target hc value
def find_matching_hc(initial_h, initial_c, target_hc, tolerance=1e-15, max_iterations=1000):
    meter_factor = 1.0
    step_size = 0.5
    direction = 1
    prev_difference = float('inf')

    # immediately return for base case
    if (target_hc == initial_h*initial_c):
        return meter_factor, initial_c, initial_h,  target_hc  

    for iteration in range(max_iterations):
        h, c = adjust_values(initial_h, initial_c, meter_factor)
        hc = h * c
        difference = hc - target_hc
        
        if np.isclose(hc, target_hc, rtol=tolerance, atol=0):
            print(f" * Iteration {iteration}: hc = {hc:.12e}, step_size = {step_size:.6e}, meter_factor = {meter_factor:.24e}")
            return meter_factor, h, c, hc
        
        if np.sign(difference) != np.sign(prev_difference):
            direction *= -1
            step_size /= 2
        
        meter_factor *= (1 + direction * step_size)
        prev_difference = difference
        
        #if iteration % 10 == 0:
            #print(f"Iteration {iteration}: hc = {hc:.12e}, difference = {difference:.6e}, step_size = {step_size:.6e}, meter_factor = {meter_factor:.24e}")

    raise ValueError("Convergence not achieved within maximum iterations")

# Function to run the search for a list of target hc values
def run_hc_searches(target_hc_values):
    results = []
    for target_hc in target_hc_values:
        print(f"\nSearching for target hc = {target_hc:.12e}")
        
        # Reset initial values for each target hc
        meter_factor, final_h, final_c, final_hc = find_matching_hc(initial_h, initial_c, target_hc)
        
        results.append({
            "target_hc": target_hc,
            "meter_factor": meter_factor,
            "new_meter_length": 1 / meter_factor,
            "final_c": final_c,
            "final_h": final_h,
            "final_hc": final_hc,
            "relative_difference": abs(final_hc - target_hc) / target_hc
        })
        
        print(f"Results for target hc = {target_hc:.12e}")
        print(f"Meter factor: {meter_factor:.12e}")
#        print(f"New meter length: {1/meter_factor:.12e} old meters")
        print(f"Final c: {final_c:.12e} m/s")
        print(f"Final h: {final_h:.12e} J·s")
        print(f"1/c:     {1 / final_c:.14e} s/m")
        print(f"hc:      {final_hc:.12e} J·m")
        print(f"Relative difference from target hc: {abs(final_hc - target_hc) / target_hc:.12e}")
        
    return results

# List of target hc values to search for
target_hc_values = [initial_c*initial_h, 2e-25, 1e-25, 1e-24, 1.0]  # Example target hc values

# Run the search for each target hc value
results = run_hc_searches(target_hc_values)
