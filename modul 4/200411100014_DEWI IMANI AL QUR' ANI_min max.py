def selection_min_max(data) :
    print('Data Awal = ',data)
    temp = 0
    n = len(data)
    while temp < len(data)//2 :
        print('Iterasi ke - ',temp+1)
        indek = temp
        for j in range(temp+1,len(data)) :
            if data[indek] > data[j] :
                indek = j
        data[temp],data[indek]=data[indek],data[temp]
        print('Urut data minimal  : ',data)
        indek = n - 1
        for k in range(n-2,temp,-1) : 
            if data[indek] < data[k] :
                indek = k
        data[n-1],data[indek] = data[indek],data[n-1]
        n-=1
        temp += 1
        print('Urut data maksimal : ',data)
    return data

print('Algoritma Modifikasi Selection Sort')
array= [10,2,5,8,1,20,7,12,4]
y = selection_min_max(array)
print('Data Urut =  ',y)