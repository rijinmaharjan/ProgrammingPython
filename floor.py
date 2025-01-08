floor=['floor1','floor2','floor3']
room=[1,2,3]
for i in floor:
    for j in room:
        if i=='floor1':
            if j==1 or j==2:
                continue
            else:
                print(f'{i}, {j}')
        elif i=='floor2':
            if j==3:
                continue
            else:
                print(f'{i}, {j}')
        else:
            if j==1 or j==3:
                continue
            else:
                print(f'{i}, {j}')
                