print('===== MODUL 1 - DICTIONARIES =====')
print('===== Struktur Data - 24 Maret 2021 =====')

def createSparseMatrix(): 
    chek = 0
    baris = int(input('Jumlah baris  =  '))
    kolom = int(input('Jumlah kolom  =  '))
    data = int(input('Jumlah data   =  '))
    sparMatr = {'baris' : baris, 'kolom' : kolom }
    while chek != data :  
        line =int(input(' Baris ke     ?  '))
        colom =int(input(' Kolom ke     ?  '))
        ordo = "matrik [ "+str(line)+','+str(colom)+" ]=  "
        sparMatr[line ,colom]=int(input(ordo))
        chek += 1
    return sparMatr

def dispSparseMatrix2D(Matrix):
    baris=Matrix['baris']
    kolom=Matrix['kolom']
    temp1=''
    for x in range(baris):
        temp=''
        for y in range(kolom):
            if Matrix.get((x,y))!=None:
                temp="%s%4d%2s"%(temp,Matrix[x,y],' ')
            else:
                temp="%s%4d%2s"%(temp,0,' ')
        temp1='%s|%s|\n'%(temp1,temp)
    return temp1

print('Matrik - 1 ')
matrix1 = createSparseMatrix()
print(matrix1)
print(dispSparseMatrix2D(matrix1))
print('Matrik - 2 ')
matrix2 = createSparseMatrix()
print(matrix2)
print(dispSparseMatrix2D(matrix2))

def multSparseMatrix2D(data1,data2):
    numOfRows1 = data1["baris"]
    numOfCols1 = data1["kolom"]
    numOfRows2 = data2["baris"]
    numOfCols2 = data2["kolom"]
    hasil={}
    matrix1={}
    matrix2={}
    hasil["baris"] = numOfRows1
    hasil["kolom"] = numOfCols2
    if numOfCols1!=numOfRows2:
        return False
    else:
        for x in range(numOfRows1):
            for z in range(numOfCols2):
                temp=0
                for y in range(numOfCols1):
                    if data1.get((x,y))==None:
                        matrix1[x,y]=0
                    else:
                        matrix1[x,y]=data1.get((x,y))
                    if data2.get((y,z))==None:
                        matrix2[y,z]=0
                    else:
                        matrix2[y,z]=data2.get((y,z))
                    temp+=(matrix1[x,y]*matrix2[y,z])
                hasil[x,z]=temp
        return hasil


print('Matriks 1 = ') 
print(dispSparseMatrix2D(matrix1))
print('Matriks 2 = ')
print(dispSparseMatrix2D(matrix2))
hasilKali=multSparseMatrix2D(matrix1,matrix2)
if hasilKali==False:
    print('Ukuran Tidak Memenuhi Syarat')
else:
    print('Hasil = ')
    print(dispSparseMatrix2D(hasilKali))