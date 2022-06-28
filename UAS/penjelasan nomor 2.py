#SOAL !
#1. Buatlah kode program untuk menampilkan perubahan setiap iterasi dari proses pengurutan dengan counting sort
#2. Tambahkan kode program untuk menghitung banyaknya perbandingan dan pergeseran pada algoritma counting sort

#Counting sort melakukan pengurutan tanpa melakukan pembandingan antar data. Syarat agar pengurutan ini dapat dilakukan adalah 
# diketahui rentang nilai data - datanya  yang akan diurutkan juga harus berupa bilangan bulat(integer).
#counting sort bisa efisien bila k tidak jauh lebih besar daripada n. dimana semakin besar k maka 
# memori tambahan yang diperlukan menjadi sangat besar.

def countingSort(listdata,k):
    D = []
    E = []

    for i in range(k+1):
        D.append(0)

    for j in range(len(listdata)):
        D[listdata[j]] = D[listdata[j]] + 1 
        E.append(0)

    for x in range(1,k+1):
        D[x] = D[x] + D[x-1]

    g = 1

    for j in range(len(listdata)-1,-1,-1):
        E[D[listdata[j]]-1] = listdata[j]
        print('Pada Iterasi ke - {} \n pada E[{}] akan digantikan dengan {} \n jadi data akan menghasilkan data baru : {} \n'.format(g,D[listdata[j]]-1,listdata[j],E))
        D[listdata[j]] = D[listdata[j]] -1

        g += 1

    return E

alist = [81,5,7,2]
print(countingSort(alist,max(alist)))

