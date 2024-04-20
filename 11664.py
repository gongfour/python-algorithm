import numpy as np


def dist(x1, x2):
    a = (x1[0] - x2[0]) ** 2
    b = (x1[0] - x2[0]) ** 2
    c = (x1[0] - x2[0]) ** 2
    return (a + b + c) ** 0.5


a = np.array([0, 0, 0])
b = np.array([1, 1, 1])
c = np.array([2, 2, 2])

vec_ab = b - a
d_ab = dist(a, b)
vec_norm_ab = vec_ab / d_ab

norm_c = dist(c, np.zeros((1, 3)))
proj_c = vec_norm_ab * norm_c
print(proj_c)
print(vec_norm_ab)


d_ac = dist(a, c)
d_bc = dist(b, c)
