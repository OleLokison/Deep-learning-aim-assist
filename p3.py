import pickle
from matplotlib import pyplot as plt
import random
a = (1, 2)


try:
    a = random.randrange(0, 0)
except ValueError:
    print("hey")
    a = random.randrange(0, 10)
print(a)