# def debug_test():
#     for x in range(10):
#         if x == 8:
#             print('hello number 8')
#         print(x + 10)

# debug_test()


def add(a, b):
    return a + b

assert add(1, 2) == 3, 'Should add integers'
assert add(-1, 2) == 1, 'Should handle negative numbers'
assert add(1.1, 2.2) == 3.3, 'Should handle floating point'
