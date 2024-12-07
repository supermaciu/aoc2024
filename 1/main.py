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
r = 0
count = 0
for i in range(len(n1)):
    if not (i-1 >= 0 and n1[i-1] == n1[i]):
        count = 0
        for j in range(len(n2)):
            if n1[i] == n2[j]:
                count += 1
            elif n1[i] != n2[j] and count != 0:
                break
    
    r += n1[i] * count

print(r)
