import QuantLib as ql
import math


def create_swaption_helpers(data, index, term_structure, engine):
    swaptions = []
    fixed_leg_tenor = ql.Period(1, ql.Years)
    fixed_leg_daycounter = ql.Actual360()
    floating_leg_daycounter = ql.Actual360()
    for d in data:
        vol_handle = ql.QuoteHandle(ql.SimpleQuote(d.volatility))
        helper = ql.SwaptionHelper(ql.Period(d.start, ql.Years),
                                   ql.Period(d.length, ql.Years),
                                   vol_handle,
                                   index,
                                   fixed_leg_tenor,
                                   fixed_leg_daycounter,
                                   floating_leg_daycounter,
                                   term_structure
                                   )
        helper.setPricingEngine(engine)
        swaptions.append(helper)
    return swaptions


def calibration_report(swaptions, data):
    print("-" * 82)
    print("%15s %15s %15s %15s %15s" % ("Model Price", "Market Price", "Implied Vol", "Market Vol", "Rel Error"))
    print("-" * 82)
    cum_err = 0.0
    for i, s in enumerate(swaptions):
        model_price = s.modelValue()
        market_vol = data[i].volatility
        black_price = s.blackPrice(market_vol)
        rel_error = model_price / black_price - 1.0
        implied_vol = s.impliedVolatility(model_price,
                                          1e-5, 50, 0.0, 0.50)
        rel_error2 = implied_vol / market_vol - 1.0
        cum_err += rel_error2 * rel_error2

        print("%15.5f %15.5f %15.5f %15.5f %15.5f" % (model_price, black_price, implied_vol, market_vol, rel_error))
    print("-" * 82)
    print("Cumulative Error : %15.5f" % math.sqrt(cum_err))

