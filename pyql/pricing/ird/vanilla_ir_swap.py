import QuantLib as ql

calc_date = ql.Date(15, 1, 2015)
ql.Settings.instance().evaluationDate = calc_date

#################################
# Curves. discount and libor curve
#################################
risk_free_rate = 0.01
libor_rate = 0.02
day_count = ql.Actual365Fixed()

discount_curve = ql.YieldTermStructureHandle(ql.FlatForward(calc_date, risk_free_rate, day_count))
libor_curve = ql.YieldTermStructureHandle(ql.FlatForward(calc_date, libor_rate, day_count))

#libor3M_index = ql.Euribor3M(libor_curve)
libor3M_index = ql.USDLibor(ql.Period(3, ql.Months), libor_curve)

###########################
# Swap Leg Schedules
###########################
calendar = ql.UnitedStates(ql.UnitedStates.NYSE)
settle_date = calendar.advance(calc_date, 5, ql.Days)
maturity_date = calendar.advance(settle_date, 10, ql.Years)

fixed_leg_tenor = ql.Period(6, ql.Months)
fixed_schedule = ql.Schedule(settle_date, maturity_date,
                             fixed_leg_tenor, calendar,
                             ql.ModifiedFollowing, ql.ModifiedFollowing,
                             ql.DateGeneration.Forward, False)

float_leg_tenor = ql.Period(3, ql.Months)
float_schedule = ql.Schedule (settle_date, maturity_date,
                              float_leg_tenor, calendar,
                              ql.ModifiedFollowing, ql.ModifiedFollowing,
                              ql.DateGeneration.Forward, False)

######################################
# Construct Vanilla IR Swap Instrument
######################################
notional = 10000000
fixed_rate = 0.025
fixed_leg_daycount = ql.Actual360()
float_spread = 0.004
float_leg_daycount = ql.Actual360()

ir_swap = ql.VanillaSwap(ql.VanillaSwap.Payer, notional,
                         fixed_schedule, fixed_rate, fixed_leg_daycount,
                         float_schedule, libor3M_index, float_spread, float_leg_daycount )


######################################
# Set Pricing Engine to Swap Instrument
######################################
swap_engine = ql.DiscountingSwapEngine(discount_curve)
ir_swap.setPricingEngine(swap_engine)

######################################
# Print swap cashflows
######################################
for i, cf in enumerate(ir_swap.leg(0)):
    print("%2d %-18s %10.2f"%(i+1, cf.date(), cf.amount()))

for i, cf in enumerate(ir_swap.leg(1)):
    print("%2d %-18s %10.2f"%(i+1, cf.date(), cf.amount()))

print("%-20s: %20.3f" % ("Net present Value", ir_swap.NPV()))
print("%-20s: %20.3f" % ("Fair Spread", ir_swap.fairSpread()))
print("%-20s: %20.3f" % ("Fair Rate", ir_swap.fairRate()))
print("%-20s: %20.3f" % ("Fixed Leg BPS", ir_swap.fixedLegBPS()))
print("%-20s: %20.3f" % ("Float Leg BPS", ir_swap.floatingLegBPS()))