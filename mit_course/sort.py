#insertionSort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
arr = [12, 6, 2, 78, 64]
insertionSort(arr)
for i in range(len(arr)):
    print (arr[i])
    
#mergeSort
def mergeSort(arr):
    if len(arr) > 1:
          mid = len(arr)//2
          L = arr[:mid]
          R = arr[mid:]
          mergeSort(L)
          mergeSort(R)
          i = j = k = 0

          while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
         
          while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
          while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
  
if __name__ == '__main__':
    arr = [43,73,23,773,325]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)