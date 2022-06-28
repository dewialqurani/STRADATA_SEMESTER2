import moduldewi as sm
#main program
print('Matrik - 1 ')
matrix1 = sm.createSparseMatrix()
print(matrix1)
print(sm.dispSparseMatrix2D(matrix1))
print('Matrik - 2 ')
matrix2 = sm.createSparseMatrix()
print(matrix2)
print(sm.dispSparseMatrix2D(matrix2))

print('Perkalian Matrik')
print('Matriks 1 = ') 
print(sm.dispSparseMatrix2D(matrix1))
print('Matriks 2 = ')
print(sm.dispSparseMatrix2D(matrix2))
hasilx=sm.multSparseMatrix2D(matrix1,matrix2)
if hasilx==False:
    print('Ukuran Tidak Memenuhi Syarat')
else:
    print('Hasil = ')
    print(sm.dispSparseMatrix2D(hasilx))  