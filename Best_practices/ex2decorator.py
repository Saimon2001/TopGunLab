#ex2 Create a Python decorator called timer that measures the time taken to execute a function. 
# Use this decorator on a function that sorts a list of random numbers and prints the sorted list.
import time

def timer(func):
    def wrapper(*args):
        start_t = time.time()
        result = func(*args)
        end_t = time.time()
        exec_time = end_t - start_t
        
        return print(f"Execution time: {exec_time} seconds")
    return wrapper


def sort(lista:list):
    lista.sort()
    return print(lista)

sort = timer(sort)

sort([4,5,6,34,5,765456,546,53,543,675,2,45])