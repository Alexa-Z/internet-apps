import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

#print(list(gen_random(5, 1, 3)))
