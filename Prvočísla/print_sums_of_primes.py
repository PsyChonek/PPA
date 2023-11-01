from is_prime import is_prime


def print_sums_of_primes(num: int,n: int):
    for i in range(2, int(num/2)+1):
        if (is_prime(i) and is_prime(num-i)):
            print("Lze rozlozit: ",i," + ",num-i)
            n -= 1
            if (n == 0):
                break
