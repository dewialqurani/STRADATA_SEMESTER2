def binarySearch(listData, data):
    first=0
    last=len(listData)-1
    found=False
    temp=[]
    while first<=last and not found:
        midpoint=(first+last)//2
        if listData[midpoint]==data:
            found=True
            temp.append(midpoint)
            midpoint1 = midpoint
            if midpoint == last:
                break
            elif midpoint == first:
                break
            else:
                
                while listData[midpoint1+1] == data:
                    if midpoint1+1 == last:
                        temp.append(midpoint1+1)
                        break
                    else:
                        temp.append(midpoint1+1)
                        midpoint1 += 1

                while listData[midpoint-1] == data:
                    if midpoint-1 == first:
                        temp.insert(0, midpoint-1)
                        break
                    else:
                        temp.insert(0,midpoint-1)
                        midpoint -= 1
                
        else:
            if data<listData[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1

    if found==True:
        print('posisi data  =', temp)
        return found
    else:
        print('Data tidak ada')
        return False

a=[1, 5, 9, 8, 1, 5, 10, 26, 5, 12]
print(binarySearch(a, 0))
