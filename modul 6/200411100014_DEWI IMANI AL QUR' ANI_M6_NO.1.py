def seqSearch(listData, data):
    hasil1=[]
    ind = 0
    found = False
    count=0
    for i in listData:
        if i == data:
            found=True
            hasil1.append(ind)
            ind += 1
        else:
            ind = ind+1
        count+=1
    if found==True:
        return(hasil1,count)
    else:
        return('Data Tidak Ada',count)

a=[3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
[hasil,jumlahIterasi]=seqSearch(a,16)
print('Posisi Data = ',hasil)
print('Jumlah Iterasi = ',jumlahIterasi)