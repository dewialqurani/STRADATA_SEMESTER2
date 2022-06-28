# Merge Sort  
perbandingan = 0
pergeseran = 0
def mergeSort(arr):
    global perbandingan,pergeseran
    if len(arr) > 1:
        print('Pemisahan ',arr,' = ',end='')
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        print(left,',',right)

        mergeSort(left)
        mergeSort(right)
        i,j,k = 0,0,0

        print('Merging ',left,' and ',right,' = ',end='')

        while i < len(left) and j < len(right):
            perbandingan += 1 
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                pergeseran += 1
            else:
                arr[k] = right[j]
                j += 1
                pergeseran += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            pergeseran += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            pergeseran += 1
        print(arr,'\n')
    else:
        print('Tidak Ada Pemisahan ',arr)

a = [5,7,8,6,3]
print('Sebelum di urutkan = ',a)
mergeSort(a)

# Pergeseran dilihat dari data yang perbandingannya true
print('Banyak Pergeseran = ',pergeseran)

# Pergeseran dilihat dari banyaknya perbandingan data
print('Banyak Perbandingan = ',perbandingan)
print('Sesudah di urutkan = ',a)



#  QUICK SORT
iteration = 1
perbandingan = 0
pergeseran = 0
def partition(arr,p,q):
    global iteration,perbandingan,pergeseran
    pivot = arr[p]
    i = p
    print('Iterasi Ke - ',iteration)
    print('Pivot = ',pivot)
    for j in range(p+1,q+1):
        perbandingan += 1
        print(f'Pivot -----> {arr[j]} ? {pivot >= arr[j]}',end='')
        if pivot >= arr[j]:
            pergeseran += 1
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        print(f', \tData = {arr}')
    arr[i],arr[p] = arr[p],arr[i]
    print('Data Akhir = ',arr)
    iteration += 1
    return i

def Quicksort(arr,p,q):
    if p < q:
        r = partition(arr,p,q)
        Quicksort(arr, p, r-1)
        Quicksort(arr, r+1, q)

a=[8,78,18,28,48,38,68,88,58]
print('Sebelum di urutkan = ',a)
Quicksort(a,0,len(a)-1)

# Pergeseran dilihat dari data yang perbandingannya true
print('Banyak Pergeseran = ',pergeseran)

# Pergeseran dilihat dari banyaknya perbandingan data
print('Banyak Perbandingan = ',perbandingan)
print('Setelah di urutkan =  ',a)