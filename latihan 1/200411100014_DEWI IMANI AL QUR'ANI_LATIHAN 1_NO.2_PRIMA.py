angka=int(input('Masukkan Angka = '))
faktor=0
for pembagi in range (angka) :
    if angka%(pembagi+1) == 0 :
       faktor = faktor + 1
if faktor == 2 :
        print (angka,'Bilangan Prima ')
else :
        print (angka, 'Bukan Bilangan Prima')
