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
    i = 0; j = 1
    last = report[j] - report[i]
    if not (abs(last) >= 1 and abs(last) <= 3):
        removed = True
        d20 = report[2] - report[0]
        d21 = report[2] - report[1]
        if abs(d20) >= 1 and abs(d20) <= 3:
            j = 2
        elif abs(d21) >= 1 and abs(d21) <= 3:
            i = 1
            j = 2
        else:
            safe = False
        last = report[j] - report[i]

    while i in range(len(report)-1) and j in range(1, len(report)) and safe:
        d = report[j] - report[i]

        if not (abs(d) >= 1 and abs(d) <= 3 and d/abs(d) == last/abs(last)):
            if not removed:
                removed = True
                j += 1
                continue
            else:
                safe = False
                break
        
        last = d if d != 0 else last
        i += 2 if j-i == 2 else 1
        j += 1

    print(report, safe)
    safe_reports += 1 if safe else 0

print(safe_reports)