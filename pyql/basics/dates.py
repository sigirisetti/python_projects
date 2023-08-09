import QuantLib as ql

date = ql.Date(31, 3, 2015) # 31 March, 2015
print(date)

print(date.dayOfMonth())
print(date.month())
print(date.year())
print(date.weekday() == ql.Tuesday)

print(date + 1)
print(date - 1)
print(date + ql.Period(1, ql.Months))
print(date + ql.Period(1, ql.Weeks))
print(date + ql.Period(1, ql.Years))
print(ql.Date(31, 3, 2015) > ql.Date(1, 3, 2015))