def selection_sort(data):
    iterasi = 0
    cek = data.copy()
    cek.sort()
    print("Data : {}\n".format(data))
    while data != cek:
        lock = data[iterasi] #Mengunci element pertama dan setiap iterasi += 1
        set_low = max(data) #reset ke nilai terbesar setiap iterasi
        for b in range(len(data)-1,iterasi,-1): #mencari data terkecil dari rear ke front
            if data[b] <= set_low:
                set_low = data[b]
        #Deklarasi   
        idx_lock = data.index(lock)
        idx_low = data.index(set_low)
        #Swapping
        if lock > set_low: #logika swapping 1
            temp = data[idx_lock]
            data[idx_lock] = data[idx_low]
            data[idx_low] = temp
            #output
            print("Nilain Min :",set_low)
            print("Minimal : {}\n".format(data))
        
        
        if data != cek : #Pengecekan ulang apakah data == cek 
            
            set_high = min(data) #reset ke nilai terkecil di setiap iterasi 
            lock2 = data[len(data)-(iterasi+1)] #Mengunci element kedua dan setiap iterasi -= 1
            for c in range(iterasi,len(data)-(iterasi+1),1): #mencari data terkecil dari front ke rear
                if data[c] >= set_high:
                    set_high = data[c]
            #Deklarasi
            idx_lock2 = data.index(lock2)
            idx_high = data.index(set_high)
            if lock2 < set_high:#logika swapping 2
                data[idx_lock2],data[idx_high] = data[idx_high],data[idx_lock2]
                #output
                print("Nilai Maksimal :",set_high)
                print("Maksimal : {}\n".format(data))
        iterasi += 1   
    
array = [10,2,5,8,1,20,7,12,4]
selection_sort(array)