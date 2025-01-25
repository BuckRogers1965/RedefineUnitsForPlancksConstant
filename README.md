# RedefineUnitsForPlancksConstant
This project reinterprets Planck’s constant h as a product of unit choices rather than intrinsic mysteries. By redefining h and the speed of light c as unit-derived quantities. Complexities in quantum mechanics and relativity could stem from unit systems.

When you finally see that the interaction of the curved space of the photon with space time is the key to understanding the photon.

This framework is modeled in the above constants_framework.py file.

More info here:  https://docs.google.com/presentation/d/e/2PACX-1vQvkEua3rCAui3O87HFVlZTIHmkabKsIDimF2yKUKsSmBKIhvNEMs_ziEQllDWzZMNypY0CXn0a8tDj/pub?start=true&loop=false&delayms=30000&slide=id.p


Summary

This is the framework in a nutshell:

m   = h/c^2                 with no scaling, this extracts the encoded potential mass with units of kg s which is only real at an observed frequency.
c                           is the length scaling, also the velocity.
p  = m * f * c              momentum  is a mass times a velocity, in this case velocity is c 
h  = m * c**2 *1s           Planck's constant is a potential mass encoded with a second to represent the required frequency scaling that is observed. 
E  = m * f * c**2           How planck's constant has always worked.  Energy is a mass times velocity squared, or c^2 for a photon
hc/ = m * c**3 / wavelength  same thing, but decoded with an extra c and wavelength
G = (m * c**3) / m_p^2      G encoded the same photon mass and a Planck mass squared in the denomintator

m is the mass of a photon in the photon.  This value is encoded into both h and G.  

m = h/c^2 gives kg s units which is a mass just waiting to be scaled to the right value. 

that m is literally the value of the mass at 1Hz in a photon, it is kg s units because it is only valued at a frequency. 
7.3724973E-51 kg s = 6.62607015e-34 / c^2

This mass is litterally encoded into h along with with speed of light squared. 
This is not a metaphore, in order for m = h/c^2 to give a value, that value has to be encoded in h with c^2.
And yes, if you know the energy and velocity of anything, you can infer its exact mass and that is 100% valid, for any particle. Feel free to qualify the mass, but curved space time is curved space time and it has real mass and real gravity effects even if that mass is from interactions of a particle with space time in their worldline. 

you can use E=mc^2 to go from the mass and velocity a photon has to the energy as well.
E=1/2 mv^2 where the velocity is c turns into E = mc^2
6.62607015e-34 = 7.3724973E-51 kg * c^2

And you can pull this same potential mass out of G too:

7.3724973E-51 kg s = G *m_p / c^3
where the m_p is the standard plank mass.  m_p=sqrt(hc/G)

this mass m with units of kg s is what scales as the worldline changes in a photon that scaled mass is then used to derive the energy and momentum of something moving in space time. 

m_observed = (m kg s * f 1/s) 
p_observed = (m kg s * f 1/s) * c
E_observed = (m kg s * f 1/s) * c^2
E_observed = (m kg s * f 1/s) * c^3/wavelenth

observing the frequency observes the mass, and that mass is then used to drive the momentum and enrgy. It is literally encoded in h. 

Why have we never seen this before?  

Here is the problem with unit analysis of a final value when you don't know what values went into a number.  Planck mass only picked up part of the mass from the denominator that is inside h and G.  There is the photon mass in the numerator, and two factors of m_p
G  = m * c^3 / m_p^2

When we isolate the m_P value which scales the mass on the top of the formula with

hc which is hc = m * c^3

So m_P = sqrt ( hc/G) we get the following:
m_p = sqrt( m * c^3/m * c^3 / m_p^2)
m_p = sqrt( 1/1 / m_p^2)
m_p = sqrt( m_p^2)

And when we isolated s_t = sqrt(hcG)
s_t = sqrt(m * c^3 *  m * c^3 / m_p^2)
s_t = m * c^3 / m_p
which is just hc/m_p  and if I had recognized that months ago I would have understood things as well as I understand them now.


---


I deconstructed Planck's and the gravitational constants (h and G) to separate the contribution from the mass and length units.  This work is in the simplified_plancks_constants.py file.  This has the simplified formulas with just the needed scaling, the uneeded scaling cancelled out. The alpha and beta scaling units are 100% only unit scaling. They are an artifact entirely created by how we define our units.  

Here are the four formulas together:

* h = (s_lenght x s_mass) / c
* G = s_length/s_mass
* k = (s_lenght x s_mass) /s_temp
* ε₀ = s_charge²/(s_lenght x s_mass) 

And the values for each parameter:

* s_length: 3.64117228161056598231271787236294544974398351386800e-18 m    length unit scaling
* s_mass  : 5.45551186133462083261573179563841219265538485514280e-8 kg   mass unit scaling
* s_temp  : 1.43877687750393380214667160154391159519906942314810e-2 K^-1 temperature unit scaling
* s_charge: 1.32621132205611059057563089920041186351594040760120e-18 C   charge unit scaling

This reduces Planck’s charge = s_charge x √2 

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
