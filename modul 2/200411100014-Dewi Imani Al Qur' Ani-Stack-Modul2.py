#fungsi-fungsi yang digunakan  untuk menerapkan fungsi stack
def stack() : #penambahan dan penghapusan data hanya dapat dilakukan satu ujung.
    s=[]
    return s
def push (s,data) : #push untuk penambahan data
    s.append(data)
    return s
def pop (s) :   #pop untuk menghapus data
    data = s.pop()
    return data
def peek(s) :   #peek informasi data yang terletak pada posisi top 
    return (s[len(s)-1])
def isEmpty(s) :    #isEmpty memeriksa apakah stack dalam keadaan kosong
    return(s==[])
def size (s) :  #jumlah data atau ukuran yang terdapat pada stack
    return(len(s))

def checkkurung (data) : #fungsi yang digunakan untuk mengecek kurung pada operasi aritmetika
    st = stack()
    data = data.replace(" ","") #berguna untuk saat inputakan string tidak usah memberikan spasi lagi.
    kurungbuka = "({["
    kurungtutup = ")}]"
    check = True #digunakan untuk perulangan.
    for i in data : #digunakan untuk perulangan yang jumlah perulangannya diketahui. 
        if i in kurungbuka : #jika ada tanda kurung buka maka akan di push
            push(st,i)
        elif i in kurungtutup :
            if not isEmpty(st) :
                if kurungbuka.index(peek(st)) == kurungtutup.index(i) : #jika kurung buka sama dengan kurung tutup, untuk memeriksa kurang tytyo dan kurung buka cocok atau tidak
                    pop(st)
                else :
                    return ("Kurung Buka dan Kurung  Tutup Tidak Cocok")
            else :
                return ("Jumlah Kurung Tutup Lebih Banyak")
    if not isEmpty(st) :
        return ("Jumlah Kurung Buka Lebih Banyak")

    return check

#fungsi konversi aritmetika infix ke aritmetika postfix
def infixtopostfix(data) :
    if checkkurung(data) is True : #apabila fungsi pertama bernilai benar maka def yang kedua akan dijalankan.
        st = stack()
        infix = data.replace(" ","") #berguna untuk saat inputakan string tidak usah memberikan spasi lagi.
        operator = { 
            "*" : 3,
            "/" : 3,
            "+" : 2,
            "-" : 2,
            "(" : 1,
            "{" : 1,
            "[" : 1
        }
        postfix = [] 
        num = "0123456789"
        kurungbuka = "({["
        kurungtutup = ")}]"
        for i in infix :
            if i in num :
                postfix.append(i)
            elif i in kurungbuka :
                push(st,i)
            elif i in kurungtutup :
                temp = pop(st)
                while temp != kurungbuka[kurungtutup.index(i)] : #jika kurung tutup tidak sama dengan kurung buka maka akan dimasukkan ke postfix
                    postfix.append(temp)
                    temp = pop(st)
            else :
                while not (isEmpty(st)) and operator[peek(st)] >= operator[i] :
                    postfix.append(pop(st))
                push(st,i)
        while not (isEmpty(st)) :
            postfix.append(pop(st))

        return True, "".join(postfix) #untuk menyatukan banyak string kedalam sebuah string.
    else :
        return False, checkkurung(data)

#fungsi untuk operasi
def operasi(data1,operator,data2) :
    c = str(data2) + operator + str(data1)
    return eval(c) #untuk mengoperasikan angka yang berbentuk string

#fungsi evaluasi postfix
def Evaluatepostfix(postfix): #fungsi untuk mengevaluasi angka string
    st = stack() 
    output ="" 
    operator = ['*','/','-','+']
    for i in postfix:
        if i in operator:
            total = operasi(pop(st),i,pop(st)) #digunakan untuk operator yang berbentuk postfix
            push(st,total)
        else:
            push(st,i) #operatornya dimasukkan ke stack
    while not isEmpty(st) : #untuk mengecek di st it kosong atau tidak
        output = str(pop(st)) + output
    return output
start = True #untuk main program
while start :
    inp = str(input("Masukkan String Operasi Aritmatika   =    "))
    a,b = infixtopostfix(inp) #a cek  b postfix
    if a is True :
        print("Infix :   ",inp,"   ;   " , "Postfix :     ",b,"  =  ",Evaluatepostfix(b)) #rvav hasil
    else :
        print(b)
    ulang = input("lngin Melanjutkan Operasi Aritmetika Selanjutnya ? (Ya/Tidak) : ")
    if ulang.lower() == "Tidak" :
        print(" ")
        print("---------------------------------------")
        print("SELESAI")
        print(" ")
        print("---------------------------------------")
        start = False   