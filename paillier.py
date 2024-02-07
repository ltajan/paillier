import primes
import random

def invmod(a, n, maxiter=1000000):
    if a == 0:
        raise ValueError('%d has no inverse mod %d' % (a,n))
    
    r = a
    d = 1
    for i in range(min(n, maxiter)):
        d = ((n // r + 1) * d) % n
        r = (d * a) % n
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, n))
    
    return d


class PaillierPubkey(object):

    def __init__(self, n):
        self.n = n
        self.nsquare = n * n

    def __repr__(self):
        return '<PaillierPubKey: %s>' % self.n

    def __eq__(self, other):
        return self.n == other.n
    
class PaillierPrivkey(object):

    def __init__(self, p, q, n):
        if p*q != n:
            raise ValueError('public key n does not match p and q')
        self.n = n
        self.nsquare = n * n
        self.psi = (p-1)*(q-1)

        x = (pow(random.randrange(1, self.nsquare), self.psi, self.nsquare)-1)//self.n

        self.mu = invmod(self.psi, self.n)


def keygen(size):

    p = primes.generate_prime(size)
    q = primes.generate_prime(size)
    n = p*q

    return PaillierPubkey(n), PaillierPrivkey(p, q, n)


def encrypt(pubkey, plain):

    r = random.randrange(1, pubkey.n)
    r_pow = pow(r, pubkey.n, pubkey.nsquare)

    ct = (pow((1+pubkey.n), plain, pubkey.nsquare) * r_pow) % pubkey.nsquare

    return ct


def decrytp(privkey, ct):

        x = pow(ct, privkey.psi, privkey.nsquare) - 1
        Lx = x//privkey.n
        plain = (Lx * privkey.mu) % privkey.n

        return plain