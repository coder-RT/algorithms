
if __name__ == '__main__':
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    
    m = {}
    ans = 0
    
    for i in range(len(A)):
        for j in range(len(B)):
            target = A[i] + B[j]

            if target not in m:
                m[target] = 0
            m[target] += 1
    
    for k in range(len(C)):
        for l in range(len(D)):
            target = -(C[k] + D[l])
            if target in m:
                ans += m[target]
                
    print(ans)