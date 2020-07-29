import numpy as np
from matplotlib import pyplot as plt
import math


def function(x, y):
    return (x + 20 * y) * (math.sin(x * y))


def euler_method(func, init_x, init_y, final_x, step):
    x_values = np.arange(init_x, final_x + step, step)
    n = len(x_values)
    y_values = np.zeros([n])

    y_values[0] = init_y
    for i in range(1, n):
        value = func(x_values[i - 1], y_values[i - 1])
        y_values[i] = y_values[i - 1] + value * step

    return x_values, y_values


def second_order_rk(func, a2, x, y, step):
    a1 = 1 - a2
    p = 1 / (2 * a2)
    k1 = func(x, y)
    k2 = func(x + p * step, y + p * k1 * step)
    return y + (a1 * k1 + a2 * k2) * step


def fourth_order_rk_helper(func, x, y, step):
    k1 = func(x, y)
    k2 = func(x + 0.5 * step, y + 0.5 * k1 * step)
    k3 = func(x + 0.5 * step, y + 0.5 * k2 * step)
    k4 = func(x + step, y + k3 * step)
    return y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * step


def heuns_method(func, init_x, init_y, final_x, step):
    x_values = np.arange(init_x, final_x + step, step)
    n = len(x_values)
    y_values = np.zeros([n])
    y_values[0] = init_y
    for i in range(1, n):
        y_values[i] = second_order_rk(func, 0.5, x_values[i - 1], y_values[i - 1], step)

    return x_values, y_values


def midpoint_method(func, init_x, init_y, final_x, step):
    x_values = np.arange(init_x, final_x + step, step)
    n = len(x_values)
    y_values = np.zeros([n])
    y_values[0] = init_y
    for i in range(1, n):
        y_values[i] = second_order_rk(func, 1, x_values[i - 1], y_values[i - 1], step)

    return x_values, y_values


def ralstons_method(func, init_x, init_y, final_x, step):
    x_values = np.arange(init_x, final_x + step, step)
    n = len(x_values)
    y_values = np.zeros([n])
    y_values[0] = init_y
    for i in range(1, n):
        y_values[i] = second_order_rk(func, (2 / 3), x_values[i - 1], y_values[i - 1], step)

    return x_values, y_values


def fourth_order_rk(func, init_x, init_y, final_x, step):
    x_values = np.arange(init_x, final_x + step, step)
    n = len(x_values)
    y_values = np.zeros([n])
    y_values[0] = init_y
    for i in range(1, n):
        y_values[i] = fourth_order_rk_helper(func, x_values[i - 1], y_values[i - 1], step)

    return x_values, y_values


def plot1(x1, y1, x2, y2, x3, y3, x4, y4, title):
    plt.figure(figsize=(12, 8))
    plt.plot(x1, y1, label="Step size 0.01")
    plt.plot(x2, y2, label="Step size 0.05")
    plt.plot(x3, y3, label="Step size 0.1")
    plt.plot(x4, y4, label="Step size 0.5")
    plt.grid(color='darkgrey')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title(title)
    plt.legend()
    plt.show()


def plot2(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, title):
    plt.figure(figsize=(12, 8))
    plt.plot(x1, y1, label="Euler method")
    plt.plot(x2, y2, label="Heun’s method")
    plt.plot(x3, y3, label="Midpoint method")
    plt.plot(x4, y4, label="Ralston's method")
    plt.plot(x5, y5, label="4th order RK method")
    plt.grid(color='darkgrey')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title(title)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    x_euler_1, y_euler_1 = euler_method(function, 0, 4, 10, 0.01)
    x_euler_2, y_euler_2 = euler_method(function, 0, 4, 10, 0.05)
    x_euler_3, y_euler_3 = euler_method(function, 0, 4, 10, 0.1)
    x_euler_4, y_euler_4 = euler_method(function, 0, 4, 10, 0.5)
    plot1(x_euler_1, y_euler_1, x_euler_2, y_euler_2, x_euler_3, y_euler_3, x_euler_4, y_euler_4, "Euler method")

    x_heun_1, y_heun_1 = heuns_method(function, 0, 4, 10, 0.01)
    x_heun_2, y_heun_2 = heuns_method(function, 0, 4, 10, 0.05)
    x_heun_3, y_heun_3 = heuns_method(function, 0, 4, 10, 0.1)
    x_heun_4, y_heun_4 = heuns_method(function, 0, 4, 10, 0.5)
    plot1(x_heun_1, y_heun_1, x_heun_2, y_heun_2, x_heun_3, y_heun_3, x_heun_4, y_heun_4, "Heun’s method")

    x_mid_1, y_mid_1 = midpoint_method(function, 0, 4, 10, 0.01)
    x_mid_2, y_mid_2 = midpoint_method(function, 0, 4, 10, 0.05)
    x_mid_3, y_mid_3 = midpoint_method(function, 0, 4, 10, 0.1)
    x_mid_4, y_mid_4 = midpoint_method(function, 0, 4, 10, 0.5)
    plot1(x_mid_1, y_mid_1, x_mid_2, y_mid_2, x_mid_3, y_mid_3, x_mid_4, y_mid_4, "Midpoint method")

    x_ralston_1, y_ralston_1 = ralstons_method(function, 0, 4, 10, 0.01)
    x_ralston_2, y_ralston_2 = ralstons_method(function, 0, 4, 10, 0.05)
    x_ralston_3, y_ralston_3 = ralstons_method(function, 0, 4, 10, 0.1)
    x_ralston_4, y_ralston_4 = ralstons_method(function, 0, 4, 10, 0.5)
    plot1(x_ralston_1, y_ralston_1, x_ralston_2, y_ralston_2, x_ralston_3, y_ralston_3, x_ralston_4, y_ralston_4,
          "Ralston's method")

    x_four_rk_1, y_four_rk_1 = fourth_order_rk(function, 0, 4, 10, 0.01)
    x_four_rk_2, y_four_rk_2 = fourth_order_rk(function, 0, 4, 10, 0.05)
    x_four_rk_3, y_four_rk_3 = fourth_order_rk(function, 0, 4, 10, 0.1)
    x_four_rk_4, y_four_rk_4 = fourth_order_rk(function, 0, 4, 10, 0.5)
    plot1(x_four_rk_1, y_four_rk_1, x_four_rk_2, y_four_rk_2, x_four_rk_3, y_four_rk_3, x_four_rk_4, y_four_rk_4,
          "4th order RK method")

    plot2(x_euler_1, y_euler_1, x_heun_1, y_heun_1, x_mid_1, y_mid_1, x_ralston_1, y_ralston_1, x_four_rk_1,
          y_four_rk_1,"Step size 0.01")
    plot2(x_euler_2, y_euler_2, x_heun_2, y_heun_2, x_mid_2, y_mid_2, x_ralston_2, y_ralston_2, x_four_rk_2,
          y_four_rk_2, "Step size 0.05")
    plot2(x_euler_3, y_euler_3, x_heun_3, y_heun_3, x_mid_3, y_mid_3, x_ralston_3, y_ralston_3, x_four_rk_3,
          y_four_rk_3, "Step size 0.1")
    plot2(x_euler_4, y_euler_4, x_heun_4, y_heun_4, x_mid_4, y_mid_4, x_ralston_4, y_ralston_4, x_four_rk_4,
          y_four_rk_4, "Step size 0.5")
