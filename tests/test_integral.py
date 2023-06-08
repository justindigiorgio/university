import matplotlib.pyplot as plt
from comp_math.integral import Integral, oscil

def plot_test_1():
    # per wolfram alpha
    ans = "-0.1327641442003012340629343548846822855690178761421423618114406160"
    ans = float(ans)
    mid_err = []
    trap_err = []
    simp_err = []
    precision = list(range(0, 7))
    for i in precision:
        j = Integral([0, 10], oscil, intervals=10 ** i)
        mid_err.append(abs(ans - j.midpoint()))
        trap_err.append(abs(ans - j.trapezoid()))
        simp_err.append(abs(ans - j.simpson()))
    plt.scatter(precision, mid_err, marker='x', c='r')
    plt.scatter(precision, trap_err, marker='x', c='b')
    plt.scatter(precision, simp_err, marker='x', c='g')
    plt.yscale('log')
    plt.ylim([10 ** -18, 10 ** 1])
    plt.show()

if __name__ == '__main__':
    plot_test_1()