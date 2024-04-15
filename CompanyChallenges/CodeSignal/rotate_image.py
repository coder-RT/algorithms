def solution(a):
    r = len(a)
    c = len(a[0])
    
    for i in range(r):
        for j in range(c):
            if i != j and i < j: # Execute only till half portion of an array
                temp = a[i][j]
                a[i][j] = a[j][i]
                a[j][i] = temp
    
    for i in range(r):
        lft = 0
        rgt = len(a[i])-1
        
        while lft < rgt:
            temp = a[i][lft]
            a[i][lft] = a[i][rgt]
            a[i][rgt] = temp
            lft += 1
            rgt -= 1
    
    return a