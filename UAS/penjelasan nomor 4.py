#SOAL !
#1. Buatlah kode untuk menampilkan perubahan setiap iterasi dari proses pengurutan dengan quick sort 
#2. tambahkan kode untuk menghitung perbandingan dan pergeseran pada algoritma quick sort

#quick sort adalah salah satu algoritma pengurutan data yang palig cepat, yaitu dengan membagi list mengunakan sebuat pivot.
#data yang kurang dari pivot sudah ditentukan ditaruh disebelah kirinya pivot.
#data yang lebih besar dari pivot sudah ditentukan ditaruh disebelah kanannya pivot.

banding = 0
geser = 0
def partition(arr,p,q):
    global banding,geser
    pivot= arr[p]
    i = p

    for j in range(p+1,q+1):
        banding +=1
        if pivot >= arr[j]:
            geser +=1
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[p] = arr[p],arr[i]
    return i

def quicksort(arr,p,q):
    if p <q:
        r = partition(arr,p,q)
        quicksort(arr,p,r-1)
        quicksort(arr,r+1,q)

d=[7,9,2,3,5,1]
print('Data sebelum diurutkan : ',d)
quicksort(d,0,len(d)-1)
print('Banyaknya Pergeseran : ',geser)
print('Banyaknya Perbandingan : ',banding)
print('setelah diurutkan = ',d)

     