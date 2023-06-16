import time


def print_prime_default(limit):
    time_1 = time.time()
    prime_list = [2]
    for i in range(limit - 2):
        number = i + 3
        is_prime = True
        for p in prime_list:
            if p * p > number:
                break
            if (number % p) == 0:
                is_prime = False
        if is_prime:
            prime_list.append(number)
    print(prime_list)
    time_2 = time.time()
    print(time_2 - time_1)
    len(prime_list)


def print_prime_contradict(limit):
    time_1 = time.time()
    prime_list = []
    for num in range(limit):
        prime_list.append(num + 1)
    prime_list.remove(1)
    for p in prime_list:
        if p * p > limit:
            break
        for i in range(p, limit // p + 1):
            if i * p in prime_list:
                prime_list.remove(i * p)
    print(prime_list)
    time_2 = time.time()
    print(time_2 - time_1)


if __name__ == '__main__':
    print_prime_default(10)

