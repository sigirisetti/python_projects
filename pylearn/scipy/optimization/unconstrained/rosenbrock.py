import numpy as np
import pandas as pd
from scipy.optimize import minimize
from util import timer

df = pd.DataFrame.from_items([('Optimization Method', []), ('Iterations', []), ('Function Evaluations', []), ('Status', []), ('Message', []), ('Time in Secs', []), ])


def rosen(x):
    """The Rosenbrock function"""
    # print(sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0))
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)


def rosen_der(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[-1] = 200*(x[-1]-x[-2]**2)
    return der


def rosen_hess(x):
    x = np.asarray(x)
    H = np.diag(-400*x[:-1],1) - np.diag(400*x[:-1],-1)
    diagonal = np.zeros_like(x)
    diagonal[0] = 1200*x[0]**2-400*x[1]+2
    diagonal[-1] = 200
    diagonal[1:-1] = 202 + 1200*x[1:-1]**2 - 400*x[2:]
    H = H + np.diag(diagonal)
    return H


def rosen_hess_p(x, p):
    x = np.asarray(x)
    Hp = np.zeros_like(x)
    Hp[0] = (1200*x[0]**2 - 400*x[1] + 2)*p[0] - 400*x[0]*p[1]
    Hp[1:-1] = -400*x[:-2]*p[:-2]+(202+1200*x[1:-1]**2-400*x[2:])*p[1:-1] \
               -400*x[1:-1]*p[2:]
    Hp[-1] = -400*x[-2]*p[-2] + 200*p[-1]
    return Hp


def addRes(name, t, res):
    df.loc[len(df)] = [name, res['nit'], res['nfev'], res['status'], res['message'], t.secs]


########### Nelder Mead ##################################

with timer.Timer() as t:
    x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
    res = minimize(rosen, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})

addRes('Nelder Mead', t, res)


########### BFGS ##################################

with timer.Timer() as t:
    res = minimize(rosen, x0, method='BFGS', jac=rosen_der, options={'disp': True})
addRes('BFGS', t, res)



########### Conjugate Gradient ##################################

with timer.Timer() as t:
    res = minimize(rosen, x0, method='Newton-CG', jac=rosen_der, hess=rosen_hess, options={'xtol': 1e-8, 'disp': True})
addRes('Newton-CG', t, res)



########### Conjugate Gradient ##################################

with timer.Timer() as t:
    res = minimize(rosen, x0, method='Newton-CG', jac=rosen_der, hessp=rosen_hess_p, options={'xtol': 1e-8, 'disp': True})
addRes('Newton-CG Hessian Product', t, res)



# print(dict(res))
########### Final Results ##################################

with pd.option_context('display.width', 300):
    print(df)
