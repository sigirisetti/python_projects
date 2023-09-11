import QuantLib as ql
import math

calc_date = ql.Date(30, 11, 2015)
ql.Settings.instance().evaluationDate = calc_date
day_count = ql.ActualActual(ql.ActualActual.ISMA)
calendar = ql.UnitedStates(ql.UnitedStates.NYSE)
bussiness_convention = ql.Following
end_of_month = False
settlement_days = 0
face_amount = 100

###########################################
# build curve
###########################################
prices = [99.9935, 99.9576, 99.8119, 99.5472, 99.8867, 100.0664, 99.8711, 100.0547, 100.3047, 100.2266]
coupon_rates = [0.0000, 0.0000, 0.0000, 0.0000, 0.00875, 0.0125, 0.01625, 0.02, 0.0225, 0.03]

maturity_dates = [ql.Date(24, 12, 2015), ql.Date(25, 2, 2016),
                  ql.Date(26, 5, 2016), ql.Date(10, 11, 2016),
                  ql.Date(30, 11, 2017), ql.Date(15, 11, 2018),
                  ql.Date(30, 11, 2020), ql.Date(30, 11, 2022),
                  ql.Date(15, 11, 2025), ql.Date(15, 11, 2045)]

issue_dates = [ql.Date(25, 6, 2015), ql.Date(27, 8, 2015),
               ql.Date(28, 5, 2015), ql.Date(12, 11, 2015),
               ql.Date(30, 11, 2015), ql.Date(16, 11, 2015),
               ql.Date(30, 11, 2015), ql.Date(30, 11, 2015),
               ql.Date(16, 11, 2015), ql.Date(16, 11, 2015)]

coupon_frequency = ql.Period(6, ql.Months)

bond_helpers = []
for coupon, issue_date, maturity_date, price in zip(coupon_rates, issue_dates, maturity_dates, prices):
    print("Coupon : {0}, issue_date : {1}, maturity_date : {2}, price : {3}".format(coupon, issue_date, maturity_date,
                                                                                    price))
    schedule = ql.Schedule(calc_date, maturity_date, coupon_frequency, calendar,
                           bussiness_convention, bussiness_convention, ql.DateGeneration.Backward, False)

    helper = ql.FixedRateBondHelper(ql.QuoteHandle(ql.SimpleQuote(price)), settlement_days, face_amount,
                                    schedule, [coupon], day_count, bussiness_convention)
    bond_helpers.append(helper)

yield_curve = ql.PiecewiseCubicZero(calc_date, bond_helpers, day_count)
yield_curve_handle = ql.YieldTermStructureHandle(yield_curve)
for d in maturity_dates:
    print("|%20s  %9.6f|" % (d, yield_curve.discount(d)))


def create_tsy_security(bond_issue_date, bond_maturity_date, coupon_rate, coupon_frequency=ql.Period(6, ql.Months),
                        day_count=ql.ActualActual(ql.ActualActual.ISMA),
                        calendar=ql.UnitedStates(ql.UnitedStates.NYSE)):
    face_value = 100.
    settlement_days = 0

    schedule = ql.Schedule(bond_issue_date, bond_maturity_date, coupon_frequency, calendar, ql.ModifiedFollowing,
                           ql.ModifiedFollowing, ql.DateGeneration.Forward, False)
    security = ql.FixedRateBond(settlement_days, face_value, schedule, [coupon_rate], day_count)
    return security


bond_issue_date = calc_date
delivery_date = ql.Date(1, 12, 2015)

bond_maturity_date = bond_issue_date + ql.Period(10, ql.Years)
coupon_frequency = ql.Period(6, ql.Months)
coupon_rate = 6 / 100.

deliverable = create_tsy_security(bond_issue_date, bond_maturity_date, coupon_rate, coupon_frequency, day_count,
                                  calendar)
bond_engine = ql.DiscountingBondEngine(yield_curve_handle)
deliverable.setPricingEngine(bond_engine)

futures_price = 127.0625
clean_price = futures_price * yield_curve.discount(delivery_date)

zspread = ql.BondFunctions.zSpread(deliverable, clean_price, yield_curve, day_count, ql.Compounded, ql.Semiannual,
                                   calc_date) * 10000
print("Z-Spread =%3.0fbp" % (zspread))

