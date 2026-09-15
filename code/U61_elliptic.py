"""Exact arithmetic on the U61 elliptic curve over Q(sqrt(17))."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
import json

@dataclass(frozen=True)
class K:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, 'a', Fraction(self.a))
        object.__setattr__(self, 'b', Fraction(self.b))

    def __add__(self, other: K | int) -> K:
        q = other if isinstance(other, K) else K(Fraction(other))
        return K(self.a+q.a, self.b+q.b)

    __radd__ = __add__

    def __neg__(self) -> K:
        return K(-self.a, -self.b)

    def __sub__(self, other: K | int) -> K:
        return self + -other

    def __rsub__(self, other: int) -> K:
        return -self + other

    def __mul__(self, other: K | int) -> K:
        q = other if isinstance(other, K) else K(Fraction(other))
        return K(self.a*q.a+17*self.b*q.b, self.a*q.b+self.b*q.a)

    __rmul__ = __mul__

    def __truediv__(self, other: K | int) -> K:
        q = other if isinstance(other, K) else K(Fraction(other))
        norm = q.a*q.a-17*q.b*q.b
        if not norm:
            raise ZeroDivisionError('Zero field element')
        return self*K(q.a/norm, -q.b/norm)

    def __rtruediv__(self, other: int) -> K:
        return K(Fraction(other))/self

    def __pow__(self, n: int) -> K:
        if n < 0:
            return (1/self)**(-n)
        out, base = K(Fraction(1)), self
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n >>= 1
        return out

    def mod(self, modulus: int) -> tuple[int, int]:
        return tuple(f.numerator*pow(f.denominator, -1, modulus) % modulus
                     for f in (self.a, self.b))

    def serial(self) -> list[str]:
        return [str(self.a), str(self.b)]

ZERO = K()
PI = K(Fraction(0), Fraction(1))
AE = 4-PI
BE = -8+33*PI/17
Point = tuple[K, K] | None
P: Point = (17*K(Fraction(1))/4-PI, -16+31*PI/8)
T: Point = (ZERO, ZERO)


def on_curve(p: Point) -> bool:
    if p is None:
        return True
    x, y = p
    return y*y == x**3+AE*x*x+BE*x


def add(p: Point, q: Point) -> Point:
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    u, v = q
    if x == u:
        if y+v == ZERO:
            return None
        slope = (3*x*x+2*AE*x+BE)/(2*y)
    else:
        slope = (v-y)/(u-x)
    xx = slope*slope-AE-x-u
    yy = -y+slope*(x-xx)
    result = (xx, yy)
    assert on_curve(result)
    return result


def mul(n: int, p: Point) -> Point:
    if n < 0:
        return mul(-n, None if p is None else (p[0], -p[1]))
    out: Point = None
    while n:
        if n & 1:
            out = add(out, p)
        p = add(p, p)
        n >>= 1
    return out


def u_coordinate(q: Point) -> K:
    if q is None:
        return K(Fraction(2))
    x, y = q
    big_x = x+(PI-5)/2
    return 2+(2*y+(6-PI)*big_x+(13-3*PI))/(big_x*big_x-4*(1-4*PI/17))


def main() -> None:
    assert PI*PI == K(Fraction(17))
    assert (PI+4)*(PI-4) == K(Fraction(1))
    assert on_curve(P) and on_curve(T)
    assert mul(2, T) is None
    assert u_coordinate(P) == K(Fraction(2))
    m = mul(22, P)
    assert m is not None
    parameter = -m[0]/m[1]
    m8 = mul(8, P)
    assert m8 is not None
    tau8 = -m8[0]/m8[1]
    assert (tau8/3).mod(3) == (2, 2)
    scanned = []
    for n in range(-6, 7):
        for torsion in (0, 1):
            q = mul(n, P)
            if torsion:
                q = add(q, T)
            u = u_coordinate(q)
            if not u.b:
                scanned.append({'n': n, 'torsion': torsion, 'u': str(u.a)})
    print(json.dumps({
        'status': 'completed', 'P': [coord.serial() for coord in P],
        'M_22P': [coord.serial() for coord in m],
        'M_8P': [coord.serial() for coord in m8],
        'tau_8P': tau8.serial(),
        'tau_8P_mod9': tau8.mod(9),
        'tau_8P_div3_mod3': (tau8/3).mod(3),
        'formal_parameter_minus_x_over_y': parameter.serial(),
        'formal_parameter_mod125': parameter.mod(125),
        'formal_parameter_div5_mod25': (parameter/5).mod(25),
        'u_T': u_coordinate(T).serial(),
        'bounded_scan': {'n_min': -6, 'n_max': 6, 'torsion': [0, 1],
                         'rational_u': scanned, 'not_a_completeness_proof': True}
    }, indent=2))

if __name__ == '__main__':
    main()
