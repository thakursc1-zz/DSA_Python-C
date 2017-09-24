#O(n) solution for finding a duplicate in a string python by bit masking 
s  = "strings"
def find_dup(s):
    c = 0
    for i in s:
      val = ord(i) - ord('a')
      if (c & (1<<val))>0:
        print('{0:b}'.format(c),"duplicate Found",i)
        return False 
      c |= 1<<val
      print('{0:b}'.format(c), "And",i)
    
    return True 
    
print(find_dup(s))
    
