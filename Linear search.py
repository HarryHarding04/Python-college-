def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = [1, 3, 6, 7, 8, 10]
x = 6
print(x, "found at", linearsearch(arr,x))
