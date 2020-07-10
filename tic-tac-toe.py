board={
'1':' ','2':' ','3':' ',
'4':' ','5':' ','6':' ',
'7':' ','8':' ','9':' '
}

player=1
moves=0
end_check=0

print()
player1 = input("enter name of player 1: ")
player2 = input("enter name of player 2: ")
print()

def check():
     if board['1']=='X' and board['2']=='X' and board['3']=='X':
          print()
          print('    '+player1+' won !!')
          print()
          return 1
     if board['4']=='X' and board['5']=='X' and board['6']=='X':
          print()
          print('    '+player1+' won !!')
          print()
          return 1  
     if board['7']=='X' and board['8']=='X' and board['9']=='X':
          print()
          print('    '+player1+' won !!')
          print()
          return 1
     if board['1']=='X' and board['4']=='X' and board['7']=='X':
          print()
          print('    '+player1+' won !!')
          print()
          return 1
     if board['2']=='X' and board['5']=='X' and board['8']=='X':
          print()
          print('    '+player1+' won !!')
          print()
          return 1
     if board['3']=='X' and board['6']=='X' and board['9']=='X':
          print()
          print('    '+player1+' won !!')
          print()
          return 1
     if board['1']=='X' and board['5']=='X' and board['9']=='X':
          print()
          print('    '+player1+' won !!')
          print()
          return 1
     if board['3']=='X' and board['5']=='X' and board['7']=='X':
          print()
          print('    '+player1+' won !!')
          print()
          return 1
     if board['1']=='O' and board['2']=='O' and board['3']=='O':
          print()
          print('    '+player2+' won !!')
          print()
          return 1
     if board['4']=='O' and board['5']=='O' and board['6']=='O':
          print()
          print('    '+player2+' won !!')
          print()
          return 1  
     if board['7']=='O' and board['8']=='O' and board['9']=='O':
          print()
          print('    '+player2+' won !!')
          print()
          return 1
     if board['1']=='O' and board['4']=='O' and board['7']=='O':
          print()
          print('    '+player2+' won !!')
          print()
          return 1
     if board['2']=='O' and board['5']=='O' and board['8']=='O':
          print()
          print('    '+player2+' won !!')
          print()
          return 1
     if board['3']=='O' and board['6']=='O' and board['9']=='O':
          print()
          print('    '+player2+' won !!')
          print()
          return 1
     if board['1']=='O' and board['5']=='O' and board['9']=='O':
          print()
          print('    '+player2+' won !!')
          print()
          return 1
     if board['3']=='O' and board['5']=='O' and board['7']=='O':
          print()
          print('    '+player2+' won !!')
          print()
          return 1
     return 0


print(' 1 | 2 | 3 ')
print('---+---+---')
print(' 4 | 5 | 6 ')
print('---+---+---')
print(' 7 | 8 | 9 ')
print()

while True:
     print(' '+board['1']+' | '+board['2']+' | '+board['3']+' ')
     print('---+---+---')
     print(' '+board['4']+' | '+board['5']+' | '+board['6']+' ')
     print('---+---+---')
     print(' '+board['7']+' | '+board['8']+' | '+board['9']+' ')
     ch = check()
     if ch==1:
          break
     if moves==9:
          print("game draw !!")
          break
     print()
     while True:
          if player==1:
               player1_input = input(player1+"'s turn: ")
               if (player1_input in board and board[player1_input]==' '):
                    board[player1_input]='X'
                    player=2
                    break
               else:
                    print('invalid input! please try again')
                    continue
          elif player==2:
               player2_input = input(player2+"'s turn: ")
               if player2_input in board and board[player2_input]==' ':
                    board[player2_input]='O'
                    player=1
                    break
               else:
                    print('invalid input! please try again')
                    continue
          moves+=1
          print('**********************************')
                      




















