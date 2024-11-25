

from decimal import Decimal, getcontext, Context, ROUND_DOWN
getcontext().prec = 50

# Define the known constants
alpha = Decimal('1.53843945498418988525651584231678083324584755185780e-6')
beta  = Decimal('5.45551186133462083261573179563841219265538485514280e-8')
k_B   = Decimal('1.380649e-23')  # Boltzmann constant in J/K
e0    = Decimal('8.854187817e-12')

alpha_cubed = alpha * alpha * alpha

numerator = alpha_cubed * beta

gamma = numerator / k_B
print(f"    gamma: {gamma:.50e}  K^-1")


delta = ((numerator) * e0)**(Decimal(1) / Decimal(2))
print(f"    delta: {delta:.50e} K^-1")


