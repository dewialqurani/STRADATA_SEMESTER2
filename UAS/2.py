#1. Buatlah kode program untuk menampilkan perubahan setiap iterasi dari proses pengurutan dengan counting sort
#2. Tambahkan kode program untuk menghitung banyaknya perbandingan dan pergeseran pada algoritma counting sort

def countingSort(list_data,k): 
    D = [] 
    E = [] 
    
    for i in range(k+1): 
        D.append(0)     
    
    for j in range(len(list_data)): 
        D[list_data[j]] = D[list_data[j]]+1 
        E.append(0)
    
    for x in range(1,k+1) :
        D[x] = D[x]+D[x-1] 
    
    g = 1
    for j in range(len(list_data)-1,-1,-1): 
        E[D[list_data[j]]-1] = list_data[j] 
        print('Pada Iterasi ke-{} \npada B[{}] akan di replace dengan {} \nsehingga data akan menghasilkan data terbaru : {}\n'.format(g,D[list_data[j]]-1,list_data[j],E))
        D[list_data[j]] = D[list_data[j]]-1 
        g += 1

    return(E)

a_list = [18,81,99,91,7,8,3,5,2]
print(countingSort(a_list,max(a_list)))