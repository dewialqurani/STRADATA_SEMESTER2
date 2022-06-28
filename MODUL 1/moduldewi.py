print('===== MODUL 1 - DICTIONARIES =====')
print('===== Struktur Data - 24 Maret 2021 =====')

def createSparseMatrix(): #membuat sparse matrix 
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

def dispSparseMatrix2D(Matrix): #untuk menampilkan matrix
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


def multSparseMatrix2D(data1,data2): #perkalian matrix
    numBaris = data1["baris"]
    numKolom = data1["kolom"]
    numBaris1 = data2["baris"]
    numKolom1 = data2["kolom"]
    hasil={}
    matrix1={}
    matrix2={}
    hasil["baris"] = numBaris
    hasil["kolom"] = numKolom1
    if numKolom!=numBaris1:
        return False
    else:
        for x in range(numBaris):
            for z in range(numKolom1):
                temp=0
                for y in range(numKolom):
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