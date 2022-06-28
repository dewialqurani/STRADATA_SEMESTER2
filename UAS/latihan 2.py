#Soal Bagian2
def remainderFunction(data,num): #Membuat hash dari data mod num
    return(data%num)

def strVal(strData): #Hash for string
    temp = 0
    for x in range(len(strData)):
        temp += ord(strData[x])
    return(temp)

def createHashTable(num): #Membuat table untuk store data hash, range(num)
    temp = []
    for i in range(num):
        temp.append([None])
    return(temp)

def putData(data,table): #Function untuk store data ke dlm table
    for i in range(len(data)):
        int_data = strVal(data[i])
        ind = remainderFunction(int_data,len(table)) #Deklarasi var sbgai membuat nilai hash
        temp = []
        temp.append(data[i])
        if type(table[ind]) == list and len(table[ind]) >= 1 and (table[ind] != [None]) : #Chaining
            table[ind].append(data[i])
        else:
            table[ind] = temp
          
    return(table)

def searchHash(data,table): #Matching data dari dlm table, output berupa boolean
    int_data = strVal(data)
    hashVal = remainderFunction(int_data, len(table))
    if data in table[hashVal]:
        find_index = table[hashVal].index(data)
        return("Data '{}' terdapat di slot {} indeks: {}".format(data,hashVal,find_index))
    else:
        return("Data '{}' tidak ada".format(data))

print("\nBagian2\n")
data = ["diah","dina","andi","hadi","tiara"]
hashTable = createHashTable(11)
hashTable = putData(data,hashTable)
print(searchHash("indah",hashTable))
print(searchHash("dina",hashTable))
print(searchHash("andi",hashTable))
print(searchHash("hadi",hashTable))
print(searchHash("diah",hashTable))