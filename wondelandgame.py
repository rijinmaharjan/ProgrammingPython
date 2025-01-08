print('WELCOME TO TREASURE LAND')
print('THE GAME STATS NOW')
direc=input('DO YOU WANT TO GO LEFT OR RIGHT? \n TYPE IT HERE: ').lower()
if direc=='right':
    print('GAME OVER')
elif direc=='left':
    sw=input('Congrats you move on. \n Now do you want to swim or wait? \n TYPE IT HERE: ').lower()
    if sw=='swim':
        print('Game over')
    elif sw=='wait':
        colour=input('Congrats you move on. \n Now choose a colour between red yellow and blue: ').lower()
        if colour in ['red','blue']:
            print('Game over')
        elif colour=='yellow':
            print('You win')
        else:
            print('invalid choice')   
    else:
        print('invalid choice')   
else:
    print('invalid choice')   