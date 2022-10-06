def Bubblesort(arr):
    n=len(arr)
    swapped=False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if not swapped:
            return

def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[:mid]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(l) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i +=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k]=L[i]
            i+=1
            j+=1
        while j< len(R):
            arr[k]=R[j]
            j+=1
            k+=1


def insertionSort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key


def shellSort(arr):
    gap=n//2
    while gap>0:
        j=gap
        while j<n:
            i=j-gap
            while i>=0:
                if arr[i+gap]>arr[i]:
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                i=i-gap
            j+=1
        gap=gap//2


def selectionSort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1, size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step], array[min_idx])=(array[min_idx], array[step])






#input from the user
a=[]
n=int(input("number of element"))
for i in range(0,n):
    l=int(input())
    a.append(l)
print("the entered array by the user is =", a)
for i in range(0, len(a)):    
    print(a[i], end=" ");


#menu


print("1. insertion sort")
print("2. bubble Sort")
print("2. merge Sorst")
print("4. selection Sort")

print("")
print("")


