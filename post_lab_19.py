# #question 1
import sympy as sp 
n, z = sp.symbols('n z', positive=True) 
u = 1  # unit step for n >= 0 
X = sp.summation(u * z**(-n), (n, 0, sp.oo)) 
print("Z-transform of u[n]:") 
sp.pprint(X, use_unicode=True) 


#question 2
import sympy as sp
z = sp.symbols('z')

H = 0.5 * (z - 0.7) * (z - 0.9) / ((z - 0.6) * (z - 0.4))
num = sp.simplify(sp.factor(sp.numer(H)))
den = sp.simplify(sp.factor(sp.denom(H)))
zeros = sp.solve(sp.Eq(num, 0), z)
poles = sp.solve(sp.Eq(den, 0), z)
print("Zeros:", zeros)
print("Poles:", poles)

# Check stability
stable = all(abs(p) < 1 for p in poles)
print("\nSystem Stability:", "Stable" if stable else "Unstable")