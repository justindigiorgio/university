"""
Implementing various integral calculation methods
"""

import matplotlib.pyplot as plt
import numpy as np

def oscil(x):
    return np.exp((-1) * (x/10) ** 2) * np.cos(x)


class Integral:

    def __init__(self, domain, function, intervals=20):
        assert(len(domain) == 2)
        assert(domain[0] < domain[1])
        assert(type(function(1) == int))
        assert(intervals >= 1)
        self._f = function
        delta = (domain[1] - domain[0]) / intervals
        self._x = [domain[0] + k * delta for k in range(0, intervals+1)]
        self._y = [function(xi) for xi in self._x]
        self._n = intervals

    def plot(self, show = True, linestyle="solid"):
        plt.plot(self._x, self._y, linestyle=linestyle)
        if show:
            plt.show()

    def midpoint(self):
        est = [[self._x[t], self._x[t+1]] for t in range(0, self._n)]
        est = [Integral.mid(p[0], p[1], self._f((p[0] + p[1])/2)) for p in est]
        return sum(est)

    def trapezoid(self):
        x = self._x
        y = self._y
        est = [[[x[i], x[i+1]],[y[i], y[i+1]]] for i in range(0, self._n)]
        est = [Integral.trap(p[0], p[1]) for p in est]
        return sum(est)

    def simpson(self):
        x = self._x
        y = self._y
        est = [[[x[i], x[i + 1]], [y[i], y[i + 1]]] for i in range(0, self._n)]
        est = [Integral.simp(p[0], p[1], self._f) for p in est]
        return sum(est)
        pass

    def plot_mid(self):
        Integral.plot(self, show=False, linestyle='dashed')
        offset = (self._x[1] - self._x[0]) / 2
        points = [x + offset for x in self._x[:-1]]
        est_y = [self._f(p) for p in points]
        plt.plot()
        for i in range(0,self._n):
            plt.plot([self._x[i], self._x[i+1]], [est_y[i], est_y[i]], c="red")
            plt.plot([self._x[i], self._x[i]], [est_y[i], 0], c='red')
            plt.plot([self._x[i + 1], self._x[i + 1]], [est_y[i], 0], c='red')
        plt.show()


    def plot_trap(self):
        pass

    def plot_simp(self):
        pass

    @staticmethod
    def mid(x0,x1, f_mid):
        assert(x0 < x1)
        return (x1 - x0) * f_mid

    @staticmethod
    def trap(x,y):
        assert (len(x) == len(y) == 2)
        assert(x[0] < x[1])
        return (x[1]-x[0]) * (y[0] + y[1]) / 2

    @staticmethod
    def simp(x,y, func):
        assert(len(x) == len(y) == 2)
        assert(x[0] < x[1])
        return (x[1] - x[0]) * (y[0] + 4 * func((x[0] + x[1])/2) + y[1]) / 6


#
#
# def f_mid(a,b,function):
#     pass
#
#
# def comp_midpoint(xi: "List[float]", f, plot=True):
#     points = [(xi[k] + xi[k+1]) / 2 for k in range(0,len(xi)-1)]
#     values = [f(x) for x in points]
#     calc = sum([values[i] * (xi[i+1] - xi[i])for i in range(0, len(values))])
#     # (calc)
#     if plot:
#         plt.plot(points, values, c='r')
#         plt.axhline(0, c='black')
#         for k in range(0, len(values)):
#             # print("k: ", k, "calls", values[k], xi[k], xi[k+1])
#             plt.vlines(xi[k],ymin=min(values[k],0), ymax=max(values[k],0))
#             plt.vlines(xi[k], ymin=min(values[k-1], 0), ymax=max(values[k-1], 0))
#             plt.hlines(values[k], xmin=xi[k], xmax=xi[k+1])
#         plt.show()
#     return calc
#
# class Integral:
#     def __init__(self, xi=[], f=oscil):
#         assert(len(xi))
#         assert(len(xi) == len(set(xi)))
#         assert(len(xi) >= 2)
#         self._xi = xi
#         self._len = len(xi)
#         self._f = f
#
#
#     def __repr__(self):
#         s = [(self._xi[i],self._yi[i]) for i in range(0, self._len)]
#         return str(s)
#
#
#     # def plot_int(self):
#
#     def riemann_plot(self, left = True):
#         if left:
#             values = self._yi[0:-1]
#         else:
#             values = self._yi[1:]
#         for i in range(0, self._len-1):
#             plt.vlines(self._xi[i], ymin=min(values[i], 0), ymax=max(values[i],0))
#             plt.vlines(self._xi[i+1], ymin=min(values[i], 0), ymax=max(values[i],0))
#             plt.hlines(values[i], xmin=self._xi[i], xmax=self._xi[i+1])
#         plt.axhline(0, c='black')
#         plt.plot(self._xi, self._yi, c='r')
#         plt.show()
#         return
#
#     def midpoint_plot(self):
#         points = [(self._xi[i] + self._xi[i+1]) / 2 for i in range(0, self._len - 1)]
#         values = [self._f(x) for x in points]
#         print(values)
#         for i in range(0, self._len-2):
#             plt.vlines(points[i], ymin=min(values[i], 0), ymax=max(values[i],0))
#             plt.vlines(points[i+1], ymin=min(values[i], 0), ymax=max(values[i],0))
#             plt.hlines(values[i], xmin=points[i], xmax=points[i+1])
#         plt.axhline(0, c='black')
#         plt.plot(self._xi, self._yi, c='r')
#         plt.show()
#         return
#     def trapezoid_plot(self):
#         return
#
#     def simpson_plot(self):
#         return
#
#     def midpoint(self):
#         return
#
#     def trapezoid(self):
#         return
#
#     def simpson(self):
#         return
#
#
# def midpoint(a,b,f):
#     return (b-a) * f((a+b)/2)
#
# def trapezoid(a,b,f):
#     return (b-a)/2 * (f(a) + f(b))
#
# def simpson(a,b,f):
#     return (b-a) / 6 * (f(a) + 4 * f((a+b)/2) + f(b))
#

def main():
    x = Integral([0,10], oscil)
    x.plot_mid()

    pass

if __name__ == "__main__":
    main()

