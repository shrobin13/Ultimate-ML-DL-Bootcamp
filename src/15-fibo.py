def fibo(n):
    curr = 0
    next = 1
    for i in range(n):
        temp = next
        next = curr + next
        curr = temp

    return curr


print(f"Fibo of 10th position: {fibo(10)}")

# pythonic way
# curr, next = 0, 1
# for _ in range(n):
# curr, next = next, curr + next
# return curr
