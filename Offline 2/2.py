import numpy as np
from matplotlib import pyplot as plt


def take_input():
    # Taking input from file
    fp = open("in2.txt", "r")
    maximizing_func = []
    matrix = []
    solution = []
    line = fp.readline()
    for i in line.split(' '):
        maximizing_func.append(-float(i))

    number_of_variables = len(maximizing_func)

    while True:
        line = fp.readline()
        if line == '':
            break
        temp = []
        cnt = 0
        for x in line.split(' '):
            if cnt < len(maximizing_func):
                temp.append(float(x))
            else:
                solution.append(float(x))
            cnt += 1
        matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix) + 1):
            if (j == i):
                matrix[i].append(1)
            else:
                matrix[i].append(0)

    for j in range(len(matrix)):
        maximizing_func.append(0)

    maximizing_func.append(1)
    matrix.append(maximizing_func)
    solution.append(0)
    matrix = np.array(matrix)
    solution = np.array(solution)
    fp.close()
    return matrix, solution, number_of_variables


def check_last_row(matrix):
    r = len(matrix)
    c = len(matrix[0])
    flag = True
    for i in range(c):
        if matrix[r - 1][i] < 0:
            flag = False
            break

    if flag:
        return True
    else:
        return False


def highest_negative_entry(matrix):
    r = len(matrix)
    c = len(matrix[0])
    min_idx = -1
    for i in range(c):
        if matrix[r - 1][i] < 0:
            if min_idx == -1:
                min_idx = i
            else:
                if matrix[r - 1][min_idx] > matrix[r - 1][i]:
                    min_idx = i

    return min_idx


def minimum_intercept(matrix, solution, idx):
    r = len(matrix)
    c = len(matrix[0])
    min_idx = -1
    for i in range(r):
        if matrix[i][idx] > 0:
            if min_idx == -1:
                min_idx = i
            else:
                if (solution[min_idx] / matrix[min_idx][idx]) > (solution[i] / matrix[i][idx]):
                    min_idx = i

    return min_idx


def divide_the_row(matrix, solution, row_idx, col_idx):
    r = len(matrix)
    c = len(matrix[0])
    divider = matrix[row_idx][col_idx]
    for i in range(c):
        matrix[row_idx][i] /= divider

    solution[row_idx] /= divider


def make_column_zero(matrix, solution, row_idx, col_idx):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        if i == row_idx:
            continue
        substractor = matrix[i][col_idx]
        for j in range(c):
            matrix[i][j] += -substractor * matrix[row_idx][j]
        solution[i] -= substractor * solution[row_idx]


def check_the_columon_for_zeros_and_one(matrix, solution, col_idx):
    cnt_zero = 0
    cnt_one = 0
    idx = -1
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        if matrix[i][col_idx] == 0:
            cnt_zero += 1
        elif matrix[i][col_idx] == 1:
            cnt_one += 1
            idx = i
        else:
            return 0
    if cnt_one == 1:
        return solution[idx]
    else:
        return 0


def get_heading(variable_num, equation_num):
    heading = []
    basic = []
    for i in range(variable_num):
        heading.append("X" + str(i + 1))

    for i in range(equation_num):
        heading.append("S" + str(i + 1))
        basic.append("S" + str(i + 1))

    heading.append("Z")
    basic.append("Z")
    heading.append("Solution")

    return heading, basic


def print_table(matrix, solution, heading, basic, step):
    print("Table ", step, ":")
    print("\t", end="")
    for i in range(len(heading)):
        print(heading[i], end="")
        print("      ", end="")
    print()
    for i in range(len(matrix)):
        print(basic[i] + "\t", end="")
        for j in range(len(matrix[i])):
            print(str(np.around(matrix[i][j], decimals=2)), "\t", end="")
        print(np.around(solution[i], decimals=2))

    print()


def print_Solution(solution, variable_ans, heading):
    print("The maximum value of the objective function is ", np.around(solution, decimals=2))
    for i in range(len(variable_ans)):
        print(heading[i], " : ", np.around(variable_ans[i], decimals=2))


def change_basic(row_idx, col_idx, basic, heading):
    basic[row_idx] = heading[col_idx]


def plot(matrix, solution):
    # plot the curves
    plt.figure(figsize=(10, 6))
    x = np.arange(0, 200, 0.01)
    arra = []
    for i in range(len(matrix) - 1):
        s = str(np.around(matrix[i][1], decimals=1)) + "*y" + " <= " + str(
            np.around(-matrix[i][0], decimals=1)) + "*" + "x + " + str(np.around(solution[i], decimals=1))
        if matrix[i][1] == 0:
            p = [solution[i] / matrix[i][0]] * 20000
            plt.plot(p, x, label=s)
            arra.append(y)
            continue
        y = (-matrix[i][0] * x + solution[i]) / matrix[i][1]
        plt.plot(x, y, label=s)
        arra.append(y)

    plt.ylim(0, 50)
    plt.xlim(0, 30)
    mini = np.minimum(arra[0], arra[1])
    for i in range(2, len(arra)):
        mini = np.minimum(mini, arra[i])
    y = [0] * 20000
    plt.fill_between(x, mini, y, where=mini > y, color="Grey")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    matrix, solution, variable_num = take_input()
    r = len(matrix)
    if variable_num == 2:
        plot(matrix, solution)

    ans = []
    heading, basic = get_heading(variable_num, len(matrix) - 1)
    count = 0
    while True:
        print_table(matrix, solution, heading, basic, count)
        if check_last_row(matrix):
            # Got the answer
            for i in range(variable_num):
                ans.append(check_the_columon_for_zeros_and_one(matrix, solution, i))
            print_Solution(solution[r - 1], ans, heading)
            break

        else:
            col_idx = highest_negative_entry(matrix)
            row_idx = minimum_intercept(matrix, solution, col_idx)
            divide_the_row(matrix, solution, row_idx, col_idx)
            make_column_zero(matrix, solution, row_idx, col_idx)
            change_basic(row_idx, col_idx, basic, heading)
        count += 1
