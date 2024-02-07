#!/usr/bin/env python
import paillier

print ("on test")

pub, priv = paillier.keygen(256)

m = 3

ct = paillier.encrypt(pub, m)

print(paillier.decrytp(priv, ct))

