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
print("Original:   λ_th =", λ_th)
print("Simplified: λ_th =", λ_th_simplified)
print()

σ = 2*pi**5*k**4 / (15*h**3*c**2)
σ_simplified = σ.subs({h: Hz_kg * c**2, k: K_Hz * Hz_kg * c**2 })
σ_simplified = simplify(σ_simplified)

print("Stephan-Boltzmann Formula:")
print("Original:   σ =", σ)
print("Simplified: σ =", σ_simplified)
print()

planck_law = ((2 * h * f**3)/c**2)*(1/(e**((h*f)/(k * T))-1))
planck_law_simplified = planck_law.subs({h: Hz_kg * c**2, k: K_Hz * Hz_kg * c**2 })
planck_law_simplified = simplify(planck_law_simplified)

print("Planck law Formula:")
print("Original:   B(f T) =", planck_law)
print("Simplified: B(f T) =", planck_law_simplified)
print()

λ_max = symbols("λ_max")

x_peak = h*c / (λ_max * k*T)
x_peak_simplified = x_peak.subs({h: Hz_kg * c**2, k: K_Hz * Hz_kg * c**2 })
x_peak_simplified = simplify(x_peak_simplified)

print("Wien's Displacement Constant:")
print("Original:   x_peak =", x_peak)
print("Simplified: x_peak =", x_peak_simplified)
print()

Θ_D, Θ_E, Hz_K, ν_D, ν_E  = symbols("Θ_D Θ_E Hz_K ν_D ν_E")

Θ_D = h * ν_D / k 
Θ_D_simplified = Θ_D.subs({h: Hz_kg * c**2, k: K_Hz * Hz_kg * c**2 })
Θ_D_simplified = simplify(Θ_D_simplified)
Θ_D_simplified = Θ_D_simplified.subs({K_Hz: 1/Hz_K})
Θ_D_simplified = simplify(Θ_D_simplified)

print("Debye Temperature:")
print("Original:   Θ_D =", Θ_D)
print("Simplified: Θ_D =", Θ_D_simplified)
print()

Θ_E = h * ν_E / k
Θ_E_simplified = Θ_E.subs({h: Hz_kg * c**2, k: K_Hz * Hz_kg * c**2 })
Θ_E_simplified = simplify(Θ_E_simplified)
Θ_E_simplified = Θ_E_simplified.subs({K_Hz: 1/Hz_K})
Θ_E_simplified = simplify(Θ_E_simplified)

print("Einstein Temperature:")
print("Original:   Θ_E =", Θ_E)
print("Simplified: Θ_E =", Θ_E_simplified)
print()


