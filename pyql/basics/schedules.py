import QuantLib as ql

date1 = ql.Date(1, 1, 2015)
date2 = ql.Date(1, 1, 2016)
tenor = ql.Period(ql.Monthly)
calendar = ql.UnitedStates(ql.UnitedStates.NYSE)
schedule = ql.Schedule(date1, date2, tenor, calendar, ql.Following,
                           ql.Following, ql.DateGeneration.Forward, False)
print(list(schedule))