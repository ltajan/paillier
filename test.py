#!/usr/bin/env python
import paillier

print ("on test")

pub, priv = paillier.keygen(256)

m1 = 3
m2 = 5
ct1 = paillier.encrypt(pub, m1)
ct2 = paillier.encrypt(pub, m2)
ct3 = paillier.add(pub, ct1, ct2)
ct4 = paillier.mul(pub, ct1, m2)
print(paillier.decrytp(priv, ct3))
print(paillier.decrytp(priv, ct4))

