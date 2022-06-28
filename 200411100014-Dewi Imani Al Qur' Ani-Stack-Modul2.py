def stack() :
    s=[]
    return s
def push (s,data) : #push, penambahan data
    s.append(data)
    return s
def pop (s) :   #pop, penghapusan data
    data = s.pop()
    return data
def peek(s) :   #peek, informasi data yang terletak pada posisi top 
    return (s[len(s)-1])
def isEmpty(s) :    #isEmpty, memeriksa apakah stack dalam keadaan kosong
    return(s==[])
def size (s) :  #jumlah data yang terdapat pada stack
    return(len(s))

#fungsi mengecek tanda kurung
def checkkurung (data) : 
    st = stack()
    data = data.replace(" ","") 
    kurungbuka = "({["
    kurungtutup = ")}]"
    check = True
    for i in data :
        if i in kurungbuka :
            push(st,i)
        elif i in kurungtutup :
            if not isEmpty(st) :
                if kurungbuka.index(peek(st)) == kurungtutup.index(i) :
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
    if checkkurung(data) is True :
        st = stack()
        infix = data.replace(" ","")
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
                while temp != kurungbuka[kurungtutup.index(i)] :
                    postfix.append(temp)
                    temp = pop(st)
            else :
                while not (isEmpty(st)) and operator[peek(st)] >= operator[i] :
                    postfix.append(pop(st))
                push(st,i)
        while not (isEmpty(st)) :
            postfix.append(pop(st))

        return True, "".join(postfix)
    else :
        return False, checkkurung(data)

#fungsi untuk operasi
def operasi(data1,operator,data2) :
    c = str(data2) + operator + str(data1)
    return eval(c)

#fungsi evaluasi operasi aritmetika postfix
def Evaluatepostfix(postfix):
    st = stack() 
    output =""
    operator = ['*','/','-','+']
    for i in postfix:
        if i in operator:
            total = operasi(pop(st),i,pop(st))
            push(st,total)
        else:
            push(st,i)
    while not isEmpty(st) :
        output = str(pop(st)) + output
    return output
start = True
while start :
    inp = str(input("Masukkan String O0perasi Aritmatika   =    "))
    a,b = infixtopostfix(inp)
    if a is True :
        print("Infix :   ",inp,"   ;   ","Postfix :     ",b,"  =  ",Evaluatepostfix(b))
    else :
        print(b)
    ulang = input("lngin Melanjutkan Operasi Aritmetika Selanjutnya ? (y/t) : ")
    if ulang.lower() == "t" :
        print(" ")
        print("---------------------------------------")
        print("SELESAI")
        print(" ")
        print("---------------------------------------")
        start = False   