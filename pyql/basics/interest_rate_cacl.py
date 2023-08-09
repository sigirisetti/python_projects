import QuantLib as ql


annualRate = 0.05
dayCount = ql.ActualActual(ql.ActualActual.ISMA)
compoundType = ql.Compounded
frequency = ql.Annual
interestRate = ql.InterestRate(annualRate, dayCount, compoundType, frequency)


print(interestRate.compoundFactor(2.0))
print((1.0 + annualRate)*(1.0 + annualRate))
print(interestRate.discountFactor(2.0))
print(1.0 / interestRate.compoundFactor(2.0))


newFrequency = ql.Semiannual
effectiveRate = interestRate.equivalentRate(compoundType, newFrequency, 1)
print(effectiveRate.rate())


print(interestRate.discountFactor(1.0))
print(effectiveRate.discountFactor(1.0))