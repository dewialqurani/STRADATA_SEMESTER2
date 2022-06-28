def matrix():
    print('matrix 3*3')
    mat=[]
    for i in range(1,3+1):
        temp=[]
        for j in range(1,3+1):
            print('baris',i,'kolom',j,'=')
            angka=int(input())
            temp.append(angka)
        mat.append(temp)
    return mat
def kali(x,y):
    hasil=[]
    for a in range(3):
        temp=[]
        for b in range(3):
            p=x[a][0]*y[0][b]+x[a][1]*y[1][b]+x[a][2]*y[2][b]
            temp.append(p)
        hasil.append(temp)
    return hasil
def lookmatrix(matrixs):
    for i in range(len(matrixs)):
        print('|', end= '')
        for j in range(len(matrixs)):
            strmat=str(matrixs[i][j])
            print(str(matrixs[i][j]).center(3),end='')
        print('',end='')
        print('|')
        print('')

matriks1=matrix()
lookmatrix(matriks1)
matriks2=matrix()
lookmatrix(matriks2)
print(kali(matriks1,matriks2))

