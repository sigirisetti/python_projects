import QuantLib as ql
import math

# calendar = ql.UnitedStates(ql.UnitedStates.NYSE)
# bussiness_convention = ql.ModifiedFollowing
# settlement_days = 0

###########################################
# Build yield curve
###########################################
calc_date = ql.Date(23, 9, 2015)
ql.Settings.instance().evaluationDate = calc_date

day_count = ql.ActualActual(ql.ActualActual.ISMA)
interest_rate = 0.0015
yield_curve = ql.FlatForward(calc_date, interest_rate, day_count, ql.Compounded, ql.Continuous)

T = 96.12/365.

strike = 3.5
spot = 2.919
volatility = 0.4251
flavor = ql.Option.Call

discount = yield_curve.discount(T)
###########################################
# Build yield curve
###########################################
strikepayoff = ql.PlainVanillaPayoff(flavor, strike)
stddev = volatility*math.sqrt(T)
strikepayoff = ql.PlainVanillaPayoff(flavor, strike)
black = ql.BlackCalculator(strikepayoff, spot, stddev, discount)

print("%-20s: %4.4f" %("Option Price", black.value() ))
print("%-20s: %4.4f" %("Delta", black.delta(spot) ))
print("%-20s: %4.4f" %("Gamma", black.gamma(spot) ))
print("%-20s: %4.4f" %("Theta", black.theta(spot, T) ))
print("%-20s: %4.4f" %("Vega", black.vega(T) ))
print("%-20s: %4.4f" %("Rho", black.rho( T) ))