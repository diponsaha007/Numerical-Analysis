import numpy as np
from matplotlib import pyplot as plt


def take_input(file_name):
    fp = open(file_name, "r")
    x = []
    y = []
    n = int(fp.readline())
    for i in range(n):
        line = fp.readline()
        temp = []
        for j in line.split(' '):
            temp.append(float(j))
        x.append(temp[0])
        y.append(temp[1])

    fp.close()

    return x, y


def trapezoidal(a, b, fa, fb):
    return (b - a) * ((fa + fb) / 2)


def simpson13(a, b, f0, f1, f2):
    return (b - a) * (f0 + 4 * f1 + f2) / 6


def simpson38(a, b, f0, f1, f2, f3):
    return (b - a) * (f0 + 3 * f1 + 3 * f2 + f3) / 8


def plot_graph(x, y, intervals):
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, s=10, color="Black", label="Points")
    n = len(x)
    for i in range(n - 1):
        plt.plot([x[i], x[i + 1]], [y[i], y[i + 1]], color="Black", linewidth=1)
    plt.plot([x[0], x[0]], [0, y[0]], color="Black", linewidth=1)
    plt.plot([x[n - 1], x[n - 1]], [0, y[n - 1]], color="Black", linewidth=1)
    plt.plot([x[0], x[n - 1]], [0, 0], color="Black", linewidth=1)
    flag_trap = False
    flag_sim13 = False
    flag_sim38 = False
    i = 0
    while i < n - 1:
        start = i
        typ = intervals[i]
        i += 1
        stop = i
        if typ == 0:
            if not flag_trap:
                flag_trap = True
                plt.fill([x[start], x[start], x[stop], x[stop]], [0, y[start], y[stop], 0], color="greenyellow",
                         label="Trapezoid Rule")

            else:
                plt.fill([x[start], x[start], x[stop], x[stop]], [0, y[start], y[stop], 0], color="greenyellow")

        elif typ == 1:
            if not flag_sim13:
                flag_sim13 = True
                plt.fill([x[start], x[start], x[stop], x[stop]], [0, y[start], y[stop], 0], color="dodgerblue",
                         label="Simpson 1/3 Rule")
            else:
                plt.fill([x[start], x[start], x[stop], x[stop]], [0, y[start], y[stop], 0], color="dodgerblue")

        else:
            if not flag_sim38:
                flag_sim38 = True
                plt.fill([x[start], x[start], x[stop], x[stop]], [0, y[start], y[stop], 0], color="seagreen",
                         label="Simpson 3/8 Rule")

            else:
                plt.fill([x[start], x[start], x[stop], x[stop]], [0, y[start], y[stop], 0], color="seagreen")

    plt.grid(color='darkgrey')
    plt.xlabel('X values')
    plt.ylabel('Function Values')
    plt.title('Numerical Integration')
    plt.legend()
    plt.show()


def integrate(x, y):
    count_trap = 0
    count_sim13 = 0
    count_simp38 = 0
    sum = 0
    n = len(x)
    intervals = np.zeros([n - 1])  # it will contain which interval was integrated with which method.
    # value 0 means trap , 1 means simp13, 2 means sim38
    i = 0
    while i < n - 1:
        start_idx = i
        diff = x[i + 1] - x[i]
        segment = 1
        i += 1
        while i < n - 1 and abs(x[i + 1] - x[i] - diff) <= 1e-6:
            segment += 1
            i += 1
        finish_idx = i
        if segment == 1:
            sum += trapezoidal(x[start_idx], x[finish_idx], y[start_idx], y[finish_idx])
            count_trap += segment
            intervals[start_idx] = 0

        elif segment % 3 == 0:
            for j in range(start_idx, finish_idx, 3):
                sum += simpson38(x[j], x[j + 3], y[j], y[j + 1], y[j + 2], y[j + 3])

            for j in range(start_idx, finish_idx):
                intervals[j] = 2
            count_simp38 += segment

        elif segment % 3 == 1:
            for j in range(start_idx, finish_idx - 4, 3):
                sum += simpson38(x[j], x[j + 3], y[j], y[j + 1], y[j + 2], y[j + 3])

            for j in range(start_idx, finish_idx - 4):
                intervals[j] = 2
            count_simp38 += segment - 4

            sum += simpson13(x[finish_idx - 4], x[finish_idx - 2], y[finish_idx - 4], y[finish_idx - 3],
                             y[finish_idx - 2])
            sum += simpson13(x[finish_idx - 2], x[finish_idx], y[finish_idx - 2], y[finish_idx - 1],
                             y[finish_idx])
            count_sim13 += 4
            intervals[finish_idx - 4] = 1
            intervals[finish_idx - 3] = 1
            intervals[finish_idx - 2] = 1
            intervals[finish_idx - 1] = 1

        elif segment % 3 == 2:
            for j in range(start_idx, finish_idx - 2, 3):
                sum += simpson38(x[j], x[j + 3], y[j], y[j + 1], y[j + 2], y[j + 3])

            for j in range(start_idx, finish_idx - 2):
                intervals[j] = 2
            count_simp38 += segment - 2
            sum += simpson13(x[finish_idx - 2], x[finish_idx], y[finish_idx - 2], y[finish_idx - 1],
                             y[finish_idx])
            count_sim13 += 2
            intervals[finish_idx - 2] = 1
            intervals[finish_idx - 1] = 1

    print("Trapezoid: ", count_trap, " intervals")
    print("1/3 rule: ", count_sim13, " intervals")
    print("3/8 rule: ", count_simp38, " intervals")
    print()
    print("Integral value: ", np.around(sum, decimals=5))

    plot_graph(x, y, intervals)


if __name__ == "__main__":
    x, y = take_input("input.txt")
    integrate(x, y)
