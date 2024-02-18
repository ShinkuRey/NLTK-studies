u_i = input()



def trim(x):
    while len(x) > 1:
        c = sum(int(j) for j in str(x))
        x = str(c)
    return int(x)
    
print(trim(u_i))