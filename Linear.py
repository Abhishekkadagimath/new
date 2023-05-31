import time
def linearsearch(a,key):
    n=len(a)
    for i in range(n):
        if a[i] == key:
            return i;
            return -1
        a=[13,24,35,46,57,68,79]
        start=time.time()
        print("The array elements are:",a)
        k=int(input("enter the key element to search:"))
        i=linearsearch(a,k)
if i == -1:
    print("search unsuccessful")
else:
   print("search successful key found at location:",i+1)
   end=time.time
   print("Runtime of the program is",end-start)
