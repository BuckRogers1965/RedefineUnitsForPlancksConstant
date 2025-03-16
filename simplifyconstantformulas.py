from sympy import symbols, sqrt, pi, simplify,Mul

# Define symbols
m, f_m, f_T, T, c, f, e = symbols("m f_m f_T T c f e", positive=True)
h, k, λ_max = symbols("h k λ_max")  # Planck's constant and Boltzmann's constant

# Define modular unit scaling factors
Hz_kg, kg_J = symbols("Hz_kg kg_J", positive=True)
K_Hz = symbols("K_Hz", positive=True)
two_pi = symbols("2*pi")

#two_pi = Mul(2,pi,evaluate=False)
# Define original thermal de Broglie wavelength formula
λ_th = h / sqrt(two_pi * m *  T * k)

# Substitute h and k with modular scaling factors
λ_th_simplified = λ_th.subs({h: Hz_kg * kg_J, k: K_Hz * Hz_kg * kg_J, m:f_m * Hz_kg, T:f_T/K_Hz, kg_J: c**2 })

# Further simplification
λ_th_simplified = simplify(λ_th_simplified)
λ_th_simplified = simplify(λ_th_simplified)

# Print result
print()
print("Thermal de Broglie Wavelength:")
print("Original:   ", λ_th)
print("Simplified: ", λ_th_simplified)
print()

σ = 2*pi**5*k**4 / (15*h**3*c**2)
σ_simplified = σ.subs({h: Hz_kg * c**2, k: K_Hz * Hz_kg * c**2 })
σ_simplified = simplify(σ_simplified)

print("Stephan-Boltzmann Formula:")
print("Original:   ", σ)
print("Simplified: ", σ_simplified)
print()

planck_law = ((2 * h * f**3)/c**2)*(1/(e**((h*f)/(k * T))-1))
planck_law_simplified = planck_law.subs({h: Hz_kg * c**2, k: K_Hz * Hz_kg * c**2 })
planck_law_simplified = simplify(planck_law_simplified)

print("Planck law Formula:")
print("Original:   ", planck_law)
print("Simplified: ", planck_law_simplified)
print()


x_peak = h*c / (λ_max * k*T)
x_peak_simplified = x_peak.subs({h: Hz_kg * c**2, k: K_Hz * Hz_kg * c**2 })
x_peak_simplified = simplify(x_peak_simplified)

print("Wien's Displacement Constant:")
print("Original:   ", x_peak)
print("Simplified: ", x_peak_simplified)
print()

