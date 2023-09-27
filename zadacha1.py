from pulp import *

prob1 = LpProblem("LP Problem", LpMaximize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

prob1 += 15*x1 + 21*x2 - 20

prob1 += -7*x1 + 2*x2 >= 14
prob1 += x1 +11*x2 <= 13
prob1 += x1 +x2 <= 3
prob1 += 4*x1 + 5*x2 >= 20

prob1.solve()
print("Максимальное значение функции: ", value(prob1.objective))
print("Оптимальные значения переменных x:")
for v in prob1.variables():
    print(v.name, "=", value(v))

prob = LpProblem("LP Problem", LpMinimize)

x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

prob += 15 * x1 + 21 * x2 - 20

prob += -7 * x1 + 2 * x2 >= 14
prob += x1 + 11 * x2 <= 13
prob += x1 + x2 <= 3
prob += 4 * x1 + 5 * x2 >= 20

prob.solve()

print("Минимальное значение функции: ", value(prob.objective))
print("Оптимальные значения переменных x:")
for v in prob.variables():
    print(v.name, "=", value(v))

