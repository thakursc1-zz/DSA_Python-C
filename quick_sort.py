def quicksort(arr,left,right):
  if left>=right:
    return arr
    
  pi = partition(arr,left,right)
  quicksort(arr,left,pi-1)
  quicksort(arr,pi+1,right)
  return arr
  
  
def partition(arr,left,right):
  pivot = arr[right]
  pi = left
  
  for i in range(left,right):
    if arr[i]<=pivot:
      temp = arr[i]
      arr[i] = arr[pi]
      arr[pi] = temp 
      pi+=1

  
  temp  = arr[pi]
  arr[pi] = arr[right]
  arr[right] = temp 
  
  print(pi)
  
  return pi
  
  
  
print(quicksort([5,3,4,2,1],0,4))
