#merge sort
def mergesorrt(list1):
    if len(list1)>1:
        mid=len(list1)//2
        print("yang akan dipisahkan => ",list1)
        left_list=list1[:mid]
        right_list=list1[mid:]
        print("Hasil pemisahan => ",left_list,"------",right_list)
        mergesorrt(left_list)
        mergesorrt(right_list)

        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                list1[k]=left_list[i]
                i+=1
                k+=1
            else:
                list1[k]=right_list[j]
                j+=1
                k+=1

        while len(left_list)>i:
            list1[k]=left_list[i]
            i+=1
            k+=1
        while len(right_list)>j:
            list1[k]=right_list[j]
            j+=1
            k+=1
        print("yang akan digabungkan => ",left_list,",",right_list)
        print("hasil penggabungan => ",list1)
        print(" ")

#num = int(input("jumlah data: "))
#list1=[int(input())for x in range(num)]
list1=[1,75,42,15,3]
print(list1)
print("\n")
print("MergeSort")
mergesorrt(list1)
print("list terurut: ",list1)
print("\n")
print("\n")



#Quick Sort
#pivot last element untuk ascending
def pivot_last_as(list1,first,last):
    pivot=list1[last]
    left = first
    right = last-1
    while True:
        print("pivot: ",pivot)
        print("left: ",list1[left],", right: ",list1[right])
        while left<=right and list1[left]<=pivot:
            left=left+1
            print("pivot : ",pivot)
            print("left digeser karena left lebih kecil dari pivot: ")
            print("left : ",list1[left],", Right: ",list1[right])
        while right>=left and list1[right]>=pivot:
            right=right-1
            print("pivot : ",pivot)
            print("right digeser karena right lebih besar dari pivot: ")
            print("left: ",list1[left],", Right: ",list1[right])
        if right<left:
            break
        else:
            list1[left],list1[right]=list1[right],list1[left]
        print("swap",list1[right],"dengan",list1[left])
        print("setelah swap: ",list1)
        print(" ")
    list1[last],list1[left]=list1[left],list1[last]
    print("swap",list1[last],"dengan pivot",list1[left])
    print(" ")
    print("list setelah pivot berubah",list1)
    return left

#quicksort pivot last element untuk ascending
def quicksort_as(list1,first,last):
    if first<last:
        p=pivot_last_as(list1,first,last)
        quicksort_as(list1,first,p-1)
        quicksort_as(list1,p+1,last)

#num = int(input("jumlah data: "))
#list1=[int(input())for x in range(num)]
print("Quick Sort")
list2=[1,75,42,15,3]
n=len(list2)
print(list2)
quicksort_as(list2,0,n-1)
print("list terurut: ",list1)
