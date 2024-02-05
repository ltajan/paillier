import primes




class PaillierPubkey(object):

    def __init__(self, n):
        self.n = n
        self.g = n + 1
        self.nsquare = n * n

    def __repr__(self):
        return '<PaillierPubKey: %s' % self.n

    def __eq__(self, other):
        return self.n == other.n


def keygen(size):

    p = primes.generate_prime(size)

    return p