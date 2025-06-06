import sympy as sp
import numpy as np
import random


def random_color():
    levels = range(32, 256, 64)
    return np.array([random.choice(levels) for _ in range(3)]) / 255


x = sp.symbols('x')

f_x = x ** 3 + (-6 * (x ** 2)) - x + 6
fp_x = sp.diff(f_x, x)

print(fp_x)

x0 = -10
epsilon = 1e-6

x_tmp = x0
i = 0

fs = sp.plot(f_x, line_color='r', show=False)

while True:
    i = i + 1

    tangent_line = fp_x.subs(x, x_tmp) * (x - x_tmp) + f_x.subs(x, x_tmp)
    print(tangent_line)
    fs.append(sp.plot(tangent_line, line_color=random_color(), show=False)[0])

    raphson_method = float(x_tmp) - float(f_x.subs(x, x_tmp)) / float(fp_x.subs(x, x_tmp))
    error = f_x.subs(x, raphson_method)

    if error <= epsilon:
        break

    x_tmp = raphson_method

print('반복 횟수: ' + str(i))
print('근사해: ' + str(raphson_method))

fs.show()
