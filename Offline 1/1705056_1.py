import numpy as np
from matplotlib import pyplot as plt


def lnx(x, n):
    ans = 0
    term = x
    for i in range(1, n + 1):
        ans += term
        term = -term * x * i / (i + 1)

    return ans


def relative_approx_error(x, num_of_iteration):
    current_approx = lnx(x, num_of_iteration)
    prev_approx = lnx(x, num_of_iteration - 1)

    return abs(current_approx - prev_approx) / current_approx * 100


if __name__ is '__main__':

    x = float(input('Enter the value of x to calculate ln(1+x) :'))
    n = int(input('Enter the number of iterations :'))
    ans = lnx(x, n)
    print('This answer is ', ans)

    xvalues = np.arange(1, -1, -0.1)
    yvalues = np.log(1 + xvalues)
    plt.figure(figsize=(10, 8))
    plt.plot(xvalues, yvalues, color='Red', linewidth=3, label='Builtin log function')

    plt.plot(xvalues, lnx(xvalues, 1), color='Green', label='1 iteration')
    plt.plot(xvalues, lnx(xvalues, 3), color='Orange', label='3 iteration')
    plt.plot(xvalues, lnx(xvalues, 5), color='Yellow', label='5 iteration')
    plt.plot(xvalues, lnx(xvalues, 20), color='Black', label='20 iteration')
    plt.plot(xvalues, lnx(xvalues, 50), color='Blue', label='50 iteration')
    plt.grid(color='Grey')
    plt.xlabel('X values')
    plt.ylabel('Function Values')
    plt.title('ln(1+x) figure')
    plt.legend()
    plt.show()

    iteration = np.arange(2, 51, 1)
    error = []
    for i in iteration:
        error.append(relative_approx_error(0.5, i))

    error = np.array(error)
    plt.figure(figsize=(10, 8))
    plt.plot(iteration, error, color='Blue')
    plt.xlabel('Number of iteration')
    plt.ylabel('Relative Approx Error (%)')
    plt.title('Relative approx error while calculating ln(1.5)')
    plt.grid(color='Grey')
    plt.show()
