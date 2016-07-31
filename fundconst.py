import gc
class Constant:
    def __init__(self, sym, value, unit, name):
        self.sym = sym
        self.value = value
        self.unit = unit
        self.name = name

    def __str__(self):
        val = '%e ' % self.value
        string = self.sym + '\t' + self.name + ': ' + self.sym + ' = ' + val + self.unit
        return string
    def __repr__(self):
        val = '%e ' % self.value
        string = self.sym + '\t' + self.name + ': ' + self.sym + ' = ' + val + self.unit
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


a0    = Constant('a0',    0.5291772067e-10, 'm',        'Bohr Radius')
alpha = Constant('alpha', 7.2973525664e-3,  ' ',        'Fine Structure Constant')
c     = Constant('c',     299792458,        'm/s',      'Speed of Light')
ec    = Constant('e',     1.6021766208e-19, 'C',        'Elementary Charge')
eps0  = Constant('eps0',  8.854187817e-12,  'F/m',      'Electric Constant')
ge    = Constant('ge',   -2.00231930436182, ' ',        'Electron g-factor')
gn    = Constant('gn',   -3.82608545,       ' ',        'Neutron g-factor')
gp    = Constant('gp',    5.585694702,      ' ',        'Proton g-factor')
h     = Constant('h',     6.626070040e-34,  'J/s',      'Planck\'s Constant')
hbar  = Constant('hbar',  1.054571800e-34,  'J s',      'Reduced Planck\'s Constant')
kB    = Constant('kB',    1.38064852e-23,   'J/K',      'Boltzmann\'s Constant')
muB   = Constant('muB',   927.4009994e-26,  'J/T',      'Bohr Magneton')
muN   = Constant('muN',   5.050783699e-27,  'J/T',      'Nuclear Magneton')
nA    = Constant('nA',    6.022140857e23,   ' ',        'Avogadro\'s Number')
me    = Constant('me',    9.10938356e-31,   'kg',       'Electron Mass')
mn    = Constant('mn',    1.674927471e-27,  'kg',       'Neutron Mass')
mp    = Constant('mp',    1.672621898e-27,  'kg',       'Proton Mass')
mu0   = Constant('mu0',   12.566370614e-7,  'N/A^2',    'Magnetic Constant')
R     = Constant('R',     8.3144598,        'J/mol K',  'Molar Gas Constant')
sb    = Constant('sb',    5.670367e-8,      'W/m^2 K^4','Stefan-Boltzman constant')

def index():
    allconstants = []
    for obj in gc.get_objects():
        if isinstance(obj, Constant):
            allconstants.append(str(obj))
    allconstants.sort()
    for const in allconstants:
        print(const)

