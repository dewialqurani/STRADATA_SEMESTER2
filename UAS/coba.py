def binarySearch(list_data, key):
    awal = 0
    akhir = len(list_data)-1
    temp = []
    iterasi = 0
    active = True
    while awal <= akhir and active:
        mid = awal + (akhir - awal) // 2
        
        if list_data[mid] == key:
            temp.append(mid)
            active = False
 
        elif list_data[mid] < key:
            awal = mid + 1
 
        else:
            akhir = mid - 1
        print(iterasi, list_data[mid], key)
        iterasi += 1
    
    
    if temp != [] :
        return ",".join(['{} is in : {}'.format(key,temp),' numberOfIteration: {}'.format(iterasi)])
    else:
        return ",".join(['{} is not found'.format(key),' numberOfIteration: {}'.format(iterasi)])

a=[1,1,5,5,5,8,9,10,12,26]
print("Data = ", a, "\n")
print(binarySearch(a,1))
print(binarySearch(a,18))
print(binarySearch(a,188))
print(binarySearch(a,1242))