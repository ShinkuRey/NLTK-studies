u_i = int(input())



def Fibonacci(x):
    f = [0,1]
    if x > 2:
        for i in range(2, x+1):
                new = f[i-1] + f[i-2]
                f.append(new)
        return f[-1]
    elif x == 1:
        return 1
    else:
        return 0
    
print(Fibonacci(u_i))