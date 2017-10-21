def insertion(arr):
  i= 1
  while(i<len(arr)):
    j  =  i 
    while(j>0 and arr[j-1]>arr[j]):
      temp = arr[j-1]
      arr[j-1] = arr[j]
      arr[j] = temp 
      j-=1 
    
    i+=1 
  return arr
  
  
  
print(insertion([5,3,4,2,1]))
