# number = 4
# 0, 1, 1, 2
num = 4
seq = [0, 1]
for i in range(2, num):
    seq.append(seq[-1] + seq[-2])
print(seq)