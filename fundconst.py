import constant as cc
import gc

reload(cc)

a0    = cc.Constant('a0',    0.5291772067e-10, 'm',        'Bohr Radius')
alpha = cc.Constant('alpha', 7.2973525664e-3,  ' ',        'Fine Structure Constant')
c     = cc.Constant('c',     299792458,        'm/s',      'Speed of Light')
ec    = cc.Constant('e',     1.6021766208e-19, 'C',        'Elementary Charge')
eps0  = cc.Constant('eps0',  8.854187817e-12,  'F/m',      'Electric Constant')
ge    = cc.Constant('ge',   -2.00231930436182, ' ',        'Electron g-factor')
gn    = cc.Constant('gn',   -3.82608545,       ' ',        'Neutron g-factor')
gp    = cc.Constant('gp',    5.585694702,      ' ',        'Proton g-factor')
h     = cc.Constant('h',     6.626070040e-34,  'J/s',      'Planck\'s Constant')
hbar  = cc.Constant('hbar',  1.054571800e-34,  'J s',      'Reduced Planck\'s Constant')
kB    = cc.Constant('kB',    1.38064852e-23,   'J/K',      'Boltzmann\'s Constant')
muB   = cc.Constant('muB',   927.4009994e-26,  'J/T',      'Bohr Magneton')
muN   = cc.Constant('muN',   5.050783699e-27,  'J/T',      'Nuclear Magneton')
nA    = cc.Constant('nA',    6.022140857e23,   ' ',        'Avogadro\'s Number')
me    = cc.Constant('me',    9.10938356e-31,   'kg',       'Electron Mass')
mn    = cc.Constant('mn',    1.674927471e-27,  'kg',       'Neutron Mass')
mp    = cc.Constant('mp',    1.672621898e-27,  'kg',       'Proton Mass')
mu0   = cc.Constant('mu0',   12.566370614e-7,  'N/A^2',    'Magnetic Constant')
R     = cc.Constant('R',     8.3144598,        'J/mol K',  'Molar Gas Constant')
sb    = cc.Constant('sb',    5.670367e-8,      'W/m^2 K^4','Stefan-Boltzman constant')

def index():
    allconstants = []
    for obj in gc.get_objects():
        if isinstance(obj, cc.Constant):
            allconstants.append(str(obj))
    allconstants.sort()
    for const in allconstants:
        print(const)
