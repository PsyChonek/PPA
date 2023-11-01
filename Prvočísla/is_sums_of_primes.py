# Spočítá, zda je možné číslo předané v parametru vyjádřit jako součet dvou prvočísel a pokud ano,
#  vrátí větší (či roven) ze sčítanců, v opačném případě vrátí 0. Pokud existuje více řešení, funkce vrátí libovolné.
from is_prime import is_prime

def is_sums_of_primes(n: int):
    if (n > 2):
        for i in range(2, int(n/2)+1):
            if (is_prime(i) and is_prime(n-i)):
                return max(i, n-i)
        return 0
    else:
        return 0