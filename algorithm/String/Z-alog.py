
def z_alog(s:str):    
    Z = [0] * (len(s))
    Z[0] = len(s)
    i, j = 1, 0
    while i < len(s):
        while (i+j < len(s) and s[j] == s[i+j]): j += 1
        Z[i] = j

        if j == 0:
            i += 1
            continue
            
        k = 1
        while (k < j and k+Z[k] < j):
            Z[i+k] = Z[k]
            k += 1
        
        i+= k
        j -= k
    return Z

if __name__ == "__main__":
    print(z_alog("a"))
    print(z_alog("momomohimomokusa"))