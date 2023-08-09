import QuantLib as ql
from collections import namedtuple
import math
import calibration_helper

today = ql.Date(15, ql.February, 2002);
settlement= ql.Date(19, ql.February, 2002);
ql.Settings.instance().evaluationDate = today;
term_structure = ql.YieldTermStructureHandle(ql.FlatForward(settlement,0.04875825,ql.Actual365Fixed()))
index = ql.Euribor1Y(term_structure)

CalibrationData = namedtuple("CalibrationData",
                             "start, length, volatility")
data = [CalibrationData(1, 5, 0.1148),
        CalibrationData(2, 4, 0.1108),
        CalibrationData(3, 3, 0.1070),
        CalibrationData(4, 2, 0.1021),
        CalibrationData(5, 1, 0.1000 )]

model = ql.ExtendedCoxIngersollRoss(term_structure)
# model = ql.CoxIngersollRoss(0.04875825)
engine = ql.TreeSwaptionEngine(model, 100)
swaptions = calibration_helper.create_swaption_helpers(data, index, term_structure, engine)

optimization_method = ql.LevenbergMarquardt(1.0e-8,1.0e-8,1.0e-8)
end_criteria = ql.EndCriteria(10000, 100, 1e-6, 1e-8, 1e-8)
model.calibrate(swaptions, optimization_method, end_criteria)

print(model.params())
# print("a = %6.5f, sigma = %6.5f" % (a, sigma))

calibration_helper.calibration_report(swaptions, data)