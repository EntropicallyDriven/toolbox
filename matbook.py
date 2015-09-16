class Mat:

    def __init__(self, matname):

        self.MB_INDEX = ['Al',
                         'OFE_Cu',
                         'BeCu']

        self.name         =     matname

        ############  MECHANICAL ########################
        self._density     =     None    #kg/m^3

        ############   THERMAL   ########################
        self._specheat    =     None    #J/kg
        self._tcond       =     None    #W/m K
        self.tmelt        =     None

        ############  ELECTRICAL ########################
        self._resist      =     None    #Ohm m

        ############   OPTICAL   ########################
        self._emis_pol    =     None
        self._emis_ox     =     None



        if matname == 'Al':

            self.name         =     'Aluminum'
            self._density     =     2700.0

            self._specheat    =     902.0
            self._tcond       =     205.0
            self._tmelt       =     933.7

            self._resist      =     2.65e-8
            self._cond        =     1.0/self._resist

            self._emis_pol    =     0.03
            self._emis_ox     =     0.6


        elif matname == 'OFE_Cu':
            self._name = 'Oxygen Free Electronic Copper'

            self._density     =     8960.0
            self._specheat    =     385.0


        elif matname == 'BeCu':
            self._name = 'Beryllium Copper'

            self._density     =     8250.0
            self._specheat    =     420.0
            self._tmelt       =     1139.0
            self._resist      =     8.21e-8


        else:
            print('Unknown Material!')


    def __str__(self):
        _string = 'A package of facts about ' + self._name + '.'
        return _string


    def knowndata(self):
        data = self.__dict__.copy()
        for attr in data.keys():
            if data[attr] is None:
                del data[attr]
        del data['MB_INDEX']
        return data


    def index(self):
        return self.MB_INDEX

    @property
    def name(self):
        return self._name




    ##############  MECHANICAL ########################
    @property
    def density(self):
        if self._density is not None:
            return self._density
        else:
            raise NoMatDataError(self._name,'density')


    ###############  THERMCAL  ########################
    @property
    def specheat(self):
        if self._specheat is not None:
            return self._specheat
        else:
            raise NoMatDataError(self._name,'specific heat')

    @property
    def tcond(self):
        if self._tcond is not None:
            return self._tcond
        else:
            raise NoMatDataError(self._name,'thermal conductivity')


    @property
    def tmelt(self):
        if self._tmelt is not None:
            return self._tmelt
        else:
            raise NoMatDataError(self._name,'melting temperature')


    ##############  ELECTRICAL ########################
    @property
    def resist(self):
        if self._resist is not None:
            return self._resist
        else:
            raise NoMatDataError(self._name,'resistivity')

    @property
    def cond(self):
        if self._cond is not None:
            return self._cond
        else:
            raise NoMatDataError(self._name,'conductivity')


    ##############   OPTICAL   ########################
    @property
    def emis_pol(self):
        if self._emis_pol is not None:
            return self._emis_pol
        else:
            raise NoMatDataError(self._name,'polished emissivity')

    @property
    def emis_ox(self):
        if self._specheat is not None:
            return self._specheat
        else:
            raise NoMatDataError(self._name,'oxidized emissivity')



class NoMatDataError(Exception):
    def __init__(self,matname,attrname):
        self.matname = matname
        self.attrname = attrname
    def __str__(self):
        string = 'Error: no value of ' + self.attrname + ' available for ' + self.matname + '!'
        return string
