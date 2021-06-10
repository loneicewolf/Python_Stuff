
for i in enumerate(range(3,5)):
    print([(i) for i in range(i[0],i[1])])
# output #
# [0, 1, 2]
# [1, 2, 3]

for i in enumerate(range(5,10)):
    print([(i) for i in range(i[0],i[1])])
# [0, 1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [2, 3, 4, 5, 6]
# [3, 4, 5, 6, 7]
# [4, 5, 6, 7, 8]
