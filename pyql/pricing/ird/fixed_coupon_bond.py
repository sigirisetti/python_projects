import QuantLib as ql

print(3/pow(1+0.005, 0.5) + (100 + 3)/(1+0.007))

todaysDate = ql.Date(15, 1, 2015)
ql.Settings.instance().evaluationDate = todaysDate
###########################################
# Construct spot curve
###########################################
dayCount = ql.Thirty360(ql.Thirty360.BondBasis)
calendar = ql.UnitedStates(ql.UnitedStates.Settlement)
interpolation = ql.Linear()
compounding = ql.Compounded
compoundingFrequency = ql.Annual
spotDates = [ql.Date(15, 1, 2015), ql.Date(15, 7, 2015), ql.Date(15, 1, 2016)]
spotRates = [0.0, 0.005, 0.007]
spotCurve = ql.ZeroCurve(spotDates, spotRates, dayCount, calendar, interpolation,
                             compounding, compoundingFrequency)
spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)

###########################################
# Create a schedule
###########################################
issueDate = ql.Date(15, 1, 2015)
maturityDate = ql.Date(15, 1, 2016)
tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates(ql.UnitedStates.Settlement)
bussinessConvention = ql.Unadjusted
dateGeneration = ql.DateGeneration.Backward
monthEnd = False
schedule = ql.Schedule (issueDate, maturityDate, tenor, calendar, bussinessConvention,
                            bussinessConvention , dateGeneration, monthEnd)

print('Schedule : ', list(schedule))

# Now lets build the coupon
dayCount = ql.Thirty360(ql.Thirty360.BondBasis)
couponRate = .06
coupons = [couponRate]

###########################################
# Now lets construct the FixedRateBond Instrument
###########################################
settlementDays = 0
faceValue = 100
fixedRateBond = ql.FixedRateBond(settlementDays, faceValue, schedule, coupons, dayCount)

###########################################
# create a bond engine with the term structure as input;
# set the bond to use this bond engine
###########################################
bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
fixedRateBond.setPricingEngine(bondEngine)

# Finally the price
print(fixedRateBond.NPV())