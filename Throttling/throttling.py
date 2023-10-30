"""Python da Throttling kavramı."""

from time import sleep

print("\n")

def yazi(string):
    sleep(0.2)
    print(string)

max_giris = 5
yapilan_giris = 0

while True:
    a = yazi("Merhaba")
    yapilan_giris +=1

    if yapilan_giris >= max_giris:
        print("Erişim engellendi!", "Çok fazla giriş yaptınız.\n")
        break