def bolenleri_bul(sayı):
    bolen_listesi = []

    for i in range(1, sayı+1):

        if (sayı % i == 0):
            bolen_listesi.append(i)
    return bolen_listesi

while True:

    sayı = input("Sayı:")

    if (sayı == "q"):
        print("Program sonlandırılıyor")
        break
    else:
        sayı = int(sayı)
        print("Tam Bölenler:", bolenleri_bul(sayı))
