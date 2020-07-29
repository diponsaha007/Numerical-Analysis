import numpy as np
from matplotlib import pyplot as plt


def take_input():
    fp = open("data.txt", "r")
    x_list = []
    y_list = []
    while True:
        line = fp.readline()
        if line == '':
            break
        temp = []
        for x in line.split(' '):
            num = float(x)
            temp.append(num)
        x_list.append(temp[0])
        y_list.append(temp[1])

    fp.close()

    return x_list, y_list


def summation(x, xp, y, yp, n):
    sum = 0
    for i in range(n):
        sum += (x[i] ** xp) * (y[i] ** yp)

    return sum


def calculate_coefficient(matrix, x_list, y_list):
    sr = 0
    st = 0
    average = sum(y_list) / len(y_list)
    for i in range(len(x_list)):
        sr += (y_list[i] - func_value(matrix, x_list[i])) ** 2
        st += (y_list[i] - average) ** 2

    return np.sqrt((st - sr) / st)


def regression(x_list, y_list, order):
    n = len(x_list)
    A_matrix = np.zeros([order + 1, order + 1])
    B_matrix = np.zeros([order + 1])
    row = order + 1
    col = order + 1
    for i in range(col):
        A_matrix[0][i] = summation(x_list, i, y_list, 0, n)

    for i in range(row):
        for j in range(col):
            if j < col - 1 and i >= 1:
                A_matrix[i][j] = A_matrix[i - 1][j + 1]
            else:
                A_matrix[i][j] = summation(x_list, i + j, y_list, 0, n)

    for i in range(row):
        B_matrix[i] = summation(x_list, i, y_list, 1, n)

    X_matrix = np.linalg.solve(A_matrix, B_matrix)

    # calculating regression coefficient
    r = calculate_coefficient(X_matrix, x_list, y_list)
    return X_matrix, r


def func_value(matrix, x_value):
    temp = 0
    for j in range(len(matrix)):
        temp += matrix[j] * (x_value ** j)

    return temp


def plot_equation(plot_mat, mini, mx, color, linewidth, label):
    x_list = np.linspace(mini, mx, 30000)
    y_list = []

    for i in x_list:
        y_list.append(func_value(plot_mat, i))

    plt.plot(x_list, y_list, color=color, linewidth=linewidth, label=label)


def print_equation(plot_mat):
    print("For order ", len(plot_mat) - 1, " :")
    for i in range(len(plot_mat)):
        print("a", i, " = ", plot_mat[i])

    print()
    print("So the corresponding equation is\ny = ", end="")
    for i in range(len(plot_mat)):
        print(np.around(plot_mat[i], decimals=2), "* x^(", i, ")", end="")
        if i != len(plot_mat) - 1:
            print(" + ", end="")

    print()


if __name__ == "__main__":
    # taking the x co-ordinate and y co-ordinates
    x_list, y_list = take_input()

    # plotting the points
    plt.figure(figsize=(12, 10))
    plt.scatter(x_list, y_list, s=4)

    # Plotting a first-order curve
    plot_matrix, r = regression(x_list, y_list, 1)
    plot_equation(plot_matrix, min(x_list), max(x_list), 'red', 4, 'First-order curve')
    print_equation(plot_matrix)
    print("Regression Coefficient for 1st order curve = ", r, "\n")

    # Plotting a second-order curve
    plot_matrix, r = regression(x_list, y_list, 2)
    plot_equation(plot_matrix, min(x_list), max(x_list), 'green', 4, 'Second-order curve')
    print_equation(plot_matrix)
    print("Regression Coefficient for 2nd order curve = ", r, "\n")

    # Plotting a third-order curve
    plot_matrix, r = regression(x_list, y_list, 3)
    plot_equation(plot_matrix, min(x_list), max(x_list), 'yellow', 4, 'Third-order curve')
    print_equation(plot_matrix)
    print("Regression Coefficient for 3rd order curve = ", r, "\n")

    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.title("Different order curve plotting")
    plt.legend()
    plt.show()
