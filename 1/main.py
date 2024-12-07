n1 = []
n2 = []

with open("data.txt", "r") as f:
    line = f.readline()
    while line != "":
        a, b = (int(x) for x in line.split())
        n1.append(a)
        n2.append(b)

        line = f.readline()

n1.sort()
n2.sort()

diff_sum = 0
for i in range(len(n1)):
    diff_sum += abs(n1[i] - n2[i])

print(diff_sum)
