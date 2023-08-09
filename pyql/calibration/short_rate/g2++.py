import QuantLib as ql
from collections import namedtuple
import math
from calibration_helper import *

# $d ln(r_t) = \big(\theta(t) - a ln(r(t))\big) dt + \sigma_t dW_t$

# where
# a is the mean reversion constant,
# σ is the volatility parameter.
# The parameter θ(t) is chosen in order to fit the input term structure of interest rates.

today = ql.Date(15, ql.February, 2002)
ql.Settings.instance().evaluationDate = today

settlement = ql.Date(19, ql.February, 2002)
term_structure = ql.YieldTermStructureHandle(ql.FlatForward(settlement, 0.04875825, ql.Actual365Fixed()))
index = ql.Euribor1Y(term_structure)

CalibrationData = namedtuple("CalibrationData", "start, length, volatility")
data = [CalibrationData(1, 5, 0.1148),
        CalibrationData(2, 4, 0.1108),
        CalibrationData(3, 3, 0.1070),
        CalibrationData(4, 2, 0.1021),
        CalibrationData(5, 1, 0.1000)]

model = ql.G2(term_structure);
engine = ql.TreeSwaptionEngine(model, 25)
# engine = ql.G2SwaptionEngine(model, 10, 400)
# engine = ql.FdG2SwaptionEngine(model)
###########################################
# Swaptions for calibration
##########################################
swaptions = create_swaption_helpers(data, index, term_structure, engine)

##########################################
# calibration using optimization
##########################################
optimization_method = ql.LevenbergMarquardt(1.0e-8, 1.0e-8, 1.0e-8)
end_criteria = ql.EndCriteria(10000, 100, 1e-6, 1e-8, 1e-8)
model.calibrate(swaptions, optimization_method, end_criteria)
##########################################
# Calibration params
##########################################
a, sigma, b, eta, rho = model.params()
print("a = %6.5f, sigma = %6.5f, b = %6.5f, eta = %6.5f, rho = %6.5f " % (a, sigma, b, eta, rho))

##########################################
# Calibration report
##########################################
calibration_report(swaptions, data)
