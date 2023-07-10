import numpy as np
import random as random


def make_new_die():
    die = [1,2,3,4,5,6]
    while sorted(die) == [1,2,3,4,5,6]:
        die = [random.randint(1,8) for i in range(6)]
    return die



def return_all_sums(d1, d2):
    output = []
    for x in d1:
        for y in d2:
            output.append(x+y)
    return output


if __name__ == '__main__':
    
    d = [1,2,3,4,5,6]

    normal_sums = return_all_sums(d,d)
    match_sum = False
    
    count = 0
    while not match_sum:

        d1 = make_new_die()
        d2 = make_new_die()
        new_sums = return_all_sums(d1,d2)

        match_sum = sorted(normal_sums) == sorted(new_sums)
        print('take', count)
        print('tried', sorted(d1), sorted(d2))
        count += 1
        

    print('these 2 dice worked!')
    print(sorted(d1))
    print(sorted(d2))