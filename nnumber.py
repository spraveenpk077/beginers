def multiple(m, n): 
  
    # inserts all elements from n to  
    # (m * n)+1 incremented by n. 
    a = range(n, (m * n)+1, n) 
      
    print(*a) 
  
# driver code  
m = 4
n = 3
multiple(m, n)
