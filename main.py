import math


# BEGIN (write your solution here)
def make_rational(numer, denom):
    deli = math.gcd(numer, denom)
    return {"numer": int(numer / deli), "denom": int(denom / deli)}


def get_numer(rational):
    return rational["numer"]


def get_denom(rational):
    return rational["denom"]


def add(rational1, rational2):
    numer1 = get_numer(rational1)
    denom1 = get_denom(rational1)
    numer2 = get_numer(rational2)
    denom2 = get_denom(rational2)
    deli_d = math.gcd(int(get_denom(rational1)), int(get_denom(rational2)))

    return make_rational(int((numer1 * denom2 + numer2 * denom1) / deli_d), int(denom1 * denom2 / deli_d))


def sub(rational1, rational2):
    numer1 = get_numer(rational1)
    denom1 = get_denom(rational1)
    numer2 = get_numer(rational2)
    denom2 = get_denom(rational2)
    deli_d = math.gcd(int(get_denom(rational1)), int(get_denom(rational2)))
    return make_rational(int((numer1 * denom2 - numer2 * denom1) / deli_d), int(denom1 * denom2 / deli_d))

# END


def rat_to_string(rational):
    return "{}/{}".format(get_numer(rational), get_denom(rational))