class LCG:
    def __init__(self, seed):
        self.seed = seed
        self.modulus = 2**31 - 1
        self.multiplier = 48271
        self.increment = 0

    def random(self):
        self.seed = self.seed * self.multiplier
        self.seed = self.seed + self.increment
        self.seed = self.seed % self.modulus
        return self.seed/self.modulus

lcg = LCG(456787654567)

for i in range(0,10):
    print(float(lcg.random()/lcg.modulus))


