def ascenselectionminmax(data) :
    print("Data Awal = ",data)
    start = 0
    n = len(data)
    while start < len(data)//2 :
        print("iterasi ke-",start+1)
        indek = start
        for j in range(start+1,len(data)) :
            if data[indek] > data[j] :
                indek = j
        data[start],data[indek]=data[indek],data[start]
        print("Urut data minimal  : ",data)
        indek = n - 1
        for k in range(n-2,start,-1) : 
            if data[indek] < data[k] :
                indek = k
        data[n-1],data[indek] = data[indek],data[n-1]
        n-=1
        start += 1
        print("Urut data maksimal : ",data)
    return data

print("Algoritma Modifikasi Selection Sort")
a = [10,2,5,8,1,20,7,12,4]
b = ascenselectionminmax(a)
print("Data Urut : ",b)