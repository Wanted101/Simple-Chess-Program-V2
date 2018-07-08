# Author: Duncan Podmore
# Date started: 04/07/2018
# Date Last Edited: 07/07/2018
# Program Description: Simple Chess Program
# Version: 2.0


from tkinter import *
from ChessClasses import *



Game = Tk()
Game.title("My Chess Program V2.0")
Game.state("zoomed")

"""
class NewGame:
	def __init__(self):
		start_game_button = Button(Game, bg = "white", width = 8, height = 4, \
			command = startGame)
"""

# Create the squares



A1 = Square(1, 8, "lime", Game)
A2 = Square(1, 7, "white", Game)
A3 = Square(1, 6, "lime", Game)
A4 = Square(1, 5, "white", Game)
A5 = Square(1, 4, "lime", Game)
A6 = Square(1, 3, "white", Game)
A7 = Square(1, 2, "lime", Game)
A8 = Square(1, 1, "white", Game)
B1 = Square(2, 8, "white", Game)
B2 = Square(2, 7, "lime", Game)
B3 = Square(2, 6, "white", Game)
B4 = Square(2, 5, "lime", Game)
B5 = Square(2, 4, "white", Game)
B6 = Square(2, 3, "lime", Game)
B7 = Square(2, 2, "white", Game)
B8 = Square(2, 1, "lime", Game)
C1 = Square(3, 8, "lime", Game)
C2 = Square(3, 7, "white", Game)
C3 = Square(3, 6, "lime", Game)
C4 = Square(3, 5, "white", Game)
C5 = Square(3, 4, "lime", Game)
C6 = Square(3, 3, "white", Game)
C7 = Square(3, 2, "lime", Game)
C8 = Square(3, 1, "white", Game)
D1 = Square(4, 8, "white", Game)
D2 = Square(4, 7, "lime", Game)
D3 = Square(4, 6, "white", Game)
D4 = Square(4, 5, "lime", Game)
D5 = Square(4, 4, "white", Game)
D6 = Square(4, 3, "lime", Game)
D7 = Square(4, 2, "white", Game)
D8 = Square(4, 1, "lime", Game)
E1 = Square(5, 8, "lime", Game)
E2 = Square(5, 7, "white", Game)
E3 = Square(5, 6, "lime", Game)
E4 = Square(5, 5, "white", Game)
E5 = Square(5, 4, "lime", Game)
E6 = Square(5, 3, "white", Game)
E7 = Square(5, 2, "lime", Game)
E8 = Square(5, 1, "white", Game)
F1 = Square(6, 8, "white", Game)
F2 = Square(6, 7, "lime", Game)
F3 = Square(6, 6, "white", Game)
F4 = Square(6, 5, "lime", Game)
F5 = Square(6, 4, "white", Game)
F6 = Square(6, 3, "lime", Game)
F7 = Square(6, 2, "white", Game)
F8 = Square(6, 1, "lime", Game)
G1 = Square(7, 8, "lime", Game)
G2 = Square(7, 7, "white", Game)
G3 = Square(7, 6, "lime", Game)
G4 = Square(7, 5, "white", Game)
G5 = Square(7, 4, "lime", Game)
G6 = Square(7, 3, "white", Game)
G7 = Square(7, 2, "lime", Game)
G8 = Square(7, 1, "white", Game)
H1 = Square(8, 8, "white", Game)
H2 = Square(8, 7, "lime", Game)
H3 = Square(8, 6, "white", Game)
H4 = Square(8, 5, "lime", Game)
H5 = Square(8, 4, "white", Game)
H6 = Square(8, 3, "lime", Game)
H7 = Square(8, 2, "white", Game)
H8 = Square(8, 1, "lime", Game)


WApawn = Pawn(A2, "white")
WBpawn = Pawn(B2, "white")
WCpawn = Pawn(C2, "white")
WDpawn = Pawn(D2, "white")
WEpawn = Pawn(E2, "white")
WFpawn = Pawn(F2, "white")
WGpawn = Pawn(G2, "white")
WHpawn = Pawn(H2, "white")
WArook = Rook(A1, "white")
WHrook = Rook(H1, "white")
WBknight = Knight(B1, "white")
WGknight = Knight(G1, "white")
WDSbishop = Bishop(C1, "white")
WLSbishop = Bishop(F1, "white")
Wqueen = Queen(D1, "white")
Wking = King(E1, "white")

BApawn = Pawn(A7, "lime")
BBpawn = Pawn(B7, "lime")
BCpawn = Pawn(C7, "lime")
BDpawn = Pawn(D7, "lime")
BEpawn = Pawn(E7, "lime")
BFpawn = Pawn(F7, "lime")
BGpawn = Pawn(G7, "lime")
BHpawn = Pawn(H7, "lime")
BArook = Rook(A8, "lime")
BHrook = Rook(H8, "lime")
BBknight = Knight(B8, "lime")
BGknight = Knight(G8, "lime")
BDSbishop = Bishop(C8, "lime")
BLSbishop = Bishop(F8, "lime")
Bqueen = Queen(D8, "lime")
Bking = King(E8, "lime")

A3I = InitEmptySquare(A3)
A4I = InitEmptySquare(A4)
A5I = InitEmptySquare(A5)
A6I = InitEmptySquare(A6)
B3I = InitEmptySquare(B3)
B4I = InitEmptySquare(B4)
B5I = InitEmptySquare(B5)
B6I = InitEmptySquare(B6)
C3I = InitEmptySquare(C3)
C4I = InitEmptySquare(C4)
C5I = InitEmptySquare(C5)
C6I = InitEmptySquare(C6)
D3I = InitEmptySquare(D3)
D4I = InitEmptySquare(D4)
D5I = InitEmptySquare(D5)
D6I = InitEmptySquare(D6)
E3I = InitEmptySquare(E3)
E4I = InitEmptySquare(E4)
E5I = InitEmptySquare(E5)
E6I = InitEmptySquare(E6)
F3I = InitEmptySquare(F3)
F4I = InitEmptySquare(F4)
F5I = InitEmptySquare(F5)
F6I = InitEmptySquare(F6)
G3I = InitEmptySquare(G3)
G4I = InitEmptySquare(G4)
G5I = InitEmptySquare(G5)
G6I = InitEmptySquare(G6)
H3I = InitEmptySquare(H3)
H4I = InitEmptySquare(H4)
H5I = InitEmptySquare(H5)
H6I = InitEmptySquare(H6)

Board.boardGrid(A8, B8, C8, D8, E8, F8, G8, H8, \
	A7, B7, C7, D7, E7, F7, G7, H7, \
	A6, B6, C6, D6, E6, F6, G6, H6, \
	A5, B5, C5, D5, E5, F5, G5, H5, \
	A4, B4, C4, D4, E4, F4, G4, H4, \
	A3, B3, C3, D3, E3, F3, G3, H3, \
	A2, B2, C2, D2, E2, F2, G2, H2, \
	A1, B1, C1, D1, E1, F1, G1, H1)



Game.mainloop()