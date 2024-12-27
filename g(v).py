import sympy as sp

r, theta = sp.symbols('r theta', real=True, positive=True)

integrand = 2*sp.sin(r**2)*r # type: ignore

res = sp.integrate(sp.integrate(integrand, (r, 0, 1)), (theta, 0, sp.pi/2))

print("Resultado simbólico:", res)
print("Resultado numérico aproximado:", sp.N(res))
