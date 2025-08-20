import re

infile = open("./csv/Charlotin-hallucination_cases.csv", "r")
outfile = open("./csv/monthlytotals.csv", "w")

#TODO: get month count dict to have format of "January 2023" instead of "01-2023"
monthnamesdict = {}

monthcountdict = {}

for line in infile:
    linecontentsarray = line.split(',')
    for str in linecontentsarray:
        year_str = str[0:4]
        if year_str == "2023" or year_str == "2024" or year_str == "2025":
            month_str = str[5:7]
            monthandyearstr = month_str + "-" + year_str

            print(f"{monthandyearstr}")

            if monthandyearstr in monthcountdict:
                monthcountdict[monthandyearstr] += 1
            else:
                monthcountdict[monthandyearstr] = 1

            print(f"{month_str}-{year_str}", file=outfile)

print(monthcountdict)

infile.close()
outfile.close()
