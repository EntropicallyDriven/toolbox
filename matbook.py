class Mat:
    def __init__(self, matname):

        self._knownmats = ['Al','OFE_Cu']

        if matname in self.knownmats:
            self._name = matname
        else:
            self._name = 'unknown'
        self._density = None

        self._specheat = None
        self._tcond = None

        self._resist = None

        self._emis_pol = None
        self._emis_ox = None



        if matname == 'Al':
            self._name = 'Aluminum'
            self._density = 27000.0    #kg/m

            self._specheat = 902.0     #J/kg
            self._tcond = 205.0        #W/m K

            self._resist = 2.65e-8     #Ohm/m

            self._emis_pol = 0.03
            self._emis_ox = 0.6


        elif matname == 'OFE_Cu':
            self._name = 'Oxygen Free Electronic Copper'
            self._density = 8960


        else:
            print('Unknown Material!')


    def __str__(self):
        _string = 'A package of facts about ' + self._name + '.'
        return _string


    def knowndata(self):
        data = self.__dict__
        for attr in data.keys():
            del data['knownmats']
            if data[attr] is None:
                del data[attr]
        return data



    @property
    def knownmats(self):
        return self._knownmats


    @property
    def density(self):
        if self._density is not None:
            return self._density
        else:
            raise NoMatDataError(self._name,'density')

    @property
    def resist(self):
        if self._resist is not None:
            return self._resist
        else:
            raise NoMatDataError(self._name,'resistivity')



class NoMatDataError(Exception):
    def __init__(self,matname,attrname):
        self.matname = matname
        self.attrname = attrname
    def __str__(self):
        string = 'Error: no value of ' + self.attrname + ' available for ' + self.matname + '!'
        return string
