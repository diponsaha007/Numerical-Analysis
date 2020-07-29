import numpy as np
from matplotlib import pyplot as plt
import math


def function(x):
    try:
        ret = x / (1 - x) * math.sqrt(6 / (2 + x)) - 0.05
    except(ZeroDivisionError, ValueError):
        print('Function Domain error!')
        return None
    return ret


def false_position_method(func, xl, xu, es, itmax):
    it = 0
    fl = func(xl)
    fu = func(xu)
    if fl is None or fu is None:
        return None
    xr = 0
    ea = 100
    while True:
        xrold = xr
        try:
            xr = xu - fu * (xl - xu) / (fl - fu)
        except ZeroDivisionError:
            print('Division by zero. Exiting false position method!')
            return None
        fr = func(xr)
        it += 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100

        test = fl * fr
        if test < 0:
            xu = xr
            fu = fr

        elif test > 0:
            xl = xr
            fl = fr
        else:
            ea = 0
        if ea < es or it >= itmax:
            break
    print('Iteration taken for False Position Method is ', it)
    return xr


def secant_method(func, xl, xu, es, itmax):
    fl = func(xl)
    fu = func(xu)
    if fl is None or fu is None:
        return None
    ea = 100
    xr = 0
    it = 0
    while True:
        xrold = xr
        try:
            xr = xu - fu * (xl - xu) / (fl - fu)
        except ZeroDivisionError:
            print('Division by zero. Exiting Secant method!')
            return None
        it += 1
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        xl = xu
        xu = xr
        fl = fu
        fu = func(xr)
        if ea < es or it >= itmax:
            break

    print('Iteration taken for Secant Method is ', it)
    return xr


if __name__ == "__main__":
    x = np.arange(-1.99, 1, .1)
    y = []
    for i in x:
        y.append(function(i))

    y = np.array(y)
    plt.figure(figsize=(10, 8))
    plt.plot(x, y)
    plt.grid(color='Grey')
    plt.xlabel('X Values')
    plt.ylabel('Function Values')
    plt.show()

    while True:
        xl = float(input("Enter lower bound of the bracket"))
        xu = float(input("Enter upper bound of the bracket"))
        max_iteration = int(input("Enter the maximum number of iteration"))
        ans = false_position_method(function, xl, xu, 0.5, max_iteration)
        if ans is None:
            print('Error in False Position Method! Guess Again! ')
        else:
            print('Root of the equation is ', ans)
            break

    while True:
        xl = float(input("Enter 1st initial guess"))
        xu = float(input("Enter 2nd initial guess"))
        max_iteration = int(input("Enter the maximum number of iteration"))
        ans = secant_method(function, xl, xu, 0.5, max_iteration)
        if ans is None:
            print('Error in Secant Method!')
        else:
            print('Root of the equation is ', ans)
            break
