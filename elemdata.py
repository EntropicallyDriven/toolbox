class ElemData:
    def __init__(self, element):
        elemdata = open(r'C:\Users\Joshua\Documents\Code\toolbox\elemdata.csv')
        alldata = elemdata.read()
        elemdata.close()

        lines = alldata.split('\n')
        lines = lines[:-1]

        for ii,line in enumerate(lines):
            if line.split(',')[0] == element:
                index = ii
                break
        data = lines[index]

        data = data.split(',')

        self.data = data
        self.units = lines[0].split(',')
        self.labels = lines[1].split(',')

        for ii, datum in enumerate(data):
            if datum == '':
                data[ii] = None

        self.sym     =     data[0]
        self.name    =     data[1]
        self.num     =     int(data[2])
        self.mass    =     float(data[3])    # amu
        self.density =     float(data[4])    # g/cm3
        self.tmelt   =     float(data[5])    # K
        self.tboil   =     float(data[6])    # K
        self.eneg    =     float(data[7])    # Pauling Scale


    def __str__(self):
        string = 'A package of facts about ' + self.name + '.'
        return string


    def knowndata(self):
        for ii,datum in enumerate(self.data[1:]):
            if datum is not None:
                print(self.labels[ii+1] , '=', self.data[ii+1], ' ', self.units[ii+1])
