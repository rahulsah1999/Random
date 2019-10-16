def search(lis, x):
    for i in reversed(range(len(lis))):
        if lis[i] == x:
            return i
        
lis = [1,3,9,3,9,1]
n = int(input("Enter the number to be searched : "))
print("Found last at position ",search(lis,n))
