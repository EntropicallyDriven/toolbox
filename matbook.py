import re
class Mat:

    def __init__(self, matname):
        matname = matname.lower()

        matdata = open(r'C:\Users\Joshua\Documents\Code\toolbox\matdata.csv')
        alldata = matdata.read()
        matdata.close()

        lines = alldata.split('\n')
        lines = lines[:-1]

        names = []

        for line in lines:
            name = re.search('\A[^,]+',line)
            name = name.group(0)
            name = name.lower()
            names.append(name)

        if matname in names:
            index = names.index(matname)
        else:
            index = names.index('unknown')

        data = lines[index]

        data = data.split(',')

        self.data = data
        self.units = lines[0].split(',')
        self.labels = lines[1].split(',')

        for ii, datum in enumerate(data):
            if datum == '':
                data[ii] = None

        self.name        =     float(data[0])
        ############  MECHANICAL ########################
        self.density     =     float(data[1])    # kg/m^3

        ############   THERMAL   ########################
        self.specheat    =     float(data[2])    # J/kg
        self.condt       =     float(data[3])    # W/m K
        self.tmelt       =     float(data[4])    # K

        ############  ELECTRICAL ########################
        self.resist      =     float(data[5])    # Ohm m

        ############   OPTICAL   ########################
        self.emis_pol    =     float(data[6])
        self.emis_ox     =     float(data[7])


    def __str__(self):
        string = 'A package of facts about ' + self.name + '.'
        return string


    def knowndata(self):
        for ii,datum in enumerate(self.data[1:]):
            if datum is not None:
                print self.labels[ii+1] , '=', self.data[ii+1], ' ', self.units[ii+1]
