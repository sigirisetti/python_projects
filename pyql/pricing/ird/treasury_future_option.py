import QuantLib as ql
import math

# calendar = ql.UnitedStates(ql.UnitedStates.NYSE)
# bussiness_convention = ql.ModifiedFollowing
# settlement_days = 0
calc_date = ql.Date(1, 12, 2015)
ql.Settings.instance().evaluationDate = calc_date

###########################################
# Build yield curve
###########################################
interest_rate = 0.00105
day_count = ql.ActualActual(ql.ActualActual.ISMA)
yield_curve = ql.FlatForward(calc_date,
                             interest_rate,
                             day_count,
                             ql.Compounded,
                             ql.Continuous)

option_maturity_date = ql.Date(24, 12, 2015)
strike = 119
spot = 126.953  # futures price
volatility = 11.567 / 100.
flavor = ql.Option.Call

discount = yield_curve.discount(option_maturity_date)

###########################################
# Option payoff and Black calculator
###########################################
T = yield_curve.dayCounter().yearFraction(calc_date, option_maturity_date)
stddev = volatility * math.sqrt(T)
strikepayoff = ql.PlainVanillaPayoff(flavor, strike)
black = ql.BlackCalculator(strikepayoff, spot, stddev, discount)

print("%-20s: %4.4f" % ("Option Price", black.value()))
print("%-20s: %4.4f" % ("Delta", black.delta(spot)))
print("%-20s: %4.4f" % ("Gamma", black.gamma(spot)))
print("%-20s: %4.4f" % ("Theta", black.theta(spot, T)))
print("%-20s: %4.4f" % ("Vega", black.vega(T)))
print("%-20s: %4.4f" % ("Rho", black.rho(T)))
