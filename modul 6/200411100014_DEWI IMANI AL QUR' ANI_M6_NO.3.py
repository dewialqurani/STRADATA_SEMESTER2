def binSearch(listData, data):
    first = 0
    last = len(listData) - 1
    found = ""
    iterasi = 0
    midpoint = int(len(listData)/2)

    while iterasi < int(len(listData)/2)+1:
        if listData[midpoint] < data:
            if data == listData[midpoint]:
                found += str(midpoint) 
            midpoint += 1
        else :
            if data == listData[midpoint]:
                found += str(midpoint)
            midpoint -= 1

        iterasi +=1
    if len(found)>0:
        return([",".join(found),iterasi])
    else:
        return(['Data Tidak ditemukan', iterasi])

a=[5,2,4,3,8,3,4,6]
[hasil,iterasi]=binSearch(a,4)
print('Posisi Data = ',hasil)
print('Jumlah Iterasi = ',iterasi)