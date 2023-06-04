from os import urandom

def choose(n, k):
    """
    returns n choose k, nCk, etc.
    """
    return factorial(n) / (factorial(n-k) * factorial(k))

def unif(a=0, b=1):
    # using python.random module as heavy influence and source
    # we want to convert a byte string into a float from [0,1] so we get 7 bytes (56 bits) and take away 3 using bit
    #   shift because float/double mantissa only stores 53 digits of precision. Then normalise by dividing by 2^53.
    #   maybe manually contruct the float using 1 for sign digit, "-53" in exponent in float and then 53 random bits for
    #   mantissa.
    return (b-a) * ((int.from_bytes(urandom(7), "big") >> 3) * 2 ** -53) + a

def factorial(n):
    assert(n >= 0)
    x = 1
    for i in range(1,n+1):
        x *= i
    return x


