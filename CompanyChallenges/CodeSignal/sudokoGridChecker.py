def solution(grid):
    r = len(grid)
    c = len(grid[0])
    
    # Row Check
    # for c in range(c):
    #     row_ans = []
    #     row_sum = 0
    #     for i in range(r):
    #         row_sum += grid[i][0]
    #     if row_sum == 45:
    #         row_ans.append(True)
    #     else:
    #         row_ans.append(False)
    
    # print(row_ans)
    
    # Row Check
    for col in range(c):
        row_map = {}
        #count = 0
        for i in range(r):
            if grid[i][col] != ".":
                if grid[i][col] not in row_map:
                    row_map[grid[i][col]] = 0
                row_map[grid[i][col]] += 1 
            #count += 1 
        #print("ROW Map - S")
        # print(row_map)
        for key, val in row_map.items():
            if val > 1:
                return False
        #print("ROW Map - E")
    
    # Col Check
    for row in range(r):
        col_map = {}
        for j in range(c):
            if grid[row][j] != ".":
                if grid[row][j] not in col_map:
                    col_map[grid[row][j]] = 0
                col_map[grid[row][j]] += 1
        #print("COL Map - S")
        # print(col_map)
        for key, val in col_map.items():
            if val > 1:
                return False
        #print("COL Map - S")
    
    # 3*3 Grid Check
    for i in range(0, r, 3):
        for j in range(0, c, 3):
            grid_map = {}
            for row in range(i,i+3):
                for col in range(j,j+3):
                    #print(grid[row][col], end = " ")
                    if grid[row][col] != ".":
                        if grid[row][col] not in grid_map:
                            grid_map[grid[row][col]] = 0
                        grid_map[grid[row][col]] += 1
            print("Grid Map - S")
            print(grid_map)
            for key,val in grid_map.items():
                if val > 1:
                    print ((key, val))
                    return False
                # if val > 1:
                #     return False
            print("Grid Map - E")
            #     print()
            # print()
            # if grid[i][j] != ".":
            #     if grid[i][j] not in grid_map:
            #         grid_map[grid[i][j]] = 0
            #     grid_map[grid[i][j]] += 1
        # print("Grid Map - S")
        # print(grid_map)
        # print("Grid Map - E")
    
    return True