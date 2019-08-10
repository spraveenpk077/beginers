def sumKRepeating(arr, n, k): 
    sum = 0
  
    # To keep track of processed elements 
    visited = [False for i in range(n)] 
  
    # initializing count equal to zero 
    for i in range(0, n, 1): 
          
        # If arr[i] already processed 
        if (visited[i] == True): 
            continue
  
        # counting occurrences of arr[i] 
        count = 1
        for j in range(i + 1, n, 1): 
            if (arr[i] == arr[j]): 
                count += 1
                visited[j] = True
      
        if (count == k): 
            sum += arr[i] 
  
    return sum
  
# Driver code 
if __name__ == '__main__': 
    arr = [9, 9, 10, 11, 8, 8, 9, 8] 
    n = len(arr) 
    k = 3
    print(sumKRepeating(arr, n, k)) 
