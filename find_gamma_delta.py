# Define the known constants
alpha: float = 1.53843945498419101549e-06  # length unit scaling
beta: float  = 5.45551186133462110058e-08  # mass unit scaling
k_B = 1.380649e-23  # Boltzmann constant in J/K
e0 = 8.854187817e-12

# Calculate alpha^3
alpha_cubed = alpha ** 3

# Calculate the numerator
numerator = alpha_cubed * beta

# Calculate gamma
gamma = numerator / k_B
print(f"    gamma: {gamma:.20e}  K^-1")


# e0 = constants.delta**2 / (constants.alpha**3 * constants.beta)
# e0/e0 = constants.delta**2 / (constants.alpha**3 * constants.beta * e0)
# 1/ constants.delta**2 = constants.delta**2 / (constants.alpha**3 * constants.beta * e0 * constants.delta**2)
# 1/ delta**2 = 1 / (alpha**3 * beta * e0 )
delta = ((alpha**3 * beta) * e0)**(1/2)

# Print the result
print(f"    delta: {delta:.20e} K^-1")


