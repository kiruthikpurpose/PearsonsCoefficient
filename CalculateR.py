import math

x = list(map(int, input().split()))
y = list(map(int, input().split()))

sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum([x[i] * y[i] for i in range(len(x))])
sum_x2 = sum([i ** 2 for i in x])
sum_y2 = sum([i ** 2 for i in y])
n = len(x)

numerator = (n * sum_xy) - (sum_x * sum_y)
denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

if denominator != 0:
    r = numerator / denominator
else:
    r = 0

print(r)
