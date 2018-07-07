def diagonal_diff(matrix):
    i = matrix[0]
    l_to_r=sum([matrix[x][x] for x in range(i)])
    r_to_l=sum([matrix[x][-1-i] for x in range(i)])
    print(l_to_r)
    print(r_to_l)


mat = [4,
         [1,2,3,4],
        [4,5,6,5],
        [9,8,9,3],
        [1,4,5,6]
    ]

print(diagonal_diff(mat))
