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

prob2 = LpProblem("LP Problem", LpMinimize)

prob2 += 15*x1 + 21*x2 - 20

prob2 += -7*x1 + 2*x2 >= 14
prob2 += x1 +11*x2 <= 13
prob2 += x1 +x2 <= 3
prob2 += 4*x1 + 5*x2 >= 20

prob2.solve()
print("Минимальное значение функции: ", value(prob2.objective))
print("Оптимальные значения переменных x:")
for v in prob2.variables():
    print(v.name, "=", value(v))