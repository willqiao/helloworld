# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    firstmax = 0
    secondmax = 0
    for num in numbers:
        if num > firstmax:
            secondmax = firstmax
            firstmax = num
            continue
        
        if num <= firstmax and num > secondmax:
            secondmax = num
            continue

    return secondmax * firstmax


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
#     print(max_pairwise_product([3,2,1]))