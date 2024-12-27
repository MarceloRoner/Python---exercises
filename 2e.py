import sympy as sp

# Definir variáveis
x1, x2, x3, x4, x5 = sp.symbols('x1 x2 x3 x4 x5', real=True)
lambda1, lambda2 = sp.symbols('lambda1 lambda2', real=True)

# Função objetivo
f = x1**2 + x2**2 + x3**2 + x4**2 + x5**2

# Restrições
g1 = x1 + 2*x2 + x3 - 1
g2 = x3 - 2*x4 + x5 - 6

# Lagrangiana
L = f + lambda1*g1 + lambda2*g2

# Sistema de equações: derivadas parciais da Lagrangiana = 0
eqs = [
sp.Eq(sp.diff(L, x1), 0),
sp.Eq(sp.diff(L, x2), 0),
sp.Eq(sp.diff(L, x3), 0),
sp.Eq(sp.diff(L, x4), 0),
sp.Eq(sp.diff(L, x5), 0),
sp.Eq(g1, 0),
sp.Eq(g2, 0)
]

# Resolver o sistema
sol = sp.solve(eqs, [x1, x2, x3, x4, x5, lambda1, lambda2], dict=True)

print("Soluções encontradas:")
for s in sol:
    print(s)

# Interpretando o resultado:
# Cada solução s é um dicionário com os valores de x1, x2, x3, x4, x5, lambda1, lambda2.
# Você pode verificar se é máximo ou mínimo calculando a Hessiana ou analisando o contexto.
