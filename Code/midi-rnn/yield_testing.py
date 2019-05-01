import os, glob, random
import numpy as np
from multiprocessing import Pool as ThreadPool

# generator
def get_generator():
    index = 0
    while True:
        yield index
        index += 1 

if __name__ == '__main__':
    generator = get_generator()
    while True:
        user_input = input('Input? ')
        if user_input == 'y':
            # x = generator
            print(generator) 
        if user_input == 'exit':
            break 
