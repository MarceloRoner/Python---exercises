from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, value

prob = LpProblem("Problema", LpMinimize)

x = LpVariable('x',  lowBound=0)
y = LpVariable('y',  lowBound=0)

prob += x + 4*y, "Função_Objetivo"

prob += x + 2*y >= 8, "Restrição_1"
prob += 3*x + 2*y >= 12, "Restrição_2"

prob.solve()

print("Status:", LpStatus[prob.status])

print("x =", value(x))
print("y =", value(y))

print("Valor ótimo da função objetivo:", value(prob.objective))
