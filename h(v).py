import sympy as sp

# Variáveis simbólicas
rho, phi, theta = sp.symbols('rho phi theta', real=True, positive=True)

# Integrando em esféricas: f = z*sqrt(x²+y²+z²) = (ρ cosφ)*ρ = ρ² cosφ
# Jacobiano = ρ² sinφ
# Integrando total = ρ² cosφ * ρ² sinφ = ρ^4 sinφ cosφ

integrand = (rho**4)*sp.sin(phi)*sp.cos(phi)

# Limites: rho:0->3, phi:0->pi/2, theta:0->pi/2
res = sp.integrate(sp.integrate(sp.integrate(integrand, (rho,0,3)), (phi,0,sp.pi/2)), (theta,0,sp.pi/2))

print("Resultado simbólico:", res)
print("Resultado numérico:", sp.N(res))
