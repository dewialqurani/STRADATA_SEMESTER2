arr = [13, 12, 10, 8, 7, 5, 11,2]
n = len(arr)
kondisi = True
counter = 0
print(arr)
while kondisi:
    kondisi = False
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            kondisi = True
    if kondisi:
        if counter % 2 == 0:
            print("Genap-Ganjil")
            for i in range(0,n-1,2):
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
            print(arr)
        else:
            print("Ganjil-Genap")
            for i in range(1,n-1,2):
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
            print(arr)
    counter+=1