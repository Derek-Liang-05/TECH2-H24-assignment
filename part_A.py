import numpy as npy



def std_loops(x):
    
    sum_list = 0 
    length = 0
    sum_sqr = 0

    for i in x:
        sum_list += i
        sum_sqr += i**2
        length += 1

    variance = (sum_sqr/length) - (sum_list/length) ** 2
    return variance ** 0.5

def std_builtin(x):
    
    x_sqr = []
    x_sqr = [i ** 2 for i in x]

    variance =  (sum(x_sqr)/len(x_sqr)) - (sum(x)/len(x)) ** 2

    return variance ** 0.5



print(std_loops([1,2,3]))
print(std_builtin([1,2,3]))
