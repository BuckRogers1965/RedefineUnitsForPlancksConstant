import pandas as pd
import warnings

# Suppress FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Define constants
h = 6.62607015e-34  # Planck's constant (kg m^2 / s)
c = 2.99792458e8    # Speed of light (m / s)
m = h/c**2          # mass of a photon at 1 Hz. kg
G = 6.67430e-11     # Gravitational constant (m^3 / kg s^2)
m_P = ((h * c) / G) ** 0.5  # Planck mass (kg)
G_wavelength = 9.9277379650300003e-24 # kg^2/m

print (f"m_P {m_P} m_P^2 {m_P**2} m {m} m/m_P^2 {m/m_P**2} ")
print (f"m_P {1/m_P} m_P^2 {1/m_P**2} 1/m {1/m} m_P^2/m {m_P**2/m} ")
print (f"m_P {m_P*c} m_P^2 {m_P**2*c**2} m/m_P {m/m_P} m_P/m {m_P/m} ")
print (f"1/m_P*c {1/(m_P*c)} 1/m_P^2**2 {1/(m_P**2*c**2)} ")
print (f"m_P**2/c {m_P**2/c} m_P**2/c**2 {m_P**2/c**2} m_P**2/c**3 {m_P**2/c**3} ")
print (f"c/m_P**2 {c/m_P**2} c**2/m_P**2 {c**2/m_P**2} c**3/m_P**2 {c**3/m_P**2} ")

print()
print()

# Define the function to calculate gravitational force the traditional way
def traditional_gravity_force(m1, m2, r):
    return G * m1 * m2 / r**2

# Define the function to calculate gravitational force the new way
def gravity_force_new(m1, m2, r):
    # F =c**3 * m * m1 * m2 /(m_P**2 * r**2)
    mass_term = m * m1 * m2 / m_P**2    # Mass Term (kg)
    length_time_term = c**3 / r**2      # Length Term (m/s^2) * 1 s because 1Hz photon mass
                                        # force is mass * accleration
    return mass_term * length_time_term # 1 Newton = 1 kg ⋅ m/s^2

# 
def gravity_wave(m1, m2, r):
    #wave = (m * c**2)/((m1 * m2 * m / m_P**2) * ( c**3 / r**2))
    #wave = 1/((m1 * m2 / m_P**2) * ( c / r**2))
    return ( m_P**2 * r**2)/(m1 * m2 * c) 

# Define the masses (kg) and distances (m) for examples
examples = [
    {"m1": 1, "m2": 1, "r": 1},
    {"m1": 1, "m2": 1, "r": 2},
    {"m1": 2, "m2": 1, "r": 1},
    {"m1": 2, "m2": 1, "r": 2},
    {"m1": 2, "m2": 2, "r": 2},
    {"m1": 1e1, "m2": 1e3, "r": 1e2},
    {"m1": 5e3, "m2": 3e3, "r": 2e2},
    {"m1": 1e4, "m2": 1e4, "r": 5e2},
    {"m1": 1e2, "m2": 1e2, "r": 1e1},
    {"m1": 6e3, "m2": 7e3, "r": 3e2},
    {"m1": m_P, "m2": m_P, "r": c},
    {"m1": m_P, "m2": m_P, "r": c**(1/2)},
]

# Create a DataFrame to store results
df = pd.DataFrame(columns=["m1m2", "Mass", "r^2", "Len", "F(N)"])
df = pd.DataFrame(columns=[])

# Calculate forces and populate the DataFrame
for i, example in enumerate(examples):

    m1, m2, r = example["m1"], example["m2"], example["r"]

    traditional_force = traditional_gravity_force(m1, m2, r)
    mass_term = m1 * m2 * m / m_P**2  # Mass Term (kg)
    length_term = c**3 / r**2         # Length Term (m/s^2) * 1 s because 1Hz photon
    new_force = mass_term * length_term
    new_force = m * c**3 * m1*m2/(m_P**2 * r**2)
    wave4= G_wavelength * (r**2 / ( m1 * m2 ))  # 1s is just 1
    wave5= ( m_P**2 * r**2)/(m1 * m2 * c) 
    new_force = gravity_force_new(m1, m2, r)

    df = pd.concat([df, pd.DataFrame.from_records([{
        "m1m2": m1*m2,
#        "Mass": mass_term,
        "r^2": r**2,
#        "Len": length_term,
#        "F new": new_force,
#        "wave": new_force,
#        "wave 3": h* c /(new_force * r**2),
#        "wave 4": wave4,
#        "wave 5": h/wave5,
#        "wave 22": h/new_force,
#        "*/m_P^2 ": ( m1*m2/(m_P**2*r**2)),
#        "1/(m1m2/m_P^2)": 1/(m1*m2/m_P**2),
        "m1*m2/(r^2)":  m1*m2/(r**2),
        "wn * 1/m_P^2)":  m1*m2/(r**2 * m_P**2),
#        "1/": 1/( m1*m2/(r**2 * m_P**2)),
#        "1/(m12/(r^2*m_P^2))": 1/( m1*m2/(r**2 * m_P**2)),
        "freq -- *c":  m1*m2*c/(r**2 * m_P**2),
#        "wave --1/*c":  1/(m1*m2*c/(r**2 * m_P**2)),
#        "*Q_m":  m*m1*m2*c**1/(r**2 * m_P**2),
        "*Q_m*c^2":  m*m1*m2*c**3/(r**2 * m_P**2),
        "F(N)": traditional_force,
#        "hc * m1m2/m_P^2": m*c**3 * (m1*m2/m_P**2)

    }])], ignore_index=True)

# Display the results
print(df)
print()
print()

