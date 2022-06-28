def createSparseMatrix(baris,kolom) :
    data = {}
    data["baris"] = baris
    data["kolom"] = kolom
    sparse = int(input("jumlah data = "))
    if sparse <= (baris*kolom) and sparse > 0:
        i = 1
        while i <= sparse :
            iBaris = int(input("Baris ke - "))
            iKolom = int(input("Kolom ke - "))
            if iBaris < baris and iKolom < kolom and iBaris >= 0 and iKolom >= 0:
                nilai = int(input("Matrik[{},{}]= ".format(iBaris,iKolom)))
                data[iBaris,iKolom] = nilai
                i += 1
            else :
                print("ukuran tidak sama")
    else :
        print("ukuran tidak sama")
    return data


def displaySparseMatrix(data):
    jumlahBaris= data["baris"]
    jumlahKolom= data["kolom"]
    matStr=''
    for i in range(jumlahBaris):
        temp=''
        for j in range(jumlahKolom):
            if (i,j) in data :
                temp=temp+' '+str('%4d'%data[(i,j)])
            else :
                temp=temp+' '+str('%4d'%0)

        temp='%4s'%'|'+temp+'%4s'%'|'
        matStr=matStr+temp+'\n'
    return (matStr)

def multSparseMatrix(data1, data2) :
    baris1 = data1["baris"]
    kolom1 = data1["kolom"]
    baris2 = data2["baris"]
    kolom2 = data2["kolom"]
    multHasil = {}
    mat1 = {}
    mat2 = {}
    for i in range(baris1) :
        for y in range(kolom1) :
            if (i,y) in data1 :
                nilai1 = data1[(i,y)]
                mat1[(i,y)] = nilai1
            else :
                mat1[(i,y)] = 0

    for i in range(baris2) :
        for y in range(kolom2) :
            if (i,y) in data2 :
                nilai2 = data2[(i,y)]
                mat2[(i,y)] = nilai2
            else :
                mat2[(i,y)] = 0
    if kolom1 == baris2 :
        multHasil["baris"] = baris1
        multHasil["kolom"] = kolom2
        for i in range(baris1):
            for k in range(kolom2):
                temp=0
                for j in range(kolom1): 
                    temp=temp+mat1[(i,j)]*mat2[(j,k)]
                multHasil[(i,k)] = temp
        return multHasil
    else :
        return False