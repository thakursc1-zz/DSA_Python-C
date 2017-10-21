def bubble(arr):
  end = len(arr)-1
  while(end>0):
    for i in range(1,end+1):
      if arr[i]<=arr[i-1]:
        temp = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = temp
    
    print(arr)
    end-=1 
  return arr
  
  
  
print(bubble([8,6,3,2,6,1]))
