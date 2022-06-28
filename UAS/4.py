#1. Buatlah kode untuk menampilkan perubahan setiap iterasi dari proses pengurutan dengan quick sort 
#2. tambahkan kode untuk menghitung perbandingan dan pergeseran pada algoritma quick sort

banding = 0
geser = 0
def partition(arr,p,q):
    global banding,geser
    pivot = arr[p]
    i = p
    for j in range(p+1,q+1):
        banding += 1
        if pivot >= arr[j]:
            geser += 1
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[p] = arr[p],arr[i]
    return i

def Quicksort(arr,p,q):
    if p < q:
        r = partition(arr,p,q)
        Quicksort(arr, p, r-1)
        Quicksort(arr, r+1, q)

d=[9,5,2,3,7,3,4,6,1]
print("Sebelum di urutkan : ",d)
Quicksort(d,0,len(d)-1)
print('Banyak Pergeseran : ',geser)
print('Banyak Perbandingan : ',banding)
print('Setelah di urutkan : ',d)