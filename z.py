import numpy as np

def analyze_hc_G_scaling():
    """
    Analyze how hc and G relate when we scale kg to make their ratio 1
    """
    # Original constants
    h = 6.62607015e-34
    c = 299792458
    G = 6.67430e-11

    # Calculate original hc
    hc_original = h * c
    print("\nOriginal values:")
    print(f"hc = {hc_original:.8e} kg⋅m³/s²")
    print(f"G  = {G:.8e} m³/(kg⋅s²)")
    print(f"Ratio hc/G = {hc_original/G:.8e}")

    # Calculate the kg scaling factor from sqrt(hc/G)
    kg_scale = np.sqrt(hc_original/G)
    print(f"\nkg scaling factor = {kg_scale:.8e}")

    # Calculate new values with scaled kg
    hc_new = hc_original / kg_scale  # Dividing by kg_scale because hc has kg in numerator
    G_new = G * kg_scale            # Multiplying by kg_scale because G has kg in denominator

    print("\nAfter kg scaling:")
    print(f"h_new = {h/kg_scale:.8e} (scaled_kg)⋅m^2/s")
    print(f"hc_new = {hc_new:.8e} (scaled_kg)⋅m³/s²")
    print(f"G_new  = {G_new:.8e} m³/(scaled_kg⋅s²)")
    print(f"Ratio hc_new/G_new = {hc_new/G_new:.15f}")
    print(f"Absolute difference = {abs(hc_new - G_new):.8e}")
    print(f"Relative difference = {abs(hc_new - G_new)/hc_new:.8e}")


    # Define alpha (scaling for meter) based on kg_scale and original constants
    print()
    alpha = (hc_new ) #** (1/3)
    print(f"Meter scaling factor (alpha) = {alpha:.20e}")
    print(f"1/ Meter scaling factor (alpha) = {1/alpha:.20e}")
    print(f"Meter/c scaling factor (alpha) = {alpha/c:.20e}")
    print(f"c/Meter scaling factor (alpha) = {c/alpha:.20e}")

    beta  =  kg_scale
    print(f"\nkg scaling factor (beta)     = {beta:.20e}")
    print(f"1/kg scaling factor (beta)     = {1/beta:.20e}")
    print(f"kg/c scaling factor (beta)     = {beta/c:.20e}")
    print(f"c/kg scaling factor (beta)     = {c/beta:.20e}")


    print(f"\nalpha*beta     = {alpha*beta:.20e}")
    print(f"alpha/beta     = {alpha/beta:.20e}")
    print(f"beta/alpha     = {beta/alpha:.20e}")

        # Verify the calculated constants based on alpha and beta
    h_calc = (alpha  * beta) / c
    G_calc =  alpha / beta

    print("\nDerived constants based on alpha and beta:")
    print(f"           h = {h:.8e} (scaled_kg)⋅m^2/s")
    print(f"Calculated h = {h_calc:.8e} kg⋅m²/s")
    print()
    print(f"           G = {G:.8e} m³/(kg⋅s²)")
    print(f"Calculated G = {G_calc:.8e} m³/(kg⋅s²)")
    print()
    print(f"Difference in h = {abs(h_calc - h):.8e}")
    print(f"Difference in G = {abs(G_calc - G):.8e}")


    # Calculate what this means for mass scaling
    print("\nImplications for mass:")
    print(f"1 kg in original units = {kg_scale:.8e} kg in new units")
    print(f"1 kg in new units = {1/kg_scale:.8e} kg in original units")

    return hc_new, G_new, kg_scale

if __name__ == "__main__":
    hc_new, G_new, kg_scale = analyze_hc_G_scaling()
