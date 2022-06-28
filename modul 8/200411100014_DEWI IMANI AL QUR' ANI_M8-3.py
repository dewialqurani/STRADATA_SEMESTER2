def Ascending(arr,p,q):
    pivot = arr[p]
    i = p
    for j in range(p+1,q+1):
        if pivot <= arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[p] = arr[p],arr[i]
    return i

def Descending(arr,p,q):
    pivot = arr[p]
    i = p
    for j in range(p+1,q+1):
        if pivot <= arr[j]:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[p] = arr[p],arr[i]
    return i

def msAscending(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        msAscending(left)
        msAscending(right)
        i,j,k = 0,0,0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def msDescending(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        msDescending(left)
        msDescending(right)
        i,j,k = 0,0,0

        while i < len(left) and j < len(right):

            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

while True:
    print('Metode pengurutan yang dapat dipilih :  ')
    print('1. QuickSort')
    print('2. MergeSort')
    metode= int(input('Masukan pilihan  metode pengurutan yang Anda inginkan : '))

    print('Ada Pengurutan  secara urut Ascending atau Descending')
    print('1. Ascending')
    print('2. Descending')
    implen= int(input("Masukan pilihan pengurutan yang Anda inginkan : "))

    inp = input('Masukan beberapa angka yang Anda ingunkan, seperti (1,7,3,5,6,2) *tanpa tanda kurung : ')
    data = inp.split(",")
    data = [int(i) for i in data]

    if metode == 1:
        if implen == 1:
            def Quicksort(arr,p,q):
                if p < q:
                    r = Ascending(arr,p,q)
                    Quicksort(arr, p, r-1)
                    Quicksort(arr, r+1, q)
            Quicksort(data,0,len(data)-1)
        else:
            def Quicksort(arr,p,q):
                if p < q:
                    r = Descending(arr,p,q)
                    Quicksort(arr, p, r-1)
                    Quicksort(arr, r+1, q)
            Quicksort(data,0,len(data)-1)
    else:
        if node == 1:
            msAscending(data)
        else:
            msDescending(data)
    print('Hasil nya Adalah ',data)
    lanjut = input('Lagi[y/t]?  ')
    if lanjut == 't':
        print('Terimakasih Sukses Buat Kamu')
        break

