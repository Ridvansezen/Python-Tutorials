""""Python da Generator kavramı."""

def sayilar():
    yield 1
    print("Birinci sayı")

    yield 2
    print("İkinci sayı")

    yield 3
    print("Üçüncü sayı")

custom_generator = sayilar()

for i in custom_generator:
    print(i)