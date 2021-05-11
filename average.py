lines = open("run.log", "r").readlines()
lines2 = open("run2.log", "r").readlines()
amount = 0
count = 0
for i in range(200):
    first = int(lines2[i].replace("\n", ""), 16)
    second = int(float(lines[i].replace("\n", "")))
    amount += (first - second)
    count += 1

print(amount / count)
