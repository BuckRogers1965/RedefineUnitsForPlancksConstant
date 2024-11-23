# RedefineUnitsForPlancksConstant
This project reinterprets Planck’s constant h as a product of unit choices rather than intrinsic mysteries. By redefining h and the speed of light c as unit-derived quantities. Complexities in quantum mechanics and relativity could stem from unit systems.


I deconstructed Planck's and the gravitational constants (h and G) to separate the contribution from the mass and length units.  This work is in the simplified_plancks_constants.py file.  This has the simplified formulas with just the needed scaling, the uneeded scaling cancelled out. The alpha and beta scaling units are 100% only unit scaling. They are an artifact entirely created by how we define our units.  

Here are the four formulas together:
h = α³β/c
G = α³/β
k = α³β/γ
ε₀ = δ²/(α³β)

And the values for each parameter:
α ≈ 1.53844×10⁻⁶ m (length scaling)
β ≈ 5.45551×10⁻⁸ kg (mass scaling)
γ ≈ 1.438776877504×10⁻² K⁻¹ (temperature scaling)
δ ≈ 1.32621132205611221308×10⁻¹⁸ C (charge scaling)

This reduces Planck’s charge = δ √2 

Simple Explanation: Imagine you have two super tiny numbers, one representing a piece of length and the other a piece of weight. They aren't really the length or weight, but more about how the units for weight and length interact with each other.

When you combine these tiny pieces in a certain way, you can understand important things about the universe, like how small particles behave and how gravity works. 

1. Planck's Constant (h): Think of it as a way to measure the smallest bits of energy. You get this by combining the tiny length piece (alpha) and the tiny weight piece (beta), and then dividing by the speed of light. This is a way to convert units from one kind of thing to another relationship.

2. Gravitational Constant (G): This helps us understand how gravity works. You find it by taking the tiny length piece (alpha) and dividing it by the tiny weight piece (beta).  This is almost the same as h, but it converts a different set of units to another similar relationship. 

These formulas act as a scaling factor for the different units.  Think of them as a translator.



[Reinterpreting Planck's Constant: From Fundamental Constant to Geometric Unit Conversion Factor](https://mystry-geek.blogspot.com/2024/11/reinterpreting-plancks-constant-from.html)

The quantization_demo.py program shows step by step how h works. The following is the paper where the idea was explained. 
[Reinterpreting Planck's Constant: A Geometric Perspective on Quantum Mechanics](https://mystry-geek.blogspot.com/2024/11/reinterpreting-plancks-constant.html)

The above paper is my latest understnding of what this probram shows. 

# Reframing Fundamental Constants: A New Perspective on Energy, Wavelength, and Relativity

**Author**: James Rogers  
**Location**: SE Ohio  
**Date**: 2024-11-06  

## Abstract

This project introduces a novel framework for understanding fundamental constants, particularly Planck’s constant h, as products of unit choices rather than intrinsic mysteries of nature. By redefining constants as unit-derived quantities, this perspective uncovers simpler geometric relationships between energy, wavelength, and relativistic effects. This approach suggests that complexities in quantum mechanics might stem from unit conventions rather than fundamental aspects of physical reality.  

## Key Concepts

1. **Encoding Constants via Division/Multiplication**  
   Constants like h can be seen as encoding simpler physical relationships through unit scaling, analogous to reversible division/multiplication operations.  we can extract the ratio between h and 1/c out by just setting K=hc. 

2. **Planck's Constant as a Unit Scaling Factor**  
   h is reframed as K/c, where K (e.g.,  1.98644568 * 10^-25 J m} acts as a scaling factor in energy-wavelength relationships. This redefinition proposes that h and K arise from unit-based choices rather than being fundamental values.

3. **Redefining Units to Expose Fundamental Relationships**  
   Through a thought experiment setting hc = 1 J m, we redefine the speed of light c and the meter m, revealing insights into how constants interact with unit systems. By finding the meter scaling factor where  h = 1/c, the framework suggests that both constants are emergent from unit scaling.

4. **Revised Equations Using K  as a Scaling Factor**
   - **Geometric-Replacement_for_h**: h = K/c 
   - **Energy-Frequency**: E = K f / c 
   - **Energy-Wavelength**: E = K / wavelength
   - **Reduced Planck Constant**: hbar = K / (2 pi c)
   - **Fine Structure Constant**: alpha = e^2 / (2 epsilon_0 K)

   This reformulation allows K to simplify geometric relationships between energy, frequency, and wavelength.

5. **Relating Wavelength to Time Dilation**  
   In this framework, a particle’s wavelength can encode its time dilation, linking quantum properties with relativistic effects. Thus, energy, typically seen as a scalar, may also reflect geometric factors related to time dilation, providing a bridge between quantum and relativistic models.

## Implementation

To implement these ideas computationally, this project includes:

- A search program that fine-tunes meter redefinitions to achieve a target hc value.
- An algorithm that iteratively adjusts the meter scaling factor to converge on exact values, demonstrating unit dependency of constants like h and c.

This program can be used to explore similar adjustments for other constants, offering a platform for deeper insights into unit-driven frameworks of physical relationships.
