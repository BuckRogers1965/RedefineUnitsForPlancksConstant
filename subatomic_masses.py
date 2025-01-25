from decimal import Decimal as D, getcontext

# Set precision
getcontext().prec = 50

# Constants
h = D('6.62607015e-34')  # Planck's constant (J·s)
c = D('299792458.0')     # Speed of light (m/s)
e = D('1.602176634e-19') # Elementary charge (C)
m_e = D('9.1093837015e-31')  # Electron mass (kg)
m_p = D('1.67262192369e-27') # Proton mass (kg)
m_n = D('1.67492749804e-27') # Neutron mass (kg)
m_P = D('2.176434e-8')       # Planck mass (kg)
G = D('6.67430e-11')         # Gravitational constant (m³·kg⁻¹·s⁻²)

# Calculate the mass of a photon at 1 Hz
m_photon = h / c**2

# List of masses to compare
masses = {
    "Photon at 1 Hz": m_photon,
    "Electron mass": m_e,
    "Proton mass": m_p,
    "Neutron mass": m_n,
    "Planck mass": m_P,
}

# Accepted energy values in eV (from established physics)
accepted_energy_eV = {
    "Photon at 1 Hz": D('4.135667696e-15'),  # Energy of a 1 Hz photon
    "Electron mass": D('5.109989500e5'),     # 511 keV
    "Proton mass": D('9.382720882e8'),       # 938.272 MeV
    "Neutron mass": D('9.395654205e8'),      # 939.565 MeV
    "Planck mass": D('1.220889936e28'),      # Planck energy
}

# Function to compare masses and calculate ratios, frequencies, and energies
def compare_masses(masses, reference_mass, accepted_energy_eV):
    results = {}
    for name, mass in masses.items():
        ratio = mass / reference_mass  # Ratio to photon mass at 1 Hz
        frequency = ratio              # Frequency (Hz)
        energy_joules = h * frequency  # Energy in joules
        energy_eV = energy_joules / e  # Energy in electronvolts
        accepted_eV = accepted_energy_eV[name]  # Accepted energy in eV
        results[name] = (mass, ratio, frequency, energy_joules, energy_eV, accepted_eV)
    return results

# Compare masses to the photon mass at 1 Hz
results = compare_masses(masses, m_photon, accepted_energy_eV)

# Print results
print()
print()
print(f"Mass of a photon at 1 Hz: {m_photon:.10e} kg")
print(f"Quantum of relative mass: {m_photon:.10e} kg s")
print()
print(f"{'Particle':<15} | {'kg':<14} | {'kg/kgs Hz':<14} | {'J':<14} | {'eV':<14} | {'Accepted eV':<14}")
print("-" * 120)
for name, (mass, ratio, frequency, energy_joules, energy_eV, accepted_eV) in results.items():
    print(f"{name:<15} | {mass:<14.8e} | {ratio:<14.8e} | {energy_joules:<14.8e} | {energy_eV:<14.8e} | {accepted_eV:<14.8e}")
print()
print()
