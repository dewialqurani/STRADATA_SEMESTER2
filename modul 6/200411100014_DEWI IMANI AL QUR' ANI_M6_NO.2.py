def orderedSeqSch(a,key) :
    found = False
    count = False
    iterasi = 0
    hasil=[]
    for i in range(len(a)) :
        if a[i]==key :
            found =True
            hasil.append(i)
            iterasi+=1
        elif a[i] <= key :
            iterasi+=1
        else :
            count =True
    iterasi+=1
    if found :
        return(hasil,iterasi)
    else :
        return ('Data Tidak Ada',iterasi)
a=[1,1,5,5,5,8,9,10,12,26]
[hasil,iterasi]=orderedSeqSch(a,9)
print('Posisi Data = ',hasil)
print('Jumlah Iterasi = ',iterasi)