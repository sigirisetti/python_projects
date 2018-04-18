from PyDSTool import *
import matplotlib.pyplot as plt

icdict = {'x': 1, 'y': 0.4}
pardict = {'k': 0.3, 'm': 0.5}
x_rhs = 'y'
y_rhs = '-k*x/m'
vardict = {'x': x_rhs, 'y': y_rhs}


DSargs = args()                   # create an empty object instance of the args class, call it DSargs
DSargs.name = 'SHM'               # name our model
DSargs.ics = icdict               # assign the icdict to the ics attribute
DSargs.pars = pardict             # assign the pardict to the pars attribute
DSargs.tdata = [0, 200]            # declare how long we expect to integrate for
DSargs.varspecs = vardict         # assign the vardict dictionary to the 'varspecs' attribute of DSargs

DS = Generator.Vode_ODEsystem(DSargs)


traj = DS.compute('demo')
pts = traj.sample()

plt.plot(pts['t'], pts['x'], label='x')
plt.plot(pts['t'], pts['y'], label='y')
plt.legend()
plt.xlabel('t')
plt.show()

def KE(pts):
    return 0.5*DS.pars['m']*pts['y']**2

def PE(pts):
    return 0.5*DS.pars['k']*pts['x']**2

total_energy = KE(pts) + PE(pts)

print(total_energy)