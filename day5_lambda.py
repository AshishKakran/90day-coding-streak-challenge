cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    
    if n == 0:
        return []
    
    if n == 1:
        return [0]
    
    if n == 2:
        return [0,1]
        
    f = [0,1]
    for i in range(2,n): 
        f.append(f[i-1] + f[i-2])
        
 
    return f

        
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
