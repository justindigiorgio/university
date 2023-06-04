import prob
import matplotlib.pyplot as plt

class ContinuousDist:
    def __init__(self, func, domain, parameters):
        pass


class DiscreteDist:
    def __init__(self, func, domain, parameters):
        self._pmf = func
        self._x = domain
        self._par = parameters
        self._cdf = self.pmf_to_cdf(func, domain, parameters)  # list
        self._expected = 0
        self._var = 0

    @staticmethod
    def pmf_to_cdf(pmf, dom, par):
        x = [pmf(i, par) for i in dom]
        for i in range(1, len(dom)):
            x[i] += x[i - 1]
        return x

    def random(self):
        q = prob.unif()
        x = [i for i in range(0, len(self._x)) if self._cdf[i] >= q]
        return x[0]

    def plot(self):
        y = [self._pmf(x, self._par) for x in self._x]
        plt.plot(self._x, y)
        plt.show()
        pass

    def plot_cdf(self):
        plt.plot(self._x, self._cdf)
        plt.show()
        pass




class DUnif(DiscreteDist):
    pass


class Binom(DiscreteDist):
    def __init__(self, n, p):
        DiscreteDist.__init__(self, Binom.dbinom, list(range(0,n+1)), [n,p])

    @staticmethod
    def dbinom(x, par: "[n,p]"):
        """
        returns prob(X = x) for X ~ binomial(n,p)
        """
        assert (0 <= x <= par[0])
        assert (0 <= par[1] <= 1)
        n = par[0]
        p = par[1]
        return prob.choose(n, x) * (p ** x) * ((1 - p) ** (n - x))
    pass


class Geom(DiscreteDist):
    pass


class Pois(DiscreteDist):
    pass


class HGeom(DiscreteDist):
    pass


class NBinom(DiscreteDist):
    pass


def main():
    B = Binom(100, 1/2)
    # print(B._cdf)
    # print(B._x)
    # print([B.dbinom(i, [5, 1/2]) for i in range(0,6)])
    samp = [B.random() for i in range(0,100000)]
    plt.hist(samp, bins=100)
    plt.show()


if __name__ == "__main__":
    main()