#######################################################################
# basket describes the coupon rate, maturity date, price
#######################################################################
day_count = ql.ActualActual(ql.ActualActual.ISMA)
basket = [(1.625, ql.Date(15, 8, 2022), 97.921875),
          (1.625, ql.Date(15, 11, 2022), 97.671875),
          (1.75, ql.Date(30, 9, 2022), 98.546875),
          (1.75, ql.Date(15, 5, 2023), 97.984375),
          (1.875, ql.Date(31, 8, 2022), 99.375),
          (1.875, ql.Date(31, 10, 2022), 99.296875),
          (2.0, ql.Date(31, 7, 2022), 100.265625),
          (2.0, ql.Date(15, 2, 2023), 100.0625),
          (2.0, ql.Date(15, 2, 2025), 98.296875),
          (2.0, ql.Date(15, 8, 2025), 98.09375),
          (2.125, ql.Date(30, 6, 2022), 101.06250),
          (2.125, ql.Date(15, 5, 2025), 99.25),
          (2.25, ql.Date(15, 11, 2024), 100.546875),
          (2.25, ql.Date(15, 11, 2025), 100.375),
          (2.375, ql.Date(15, 8, 2024), 101.671875),
          (2.5, ql.Date(15, 8, 2023), 103.25),
          (2.5, ql.Date(15, 5, 2024), 102.796875),
          (2.75, ql.Date(15, 11, 2023), 105.0625),
          (2.75, ql.Date(15, 2, 2024), 104.875)
          ]
securities = []
min_basis = 100
min_basis_index = -1
for i, b in enumerate(basket):
    coupon, maturity, price = b
    issue = maturity - ql.Period(10, ql.Years)
    s = create_tsy_security(issue, maturity, coupon / 100.)
    bond_engine = ql.DiscountingBondEngine(yield_curve_handle)
    s.setPricingEngine(bond_engine)
    cf = ql.BondFunctions.cleanPrice(s, 0.06, day_count, ql.Compounded, ql.Semiannual, calc_date) / 100.
    adjusted_futures_price = futures_price * cf
    basis = price - adjusted_futures_price
    if basis < min_basis:
        min_basis = basis
        min_basis_index = i
    securities.append((s, cf))

ctd_info = basket[min_basis_index]
ctd_bond, ctd_cf = securities[min_basis_index]
ctd_price = ctd_info[2]
print("CTB Bond Measures")
print("%-30s = %lf" % ("Minimum Basis", min_basis))
print("%-30s = %lf" % ("Conversion Factor", ctd_cf))
print("%-30s = %lf" % ("Coupon", ctd_info[0]))
print("%-30s = %s" % ("Maturity", ctd_info[1]))
print("%-30s = %lf" % ("Price", ctd_info[2]))

#######################################################################
# basket describes the coupon rate, maturity date, price
#######################################################################
futures_maturity_date = ql.Date(21, 12, 2015)
futures = ql.FixedRateBondForward(calc_date, futures_maturity_date, ql.Position.Long, 0.0, settlement_days,
                                  day_count, calendar, bussiness_convention, ctd_bond, yield_curve_handle,
                                  yield_curve_handle)
model_futures_price = futures.cleanForwardPrice() / ctd_cf
implied_yield = futures.impliedYield(ctd_price / ctd_cf, futures_price, calc_date, ql.Compounded, day_count).rate()
z_spread = ql.BondFunctions.zSpread(ctd_bond, ctd_price, yield_curve, day_count, ql.Compounded, ql.Semiannual,
                                    calc_date)
ytm = ql.BondFunctions.bondYield(ctd_bond, ctd_price, day_count, ql.Compounded, ql.Semiannual, calc_date)
print("Bond Future Measures")
print("%-30s = %lf" % ("Model Futures Price", model_futures_price))
print("%-30s = %lf" % ("Market Futures Price", futures_price))
print("%-30s = %lf" % ("Model Adjustment", model_futures_price - futures_price))
print("%-30s = %2.3f%%" % ("Implied Yield", implied_yield * 100))
print("%-30s = %2.1fbps" % ("Forward Z-Spread", z_spread * 10000))
print("%-30s = %2.3f%%" % ("Forward YTM ", ytm * 100))
