import re

def entries():
    matdata = open(r'C:\Users\Joshua\Documents\Code\toolbox\matdata.csv')
    alldata = matdata.read()
    matdata.close()

    lines = alldata.split('\n')
    lines = lines[:-1]

    entries = []

    for line in lines[2:-1]:
        entry = re.search('\A[^,]+',line)
        entry = entry.group(0)
        entry = entry.lower()
        entries.append(entry)
    return entries

class Mat:

    def __init__(self, matname):
        matname = matname.lower()

        matdata = open(r'C:\Users\Joshua\Documents\Code\toolbox\matdata.csv')
        alldata = matdata.read()
        matdata.close()

        lines = alldata.split('\n')
        lines = lines[:-1]

        self.names = []

        for line in lines:
            name = re.search('\A[^,]+',line)
            name = name.group(0)
            name = name.lower()
            self.names.append(name)

        if matname in self.names:
            index = self.names.index(matname)
        else:
            index = self.names.index('unknown')

        data = lines[index]

        data = data.split(',')

        self.data = data
        self.units = lines[0].split(',')
        self.labels = lines[1].split(',')

        for ii, datum in enumerate(data):
            if datum == '':
                data[ii] = None
            if ii is not 0 and data[ii] is not None:
                data[ii] = float(data[ii])

        self.name        =     data[0]
        ############  MECHANICAL ########################
        self.density     =     data[1]    # kg/m^3

        ############   THERMAL   ########################
        self.specheat    =     data[2]    # J/kg
        self.condt       =     data[3]    # W/m K
        self.tmelt       =     data[4]    # K
		
        ############  ELECTRICAL ########################
        self.conde       =	   data[5]    # S/m
        self.resist      =     data[6]    # Ohm m

        ############   OPTICAL   ########################
        self.emis_pol    =     data[7]
        self.emis_ox     =     data[8]


    def __str__(self):
        string = 'A package of facts about ' + self.name + '.'
        return string

    def knowndata(self):
        for ii,datum in enumerate(self.data[1:]):
            if datum is not None:
                print(self.labels[ii+1] , '=', self.data[ii+1], ' ', self.units[ii+1])
