kilowattHours = int(input("Enter the KW hours used: "))

rate1 = 7.633
rate2 = 9.259

if kilowattHours <= 1000:
    totalCents = kilowattHours * rate1
else:
    firstCost = 1000 * rate1
    extraCost = (kilowattHours - 1000) * rate2
    totalCents = firstCost + extraCost

totalDollars = totalCents / 100

print("Amount owed is $%.2f" % totalDollars)