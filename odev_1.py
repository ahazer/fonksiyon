def mukemmel(sayı):
    toplam = 0
    for i in range(1, sayı):
        if (sayı % i == 0):
            toplam += i
    return toplam == sayı

for i in range (1, 10000):
    if (mukemmel(i)):
        print("Mükemme Sayı:", i)