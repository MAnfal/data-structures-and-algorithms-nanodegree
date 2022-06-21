def prod(a, b):
    return a * b


def fact_gen():
    i = 1
    n = i
    while True:
        n = prod(n, i)
        i += 1
        yield n


my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120


