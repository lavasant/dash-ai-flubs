import re

infile = open("./csv/Charlotin-hallucination_cases.csv", "r")
outfile = open("./csv/monthlytotals.csv", "w")

for line in infile:
    linecontentsarray = line.split(',')
    for str in linecontentsarray:
        if str[0:4] == "2023" or str[0:4] == "2024" or str[0:4] == "2025":
            print(f"{str[5:7]}-{str[0:4]}", file=outfile)

infile.close()
outfile.close()
