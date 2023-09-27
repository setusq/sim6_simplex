from pulp import *

prob = LpProblem("LP Problem", LpMaximize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)

prob += x1 + x2 +x3 - x4

prob += x1 + x2 + 2*x3 + x4 == 12
prob += x1 + 2*x2 + x3 <= 20
prob += x1 + x2 + x3 <= 20

prob.solve()
print("Максимальное значение функции: ", value(prob.objective))
print("Оптимальные значения переменных x:")
for v in prob.variables():
    print(v.name, "=", value(v))
