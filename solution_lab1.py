# -*- coding: utf-8 -*-
"""
Лабораторная работа №1. Метод простой итерации. Вариант 1.
Задача 1: (0.2x)^3 = cos x, один корень с точностью eps=0.0001.
Задача 2: x^3 - 7x^2 + 3 = 0, все корни с точностью eps=0.01.
"""
import numpy as np
import matplotlib.pyplot as plt

# ================= Задача 1 =================
# f(x) = (0.2x)^3 - cos x = 0.008 x^3 - cos x
f1 = lambda x: 0.008 * x**3 - np.cos(x)
print("Задача 1")
print("f(1) = %.4f, f(2) = %.4f" % (f1(1), f1(2)))

# Приведение к виду x = arccos(0.008 x^3)
phi1 = lambda x: np.arccos(0.008 * x**3)
eps1 = 1e-4
x = 1.5
hist1 = [x]
while True:
    xn = phi1(x)
    hist1.append(xn)
    if abs(xn - x) < eps1:
        x = xn
        break
    x = xn
print("Итерации задачи 1:")
for i, v in enumerate(hist1):
    print("  %d  %.6f" % (i, v))
print("Корень x ≈ %.4f" % x)

# График: y = (0.2x)^3 и y = cos x
xx = np.linspace(0, 2.2, 400)
plt.figure(figsize=(7, 5))
plt.plot(xx, (0.2 * xx)**3, label=r'$y = (0.2x)^3$')
plt.plot(xx, np.cos(xx), label=r'$y = \cos x$')
plt.axhline(0, color='gray', lw=0.6)
plt.xlabel('x'); plt.ylabel('y')
plt.title('Задача 1: (0.2x)^3 = cos x')
plt.legend(); plt.grid(True); plt.tight_layout()
plt.savefig('lab1/fig_l1_t1.png', dpi=150); plt.close()

# ================= Задача 2 =================
f2 = lambda x: x**3 - 7 * x**2 + 3
print("\nЗадача 2")
for a, b in [(-1, 0), (0, 1), (6, 7)]:
    print("  f(%d)=%.0f, f(%d)=%.0f" % (a, f2(a), b, f2(b)))

def iterate(phi, x0, eps=1e-2):
    x = x0; hist = [x]
    while True:
        xn = phi(x); hist.append(xn)
        if abs(xn - x) < eps:
            return hist
        x = xn

# phi1 на [-1;0]:  x = -sqrt(3/(7-x))
r1 = iterate(lambda x: -np.sqrt(3 / (7 - x)), -0.5)
# phi2 на [0;1]:   x = +sqrt(3/(7-x))
r2 = iterate(lambda x: np.sqrt(3 / (7 - x)), 0.5)
# phi3 на [6;7]:   x = 7 - 3/x^2
r3 = iterate(lambda x: 7 - 3 / x**2, 6.5)
for name, h in [("[-1;0]", r1), ("[0;1]", r2), ("[6;7]", r3)]:
    print("  корень на %s:" % name, " ".join("%.4f" % v for v in h), "-> x ≈ %.2f" % h[-1])

# График: f(x) = x^3 - 7x^2 + 3
xx = np.linspace(-2, 8, 500)
plt.figure(figsize=(7, 5))
plt.plot(xx, f2(xx), label=r'$y = x^3 - 7x^2 + 3$')
plt.axhline(0, color='gray', lw=0.8)
plt.xlabel('x'); plt.ylabel('y')
plt.title('Задача 2: x^3 - 7x^2 + 3 = 0')
plt.legend(); plt.grid(True); plt.tight_layout()
plt.savefig('lab1/fig_l1_t2.png', dpi=150); plt.close()
print("Графики сохранены.")
