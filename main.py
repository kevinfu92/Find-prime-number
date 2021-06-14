# Find all prime number in range

min_int = int(input('Lower range:\n'))
max_int= int(input('Upper range:\n'))
prime_list = []
if 2 in range(min_int, max_int):
    prime_list.append(2)
for i in range(min_int, max_int + 1):
    for j in range(2, i):
        if i % j == 0:
            break
        elif j == i - 1:
            prime_list.append(i)

print(prime_list)
