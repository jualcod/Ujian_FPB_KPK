bil1 = int(input('Ketik angka pertama   :'))
bil2 = int(input('Ketik angka kedua     :'))

def fpb(bil1,bil2):
    while 1:
        sisa = bil1 % bil2
        if sisa == 0:
            break
        bil1, bil2 = bil2, sisa
    return bil2
print('FPB dari', bil1, 'dan', bil2, 'adalah =', fpb(bil1,bil2))

def kpk(bil1,bil2):
    perkali1 = 1
    perkali2 = 1
    p = bil1 * perkali1
    q = bil2 * perkali2
    while p != q:
        while p > q:
            perkali2 += 1
            q = bil2 * perkali2
        while p < q:
            perkali1 += 1
            p = bil1 * perkali1
    if p == q:
        return p
print('KPK dari', bil1, 'dan', bil2, 'adalah =', kpk(bil1,bil2))