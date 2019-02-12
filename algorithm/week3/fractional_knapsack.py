# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    
    weightunit = zip(values, weights)
        
    weightunit = sorted(weightunit, key=lambda item: item[0]/item[1], reverse=True)
#     print(weightunit)
    index = 0
    totalvalue = 0.
    while capacity > 0 and index < len(values):
        weight = min(weightunit[index][1], capacity)
        capacity -= weight
        totalvalue += weight * weightunit[index][0]/weightunit[index][1]
        index+=1
    
    return totalvalue


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
#     data = [1,10,500,30,20,30]
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
