# def fib(number):
#     numbers = [0,1]
#     for i in range(2,number):
#         numbers.append(numbers[-1] + numbers[-2])
#     return numbers[:number]

# print(fib(10))




def fib(numbers):
    seq = [0,1]
    for i in range(2, numbers):
        seq.append(seq[-2] + seq[-1])
    return seq

print(fib(10))

# with the fib, remember to have seq = [0,1]
# then the range is from 2 to numbers
# then append values using [-2] and [-1]

## remember:
# major thing: its -2 and -1 or else you'll just return 1s
# the question will ask to give you a list of length n, so if you don't specificy range (2, num) then you'll get too long of a list