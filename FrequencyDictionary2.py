lst = [1,2,3,2,1,4,4,3,2,4]
dict={}
done=[]
for i in range(0, len(lst)):
    count = 1
    if lst[i] not in done:
        lst.append(lst[i])
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                count = count + 1
        dict[lst[i]] = count
    else:
        pass
print(dict)
