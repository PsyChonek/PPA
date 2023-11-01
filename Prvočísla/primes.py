# README
# V testu byly dvě chyby?, špatné od 

# Je číslo předané v parametru prvočíslo? Pokud ano, vrátí True, jinak False.
from input_natural_number import input_natural_number
from print_sums_of_primes import print_sums_of_primes
from is_sums_of_primes import is_sums_of_primes
from is_prime import is_prime
from is_sums_of_primes import is_sums_of_primes

# Hlavní funkce
def main():
    num = input_natural_number()  
    if is_sums_of_primes(int(num)):
        print_sums_of_primes(int(num), int(1))
    else:
        print("Nelze rozlozit.")


if __name__ == "__main__":
    main()