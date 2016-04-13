import numpy as np
import matplotlib.pyplot as plt

class Phase:
    def __init__(self,name,cell,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.name = name
        self.cell = cell

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def allowed(cell,h,k,l):
    """Determine whether the given plane is an allowed reflection for the given cell"""
    if cell=="I":
        return (h+k+l)%2==0
    elif cell=="F":
        a1 = (h%2==0) and (k%2==0) and (l%2==0)
        a2 = (h%2==1) and (k%2==1) and (l%2==1)
        return a1 or a2
    elif cell=='D':
        a1 = (h%2==0) and (k%2==0) and (l%2==0)
        a2 = (h%2==1) and (k%2==1) and (l%2==1)
        a3 = (h+k+l)%4==0
        if a1:
            return not a3
        else:
            return a1 or a2
    elif cell=='H':
        a1 = (l%2==1)
        a2 = ((h+2*k)%3)==0
        a3 = ((2*h+k)%3)==0
        return not (a1 or a2 or a3)
    else:
        return True




def spacings(phase,num, **kwargs):
    """Compile a list of all allowed plane spacings for the given phase"""
    ii = 0
    planes = []
    indices = []
    k1=1
    k2=k3=0
    hkl = np.array((k1,k2,k3))
    h,k,l = hkl
    perm = 5
    while ii<num*2:
        if perm == 5:
            if k3==k2:
                if k3==k1:
                    k1+=1
                    k2=k3=0
                else:
                    k2+=1
                    k3=0
            else:
                k3+=1
            hkl = np.array((k1,k2,k3))
            perm = 0

        else:
            if perm==2:
                hkl = hkl[::-1]
            else:
                hkl = np.roll(hkl,1)

            h,k,l = hkl
            perm += 1

        if allowed(phase.cell,h,k,l):
            if phase.cell=='H':
                xx = 4*(h**2 + h*k + k^2)/(3*phase.a**2) + l**2/c**2
            else:
                xx = (h/phase.a)**2 + (k/phase.b)**2 + (l/phase.c)**2
            d = np.sqrt(1./xx)
            if d not in planes:
                planes.append(d)
                indices.append("(%d%d%d)"%(h,k,l))
                ii+=1

    planes, indices = zip(*sorted(zip(planes, indices)))
    planes = np.array(planes)
    indices = list(indices)
    indices = indices[::-1]
    planes = planes[::-1]

    if 'dmin' in kwargs:
        dmin = kwargs['dmin']
        for ii in range(len(planes))[::-1]:
            if planes[ii]<dmin:
                planes = np.delete(planes,ii)
                indices.remove(indices[ii])
    if len(planes)>num:
        indices = indices[:num]
        planes = planes[:num]
    return indices, planes



def gelplot(data,phases,num, **kwargs):
    """Compare graphically some data (1/d) against some candidate phases"""
    allpeaks = {}
    for phase in phases:
        if 'dmin' in kwargs:
            indices, planes = spacings(phase,num,dmin=kwargs['dmin'])
        else:
            indices, planes = spacings(phase,num)
        planes = np.array(planes)
        allpeaks[phase.name] = (indices, 1/planes)

    numphases = len(phases)*1.0
    plt.figure(figsize=(15,5))
    axes = plt.gca()
    cm_subsection = np.linspace(0, 1, numphases)
    colors = [ cm.jet(x) for x in cm_subsection ]

    plt.vlines(data,0,1,linestyle='--',linewidth = 2)

    for ii,phase in enumerate(phases):
        indices = allpeaks[phase.name][0]
        planes = allpeaks[phase.name][1]

        offset = 0.2/numphases
        top = ((ii+1.0)/numphases) - offset
        bottom = (ii)/numphases + offset


        plt.vlines(planes,bottom, top ,colors[ii], linewidth = 4)
        for jj, index in enumerate(allpeaks[phase.name][0]):
            if (jj%2):
                plt.text(planes[jj],bottom-offset/2,indices[jj],color=colors[ii],backgroundcolor = 'w',ha='center')
            else:
                plt.text(planes[jj],top+offset/4,indices[jj],color=colors[ii],backgroundcolor = 'w',ha='center')
        plt.text(np.min(data)/2,(top+bottom)/2,'('+phase.name+')',color=colors[ii],fontsize = 18, ha='center')
        plt.xlim(0,axes.get_xlim()[1]*1.05)

        plt.xlabel('Ring Spacing (1/nm)',fontsize = 18)

        axes.get_yaxis().set_visible(False)
