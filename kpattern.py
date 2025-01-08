for row in range(5):
    for column in range(18):
        if (column==0 or column==5 or column==8 or column==11 or column==13 or column==17):
            print('*',end=' ')
        elif (column in [1,2,3,7,9]) and row==0:
            print('*',end=' ')
        elif (column in [3,14]) and row==1:
            print('*',end=' ')
        elif (column in [1,2,3,15]) and row==2:
            print('*',end=' ')
        elif (column in [1,2,7,16]) and row==3:
            print('*',end=' ')
        elif (column in [3,7]) and row==4:
            print('*',end=' ')
        else:
            print(end='  ')
    print()        