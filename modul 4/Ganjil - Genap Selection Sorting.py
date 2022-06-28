def selection_sort(data):
    iterasi = 0
    block = data.copy()
    block.sort()
    print("Data : {}\n".format(data))
    while data != block:
        lock = data[iterasi] #Mengunci setiap index += 1
        set_low = max(data) #reset ke nilai terbesar setiap iterasi
        print("Iterasi ke-{}".format(iterasi+1))
        for b in range(len(data)-1,iterasi,-1): #mencari data terkecil dari rear ke front
            if data[b] <= set_low:
                set_low = data[b]
        iterasi += 1   
        #Deklarasi   
        idx_lock = data.index(lock)
        idx_low = data.index(set_low)
        #Swapping
        if lock > set_low:
            temp = data[idx_lock]
            data[idx_lock] = data[idx_low]
            data[idx_low] = temp
        #output
        if lock % 2 == 0 and set_low % 2 == 1 :
            print("Genap - Ganjil : {}\n".format(data))
        else:
            print("Ganjil - Genap : {}\n".format(data))
    
array = [13,12,10,8,7,5,11,2]
selection_sort(array)