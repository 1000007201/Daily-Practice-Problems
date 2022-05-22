# DESC --> returns max sum of subarray from given array

a = [1, 3, -5, 9, 1]
# a = [1, 2, -4, 1, 2, 3, -9]
sum = 0
max = 0

for i in a:
    if i > max:
        sum = i
        max = sum
    elif i < sum and (sum + i) < sum:
        max = sum
        sum = 0
    else:
        sum += i
        max = sum
print(max)
