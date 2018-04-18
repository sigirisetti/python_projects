import numpy as np
from scipy.integrate import odeint

def myode(f, x):
    return 3*x**2 + 12*x -4

def event(f, x):
    'an event is when f = 0'
    return f

# initial conditions
x0 = -8
f0 = -120

# final x-range and step to integrate over.
xf = 4   #final x value
deltax = 0.45 #xstep

# lists to store the results in
X = [x0]
sol = [f0]
e = [event(f0, x0)]
events = []
x2 = x0
# manually integrate at each time step, and check for event sign changes at each step
while x2 <= xf: #stop integrating when we get to xf
    x1 = X[-1]
    x2 = x1 + deltax
    f1 = sol[-1]

    f2 = odeint(myode, f1, [x1, x2]) # integrate from x1,f1 to x2,f2
    X += [x2]
    sol += [f2[-1][0]]

    # now evaluate the event at the last position
    e += [event(sol[-1], X[-1])]

    if e[-1] * e[-2] < 0:
        # Event detected where the sign of the event has changed. The
        # event is between xPt = X[-2] and xLt = X[-1]. run a modified bisect
        # function to narrow down to find where event = 0
        xLt = X[-1]
        fLt = sol[-1]
        eLt = e[-1]

        xPt = X[-2]
        fPt = sol[-2]
        ePt = e[-2]

        j = 0
        while j < 100:
            if np.abs(xLt - xPt) < 1e-6:
                # we know the interval to a prescribed precision now.
                print('x = {0}, event = {1}, f = {2}'.format(xLt, eLt, fLt))
                events += [(xLt, fLt)]
                break # and return to integrating

            m = (ePt - eLt)/(xPt - xLt) #slope of line connecting points
                                        #bracketing zero

            #estimated x where the zero is
            new_x = -ePt / m + xPt

            # now get the new value of the integrated solution at that new x
            f  = odeint(myode, fPt, [xPt, new_x])
            new_f = f[-1][-1]
            new_e = event(new_f, new_x)

            # now check event sign change
            if eLt * new_e > 0:
                xPt = new_x
                fPt = new_f
                ePt = new_e
            else:
                xLt = new_x
                fLt = new_f
                eLt = new_e

            j += 1


import matplotlib.pyplot as plt
plt.plot(X, sol)

plt.show()
# add event points to the graph
for x,e in events:
    plt.plot(x,e,'bo ')
plt.savefig('c:/tmp/event-ode-1.png')