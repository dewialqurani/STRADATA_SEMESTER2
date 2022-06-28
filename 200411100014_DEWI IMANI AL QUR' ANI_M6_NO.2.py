def orderedSeqSch(a,key) :
    found = False
    stop = False
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
            stop =True
    iterasi+=1
    if found :
        return hasil,iterasi
    else :
        return "data tidak ada",iterasi
a=[1,1,5,5,5,8,9,10,12,26]
[hasil,iterasi]=orderedSeqSch(a,5)
print('Posisi Data = ',hasil)
print('Jumlah Iterasi = ',iterasi)