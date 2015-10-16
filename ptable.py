import re

class Ptable:
    def __init__(self, element):
        elemname = element.lower()

        elemdata = open(r'C:\Users\Joshua\Documents\Code\toolbox\elemdata.csv')
        alldata = elemdata.read()
        elemdata.close()

        lines = alldata.split('\n')
        lines = lines[:-1]

        names = []

        for line in lines:
            name = re.search('\A[^,]+',line)
            name = name.group(0)
            name = name.lower()
            names.append(name)

        if elemname in names:
            index = names.index(elemname)
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

        self.name         =     data[0]
        self.num          =     float(data[1])
        self.mass         =     float(data[2])    # kg


    def __str__(self):
        string = 'A package of facts about ' + self.name + '.'
        return string


    def knowndata(self):
        for ii,datum in enumerate(self.data[1:]):
            if datum is not None:
                print self.labels[ii+1] , '=', self.data[ii+1], ' ', self.units[ii+1]
