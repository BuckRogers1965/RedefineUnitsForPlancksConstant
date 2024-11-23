import numpy as np

def analyze_hc_G_scaling():
    """
    Analyze how hc and G relate when we scale kg to make their ratio 1
    """
    # Original constants
    h = 6.62607015e-34
    c = 299792458
    G = 6.6743015e-11

    # Calculate original hc
    hc_original = h * c
    print("\nOriginal values:")
    print(f"hc = {hc_original:.6e} kg⋅m³/s²")
    print(f"G  = {G:.6e} m³/(kg⋅s²)")
    print(f"Ratio hc/G = {hc_original/G:.6e}")

    # Calculate the kg scaling factor from sqrt(hc/G)
    kg_scale = np.sqrt(hc_original/G)
    print(f"\nkg scaling factor = {kg_scale:.6e}")

    # Calculate new values with scaled kg
    hc_new = hc_original / kg_scale  # Dividing by kg_scale because hc has kg in numerator
    G_new = G * kg_scale            # Multiplying by kg_scale because G has kg in denominator

    print("\nAfter kg scaling:")
    print(f"hc_new = {hc_new:.6e} (scaled_kg)⋅m³/s²")
    print(f"G_new  = {G_new:.6e} m³/(scaled_kg⋅s²)")
    print(f"Ratio hc_new/G_new = {hc_new/G_new:.15f}")
    print(f"Absolute difference = {abs(hc_new - G_new):.6e}")
    print(f"Relative difference = {abs(hc_new - G_new)/hc_new:.6e}")

    # Calculate what this means for mass scaling
    print("\nImplications for mass:")
    print(f"1 kg in original units = {kg_scale:.6e} kg in new units")
    print(f"1 kg in new units = {1/kg_scale:.6e} kg in original units")

    return hc_new, G_new, kg_scale

if __name__ == "__main__":
    hc_new, G_new, kg_scale = analyze_hc_G_scaling()
