def bubble_gan_gen(data): #membuat fungsi untuk proses pengurutan ganjil genap. 
    cek = data.copy() #pada variabel cek ada .copy yang berguna untuk mengembalikkan objek pada parameter data.
    cek.sort()
    print('Data =',data,'\n')
    while data != cek:
        iterasi = 1
        batas = 0
        while iterasi < len(data)-1:
            for i in range(batas * 2 , (len(data) - (len(data)-((batas+1)*2))) ,1): #Penentu swap setiap iterasi dari index genap - ganjil [0-1]
                if i % 2 == 0 and i != len(data):
                    if data[i] > data[i+1]: #kondisi jika value indeks i > dari value indeks[i+1]
                        temp = data[i]
                        data[i] = data[i+1]
                        data[i+1] = temp
                        batas += 1
                    else:
                        batas += 1
            iterasi += 1
        print('Genap - Ganjil Sorting :\n{}\n'.format(data))
    
        iterasi2 = 1
        batas1 = 0
        while (iterasi2 < len(data)-1):
            for j in range((batas1 * 2)+1 , (len(data) - (len(data)-( ( (batas1+1) *2) +1))) ,1) : #Ganjil Genap[1-2]
                if j % 2 == 1 and j != len(data)-1:
                    if data[j] > data[j+1]:
                        temp = data[j]
                        data[j] = data[j+1]
                        data[j+1] = temp
                        batas1 += 1
                    else:
                        batas1 += 1
            iterasi2 += 1
        print('Ganjil - Genap Sorting :\n{}\n'.format(data))

array = [13,12,10,8,7,5,11,2]
bubble_gan_gen(array)