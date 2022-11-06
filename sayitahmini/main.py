from random import randint
rand = randint(1, 55)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 55 arasında değer girin (0 çikiş):"))
    if(sayi ==0):
        print("oyunu iptal ediniz")
        break
    elif sayi < rand:
        print("Daha yüksek bir sayi giriniz.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastgele seçilen sayi {0}!" .format(rand))
        print("Tahmin sayiniz {0}".format(sayac))
