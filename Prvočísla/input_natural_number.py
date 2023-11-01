# Zadej celé číslo!
def input_natural_number():
    while True:
        try:
            num = int(input("Zadej celé číslo! \n"))
            if num <= 0:
                raise ValueError
            return num
        except ValueError:
            print("Neplatný vstup! Zadej celé číslo! \n")
