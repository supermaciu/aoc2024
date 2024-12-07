reports = []
with open("data.txt", "r") as f:
    line = f.readline()
    while line != "":
        reports.append([int(x) for x in line.split()])

        line = f.readline()


safe_reports = 0
for report in reports:
    safe = True
    removed = False
    last = report[0] - report[1]
    for i in range(len(report)-1):
        d = report[i] - report[i+1]
        if not (d != 0 and d/abs(d) == last/abs(last) and abs(d) >= 1 and abs(d) <= 3):
            if removed:
                safe = False
                last = d
                break
            else:
                removed = True

    print(report, safe)

    safe_reports += 1 if safe else 0

print(safe_reports)