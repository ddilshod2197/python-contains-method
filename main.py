class Harf:
    def __init__(self, harf):
        self.harflar = [harf]

    def __contains__(self, harf):
        return harf in self.harflar

class Soz:
    def __init__(self, soz):
        self.soz = soz

    def __contains__(self, harf):
        return harf in self.soz

harf = Harf("a")
soz = Soz("alma")

print("a" in harf)  # True
print("a" in soz)   # True
print("b" in harf)  # False
print("b" in soz)   # False
