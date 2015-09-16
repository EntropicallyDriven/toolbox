class Constant:
    def __init__(self, sym, value, unit, name):
        self.sym = sym
        self.value = value
        self.unit = unit
        self.name = name

    def __str__(self):
        val = '%e ' % self.value
        string = self.name + ': ' + self.sym + ' = ' + val + self.unit
        return string


    def __add__(self, other):
        return self.value + other
    def __radd__(self, other):
        return self.value + other


    def __sub__(self, other):
        return self.value - other
    def __rsub__(self, other):
        return other - self.value


    def __neg__(self):
        return -self.value


    def __mul__(self, other):
        return self.value * other
    def __rmul__(self, other):
        return self.value * other


    def __div__(self, other):
        return self.value / other
    def __rdiv__(self, other):
        return  other / self.value

    def __pow__(self, other):
        return self.value**other
    def __rpow__(self, other):
        return other**self.value
