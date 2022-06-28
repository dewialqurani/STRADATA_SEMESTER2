def binSearch(listData, data):
    first = 0
    last = len(listData) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) //2
        if listData[midpoint] == data:  
            found = True   
        else:
            if data < listData[midpoint]:
                last = midpoint -1
            else :
                first = midpoint + 1
        
        return('Data Tidak Ada',found)

a=[1,1,5,5,5,8,9,10,12,26]
[hasil,iterasi]=binSearch(a,1)
print('Posisi Data = ',hasil)
print('Jumlah Iterasi = ',iterasi)