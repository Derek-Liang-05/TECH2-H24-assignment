import numpy as npy



def std_loops(x):
    
    sum_list = 0 
    length = 0
    mean = 0
    mean_sqr = 0
    sum_sqr = 0
    variance = 0
    
    
    for i in x:
        sum_list += i
        sum_sqr += i**2
        length += 1

    mean = sum_list/length
    mean_sqr = sum_sqr/length

    variance = mean_sqr - mean**2
    return variance**0.5

def std_builtin(x):
    mean = sum(x)/len(x)
    

print(std_loops([1,2,3]))
