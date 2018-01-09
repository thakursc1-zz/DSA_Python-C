def partition(tmp,arr,left,right):
  
  if(left>=right):
    return tmp 
    
  mid = (right + left)//2
  
  partition(tmp,arr,left,mid)
  partition(tmp,arr,mid+1,right)
  merge(tmp,arr,left,mid,right)
  
  return tmp
  
def merge(tmp,arr,left,mid,right):
  lstart = left
  rstart = mid+1 
  index = lstart
  
  while(lstart<=mid and rstart<=right):
    if(arr[lstart]<=arr[rstart]):
      tmp[index]= arr[lstart]
      lstart+=1 
      index+=1 
    else:
      tmp[index] = arr[rstart]
      rstart+=1 
      index+=1 
    
  while(lstart<=mid):
    tmp[index] = arr[lstart]
    lstart+=1 
    index+=1 
    
  while(rstart<=right):
    tmp[index]=arr[right]
    rstart+=1 
    index+=1 
    
  while(left<=right):
    arr[left]=tmp[left]
    left+=1
    
  #print(arr)
  return

def mergesort(arr):
  return partition(arr[:],arr,0,len(arr)-1)
  
  
print(mergesort([8,6,3,2,6,1]))
