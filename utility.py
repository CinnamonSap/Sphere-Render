import math

def quadratic_neg(poly):
    a = poly[2]
    b = poly[1]
    c = poly[0]
    return (-b-math.sqrt(b ** 2 - 4*a*c))/(2*a)

def quadratic_pos(poly):
    a = poly[2]
    b = poly[1]
    c = poly[0]
    return (-b+math.sqrt(b ** 2 - 4*a*c))/(2*a)

def epsilon_equal(n, m, epsilon=0.00001):
    return (n - epsilon) < m and (n + epsilon > m)

