#2. Buatlah fungsi binary search yang sudah dimodifikasi, sehingga dapat mencari data yang sama dan mengembalikan indeks-indeks dari data yang sama tersebut. Argument atau parameter pada fungsi tersebut berupa:
#a. data yang akan dicari
#b. list data dari data yang akan dicari
#Sedangkan return value dari fungsi ini berupa:
#a. indeks-indeks atau posisi dari data yang dicari pada list (jika data ditemukan), dan ‘Data tidak ada’ jika data tidak ditemukan.
#b. Jumlah iterasi yang diperlukan selama proses pencarian.

def binSearch(listData, data):
	first = 0
	last = len(listData) - 1
	found = ""
	iterasi = 0
	midpoint = int(len(listData)/2)
	while  iterasi < int(len(listData)/2)+1:
	       if listData[midpoint] < data:
	           			if data == listData[midpoint]:
	           				found += str(midpoint)
	           			midpoint += 1
	       else:
	           			if data == listData[midpoint]:
	           				found += str(midpoint)
	           			midpoint -= 1
	       iterasi +=1
	
	if len(found) > 0:
		return([','.join(found),iterasi])
	else:
	    return(['Data tidak ditemukan',iterasi])
	    
a=[1,1,5,5,5,8,9,10,12,26]
[hasil,iterasi]=binSearch(a,9)
print('Posisi Data = ',hasil)
print('Jumlah Iterasi = ',iterasi)