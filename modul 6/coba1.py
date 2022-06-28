def binSearch(listData, key, first=0, last=0, result=[]):
    ind = int
    found = False
    first = first or 0
    last = last or len(listData) - 1
    print("data: ", listData)
    print("posisi data :", )
    while first <= last and not found:
        mid = (first+last) // 2
        if listData[mid] == key:
            found = True
            ind = mid

        elif key > listData[mid]:
            return binSearch(listData, key, mid + 1, last, result)

        elif key < listData[mid]:
            return binSearch(listData, key, first, mid, result)

    result.append(ind)
    if found:
        count = 1
        check = True

        while check == True:
            if (ind + count) <= (len(listData)-1):

                if listData[ind] == listData[ind + count]:
                    result.append(ind + count)
                    count += 1

                elif listData[ind] == listData[ind - count]:
                    result.append(ind - count)
                    count += 1

                else:
                    check = False

            else:
                check = False

        return sorted(result)

    else:
        return False
 
print(binSearch([2, 12, 15, 15, 15, 15, 15, 25, 30, 30, 30, 54, 54, 73], 15))
