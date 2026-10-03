
import time
import os
import random

def loading():
    for i in range(23):
        print("-" * i)
        time.sleep(0.1)

    os.system('cls')

def times(x):
    for i in range(x):
        loading()

times(1000)