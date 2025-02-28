from Crypto.PublicKey import RSA

class Wallet:

    def __init__(self):
        self.KeyPair = RSA.generate(bits = 2048)
