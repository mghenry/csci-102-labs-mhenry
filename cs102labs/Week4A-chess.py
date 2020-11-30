#   Maggie Henry
#   ​CSCI 102 – Section G
#   Week 4 - Lab A - Missing Chess Pieces
#   References: none
#   Time: 20 minutes

king = int(input('KINGS>'))
queen = int(input('QUEENS>'))
rook = int(input('ROOKS>'))
bishop = int(input('BISHOPS>'))
knight = int(input('KNIGHTS>'))
pawn = int(input('PAWNS>'))

if king != 1:
    new_king = (1 - king)
elif king == 1:
    new_king = 0


if queen != 1:
    new_queen = (1 - queen)
elif queen == 1:
    new_queen = 0


if rook != 2:
    new_rook = (2 - rook)
elif rook == 2:
    new_rook = 0


if bishop != 2:
    new_bishop = (2 - bishop)
elif bishop == 2:
    new_bishop = 0


if knight != 2:
    new_knight = (2 - knight)
elif knight == 2:
    new_knight = 0


if pawn != 8:
    new_pawn = (8 - pawn)
elif pawn == 8:
    new_pawn = 0


print('The output below provides the number of each type you have (over or under):')
print('OUTPUT>', new_king, new_queen, new_rook, new_bishop, new_knight, new_pawn, end="")




    
           
