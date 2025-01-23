from decimal import Decimal, getcontext

# Set desired precision
getcontext().prec = 100

c = Decimal(299792458.0)    # m/s
h = Decimal(6.62607015e-34) # m^2 kg / s
G = Decimal(6.67430e-11)    # m^3 kg / s^2
half = Decimal (1/2)

m   = h/c**2              # kg  the mass of a photon
m_P = (h*c/G)**(half)     # kg  the original Planck mass unit using h not hbar
space_time_ratio1  = m/m_P # dimensionless, 
# m_P = m / space_time_ratio #kg this is the new definition for m_P in the framework

s_t   = (h*c*G)**(half)     # m^3/s^2  the s_t is short for space time factor
space_time_ratio = s_t/c**3  # this version has units of second, this cancels an s from denom in next line
# s_t   = space_time_ratio* c**3   # m^3/s^2 - This is the new definition for s_t in the framework
print (f"space time ratio comparison: {space_time_ratio/space_time_ratio1}")
print (f"s_t was this value all along  h*c/m_P={h*c/m_P :<13.8e} s_t = { s_t:<13.8e}")
print (f" Showing mass of 1 Hz photon from G  G * m_P**2/c**3 = { G * m_P**2/c**3:<13.8e} ")

def calculate_and_print_results_new(value_pairs, c_old, m_old):
    for pair in value_pairs:
        m_scaling, l_scaling = map(Decimal, pair)  # Attempt to convert values to decimals

        m   = m_old * m_scaling
        c   = c_old * l_scaling # m/s

        # s_t/c^3 = 1.35138507828e-43  # has units of s
        # s_t = space_time_ratio* c**3

        # m/m_P  = 1.35138507828e-43
        m_P = m / space_time_ratio  #  dimensionless

        # G = s_t/m_P
        # G = (space_time_ratio* c**3) / (m / space_time_ratio)
        # G = (space_time_ratio**2 * c**3) / m 
        # G = ((m/m_P)**2 * c**3) / m 
        # G = (m * (1/m_P)**2 * c**3)  
        # G = m * c**3 / m_P**2 

        
        # hc = s_t * m_P
        # hc = (space_time_ratio* c**3) * (m / space_time_ratio)
        # hc =  c** 3 * m

        p  = m * c
        h  = m * c**2  
        hc = m * c**3  
        G  = m * c**3 / m_P**2 

        print (f"     {1/l_scaling:<10.5e} {m_scaling:<10.5e} {hc:<13.8e} {h:<13.8e} {p:<13.8} {m:<13.8} {G:<13.8}")

'''
        # s_t/c^3 = 1.35138507828e-43  # has units of s
        # G = (space_time_ratio**2 * c**3) / m
        # G = ((s_t/c**3)**2 * c**3) / m
        # G = (s_t**2/c**3) / m
        # G = s_t**2 / (m * c**3)





'''

x = Decimal(1)
scaling_pairs = [
    (x, 100000),
    (x, 10000),
    (x, 1000),
    (x, 100),
    (x, 10),
    (x, 1),
    (x, .1),
    (x, .01),
    (x, .001),
    (x, .0001),
    (x, .00001),
    (x, 100/c),
    (x, 10/c),
    (x, 2/c),
#    (1/m_P, 1/c),
    (x, 1/c),
#    (1/(h/c**2), 1/c),
]

print()
print()
print("\n     ----  Exploring h, hc and G  ------- ")
print()
print("      s_length   s_mass     hc             h              p             m             G")
calculate_and_print_results_new(scaling_pairs, c, m)
print()
print()



