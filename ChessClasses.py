# Class module for Main.py of Chess program

from tkinter import *

class Board:
	Wpawns_captured = 0
	Bpawns_captured = 0
	Wrooks_captured = 0
	Brooks_captured = 0
	Wknights_captured = 0
	Bknights_captured = 0
	Wbishops_captured = 0
	Bbishops_captured = 0
	Wqueen_captured = False
	Bqueen_captured = False

	A1_rook_moved = False
	H1_rook_moved = False
	A8_rook_moved = False
	H8_rook_moved = False
	Wking_moved = False
	Bking_moved = False

	whites_turn = True
	blacks_turn = False
	first_click = True
	check = False

	empty_square_picture = None
	board_grid1 = [] 
	board_grid2 = []
	valid_squares = []
	piece_last_clicked = "empty_square"
	square_last_clicked = None
	@classmethod
	def higlightValidSquares(cls):
		for i in Board.valid_squares:
			i.square_button.config(bg = "red")

	@classmethod
	def secondClick (cls):
		cls.first_click = True
		for i in cls.board_grid1:
			i.square_button.config(bg = i.default_colour)
		cls.valid_squares = []
		cls.piece_last_clicked = "empty_square"
		cls.square_last_clicked = None

	@classmethod # Allows access to squares by index
	def boardGrid(cls, A8i, B8i, C8i, D8i, E8i, F8i, G8i, H8i, \
		A7i, B7i, C7i, D7i, E7i, F7i, G7i, H7i, \
		A6i, B6i, C6i, D6i, E6i, F6i, G6i, H6i, \
		A5i, B5i, C5i, D5i, E5i, F5i, G5i, H5i, \
		A4i, B4i, C4i, D4i, E4i, F4i, G4i, H4i, \
		A3i, B3i, C3i, D3i, E3i, F3i, G3i, H3i, \
		A2i, B2i, C2i, D2i, E2i, F2i, G2i, H2i, \
		A1i, B1i, C1i, D1i, E1i, F1i, G1i, H1i):
		
		cls.board_grid1 = [A8i, B8i, C8i, D8i, E8i, F8i, G8i, H8i, \
		A7i, B7i, C7i, D7i, E7i, F7i, G7i, H7i, \
		A6i, B6i, C6i, D6i, E6i, F6i, G6i, H6i, \
		A5i, B5i, C5i, D5i, E5i, F5i, G5i, H5i, \
		A4i, B4i, C4i, D4i, E4i, F4i, G4i, H4i, \
		A3i, B3i, C3i, D3i, E3i, F3i, G3i, H3i, \
		A2i, B2i, C2i, D2i, E2i, F2i, G2i, H2i, \
		A1i, B1i, C1i, D1i, E1i, F1i, G1i, H1i]
		
		cls.board_grid2 = [[A8i, B8i, C8i, D8i, E8i, F8i, G8i, H8i], \
		[A7i, B7i, C7i, D7i, E7i, F7i, G7i, H7i], \
		[A6i, B6i, C6i, D6i, E6i, F6i, G6i, H6i], \
		[A5i, B5i, C5i, D5i, E5i, F5i, G5i, H5i], \
		[A4i, B4i, C4i, D4i, E4i, F4i, G4i, H4i], \
		[A3i, B3i, C3i, D3i, E3i, F3i, G3i, H3i], \
		[A2i, B2i, C2i, D2i, E2i, F2i, G2i, H2i], \
		[A1i, B1i, C1i, D1i, E1i, F1i, G1i, H1i]]

	@classmethod  #  
	def pawnCaptured(cls, color):
		if color == "white":
			cls.Wpawns_captured += 1
		else:
			cls.Bpawns_captured += 1

	@classmethod
	def rookCaptured(cls, color):
		if color == "white":
			cls.Wrooks_captured += 1
		else:
			cls.Brooks_captured += 1

	@classmethod
	def knightCaptured(cls, color):
		if color == "white":
			cls.Wknights_captured += 1
		else:
			cls.Bknights_captured += 1

	@classmethod
	def bishopCaptured(cls, color):
		if color == "white":
			cls.Wbishops_captured += 1
		else:
			cls.Bbishops_captured += 1

	@classmethod
	def queenCaptured(cls, color):
		if color == "white":
			cls.Wqueen_captured = True
		else:
			cls.Bqueen_captured = True


class Square:
	def __init__(self, file, rank, colour, root, piece=""):
		self.file = file
		self.rank = rank
		self.colour = colour
		self.root = root
		self.piece = piece
		self.temp3 = 0
		self.temp4 = 0
		self.temp5 = 0

		self.default_colour = self.colour
		self.square_button = Button(root, bg = colour, width = 8, height = 4, \
			command = self.onClick)
		self.square_button.grid(column = file, row = rank)
		self.y = self.square_button.grid_info()['row']
		self.x = self.square_button.grid_info()['column']

		self.Wpiece_dict = {
			"Wpawn": self.WpawnMove,
			"Wrook": self.WrookMove,
			"Wknight": self.WknightMove,
			"Wbishop": self.WbishopMove,
			"Wqueen": self.WqueenMove,
			"Wking": self.WkingMove
		}
		self.Bpiece_dict = {
			"Bpawn": self.BpawnMove,
			"Brook": self.BrookMove,
			"Bknight": self.BknightMove,
			"Bbishop": self.BbishopMove,
			"Bqueen": self.BqueenMove,
			"Bking": self.BkingMove
		}
		self.y = self.square_button.grid_info()['row'] 
		self.x = self.square_button.grid_info()['column']

	def onClick(self):
		#print (Board.board_grid2[4][self.x - 1])
		#print (Board.board_grid2[self.x - 1][self.y - 1])
		if Board.first_click == True:
			if self.piece.startswith("W") and Board.whites_turn == True:
				func = self.Wpiece_dict.get(self.piece)
				return func()
			elif self.piece.startswith("B") and Board.blacks_turn == True:
				func = self.Bpiece_dict.get(self.piece)
				return func()
			else:
				Board.secondClick()
				return
		elif Board.first_click == False and Board.board_grid2[self.y - 1][self.x - 1] != Board.square_last_clicked and Board.board_grid2[self.y - 1][self.x - 1] in Board.valid_squares:# and False == True:
			self.temp3 = f"Bitmaps\\{Board.piece_last_clicked}.png"
			self.temp3 = PhotoImage(file = self.temp3)
			Board.square_last_clicked.square_button.config(image = Board.empty_square_picture, \
				width = "60", height = "65")
			if Board.piece_last_clicked == "Wking" and Board.board_grid2[self.y - 1][self.x - 1] == Board.board_grid2[7][6]:
				Board.board_grid2[7][5].piece = "Wrook"
				self.temp4 = PhotoImage(file = "Bitmaps\\Wrook.png")
				Board.board_grid2[7][5].square_button.config(image = self.temp4, width = "60", height = "65")
				Board.board_grid2[7][7].square_button.config(image = Board.empty_square_picture, width = "60", height = "65")
				Board.board_grid2[7][7].piece = ""
			elif Board.piece_last_clicked == "Wking" and Board.board_grid2[self.y - 1][self.x - 1] == Board.board_grid2[7][2]:
				Board.board_grid2[7][3].piece = "Wrook"
				self.temp4 = PhotoImage(file = "Bitmaps\\Wrook.png")
				Board.board_grid2[7][3].square_button.config(image = self.temp4, width = "60", height = "65")
				Board.board_grid2[7][0].square_button.config(image = Board.empty_square_picture, width = "60", height = "65")
				Board.board_grid2[7][0].piece = ""
			elif Board.piece_last_clicked == "Bking" and Board.board_grid2[self.y - 1][self.x - 1] == Board.board_grid2[0][6]:
				Board.board_grid2[0][5].piece = "Brook"
				self.temp4 = PhotoImage(file = "Bitmaps\\Brook.png")
				Board.board_grid2[0][5].square_button.config(image = self.temp4, width = "60", height = "65")
				Board.board_grid2[0][7].square_button.config(image = Board.empty_square_picture, width = "60", height = "65")
				Board.board_grid2[0][7].piece = ""
			elif Board.piece_last_clicked == "Bking" and Board.board_grid2[self.y - 1][self.x - 1] == Board.board_grid2[0][2]:
				Board.board_grid2[0][3].piece = "Brook"
				self.temp4 = PhotoImage(file = "Bitmaps\\Brook.png")
				Board.board_grid2[0][3].square_button.config(image = self.temp4, width = "60", height = "65")
				Board.board_grid2[0][0].square_button.config(image = Board.empty_square_picture, width = "60", height = "65")
				Board.board_grid2[0][0].piece = ""
			if Board.piece_last_clicked == "Wpawn" and self.y == 1:
				self.temp5 = PhotoImage(file = "Bitmaps\\Wqueen.png")
				Board.board_grid2[self.y - 1][self.x - 1].square_button.config(image = self.temp5, width = "60", height = "65")
				Board.board_grid2[self.y - 1][self.x - 1].piece = "Wqueen"
			elif Board.piece_last_clicked == "Bpawn" and self.y == 8:
				self.temp5 = PhotoImage(file = "Bitmaps\\Bqueen.png")
				Board.board_grid2[self.y - 1][self.x - 1].square_button.config(image = self.temp5, width = "60", height = "65")
				self.piece = "Bqueen"
			else:
				Board.board_grid2[self.y - 1][self.x - 1].square_button.config(image = self.temp3, width = "60", height = "65")###
				self.piece = Board.square_last_clicked.piece
			
			if Board.square_last_clicked.piece == "Wrook":
				if Board.square_last_clicked == Board.board_grid2[7][0]:
					Board.A1_rook_moved = True
				elif Board.square_last_clicked == Board.board_grid2[7][7]:
					Board.H1_rook_moved = True
			elif Board.square_last_clicked.piece == "Brook":
				if Board.square_last_clicked == Board.board_grid2[0][0]:
					Board.A8_rook_moved = True
				elif Board.square_last_clicked == Board.board_grid2[0][7]:
					Board.H8_rook_moved = True
			elif Board.square_last_clicked.piece == "Wking":
				Board.Wking_moved = True
			elif Board.square_last_clicked.piece == "Bking":
				Board.Bking_moved = True
			

			Board.square_last_clicked.piece = ""
			if Board.whites_turn == True:
				Board.whites_turn = False
				Board.blacks_turn = True
			else:
				Board.blacks_turn = False
				Board.whites_turn = True
			Board.secondClick()
		else:
			Board.secondClick()

	def WpawnMove(self):
		if Board.first_click == True and Board.whites_turn == True:
			self.square_button.config(bg = "blue")
			if self.y == 7 and Board.board_grid2[4][self.x - 1].piece == "" and Board.board_grid2[self.y - 2][self.x - 1].piece == "":
				Board.valid_squares.append(Board.board_grid2[4][self.x - 1])
			elif self.y == 2:
				pass
			if Board.board_grid2[self.y - 2][self.x - 1].piece == "":
				Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 1])
			try:
				if Board.board_grid2[self.y - 2][self.x - 2].piece.startswith("B") and (self.x - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 2])
			except IndexError:
				pass
			try:
				if Board.board_grid2[self.y - 2][self.x - 0].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 0])			
			except IndexError:
				pass
			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
################################################################################
		elif Board.first_click == False and Board.whites_turn == True:
			pass
		else:
			Board.secondClick()
################################################################################

	def WrookMove(self):
		if Board.first_click == True and Board.whites_turn == True:
			self.square_button.config(bg = "blue")
			for i in range(self.y, 8):
				if Board.board_grid2[i][self.x - 1].piece == "":
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
				elif Board.board_grid2[i][self.x - 1].piece.startswith("W"):
					break
				elif Board.board_grid2[i][self.x - 1].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
					break
			for i in reversed(range(self.y - 1)):
				if Board.board_grid2[i][self.x - 1].piece == "":
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
				elif Board.board_grid2[i][self.x - 1].piece.startswith("W"):
					break
				elif Board.board_grid2[i][self.x - 1].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
					break
			for i in range(self.x, 8):
				if Board.board_grid2[self.y - 1][i].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
				elif Board.board_grid2[self.y - 1][i].piece.startswith("W"):
					break
				elif Board.board_grid2[self.y - 1][i].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
					break
			for i in reversed(range(self.x - 1)):
				if Board.board_grid2[self.y - 1][i].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
				elif Board.board_grid2[self.y - 1][i].piece.startswith("W"):
					break
				elif Board.board_grid2[self.y - 1][i].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
					break
			Board.piece_last_clicked = self.piece
			Board.higlightValidSquares()
			Board.first_click = False
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def WknightMove(self):
		if Board.first_click == True and Board.whites_turn == True:
			self.square_button.config(bg = "blue")
			try:
				if (self.y - 2) >= 0 and (self.x - 3) >= 0 and not Board.board_grid2[self.y - 2][self.x - 3].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 3])
			except IndexError:
				pass
			try: 
				if (self.y - 3) >= 0 and (self.x - 2) >= 0 and not Board.board_grid2[self.y - 3][self.x - 2].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 3][self.x - 2])
			except IndexError:
				pass
			try:
				if (self.x - 2) >= 0 and not Board.board_grid2[self.y + 1][self.x - 2].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y + 1][self.x - 2])
			except IndexError:
				pass
			try: 
				if (self.x - 3) >= 0 and not Board.board_grid2[self.y][self.x - 3].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y][self.x - 3])
			except IndexError:
				pass
			try: 
				if not Board.board_grid2[self.y + 1][self.x].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y + 1][self.x])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y][self.x + 1].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y][self.x + 1])
			except IndexError:
				pass
			try: 
				if (self.y - 2) >= 0 and not Board.board_grid2[self.y - 2][self.x + 1].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x + 1])
			except IndexError:
				pass
			try: 
				if (self.y - 3) >= 0 and not Board.board_grid2[self.y - 3][self.x].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 3][self.x])
			except IndexError:
				pass
			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def WbishopMove(self):
		if Board.first_click == True and Board.whites_turn == True:
			self.square_button.config(bg = "blue")
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp) >= 0 and (self.x - 1 + temp) >= 0:
				if Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp])
				elif Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp].piece.startswith("W"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp])
					break
				temp -= 1
			while (self.y - 1 + temp2) <= 7 and (self.x - 1 + temp2) <= 7:
				if Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2])
				elif Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2].piece.startswith("W"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2])
					break
				temp2 += 1
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp) >= 0 and (self.x - 1 + temp2) <= 7:
				if Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2])
				elif Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2].piece.startswith("W"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2])
					break
				temp -= 1
				temp2 += 1
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp2) <= 7 and (self.x - 1 + temp) >= 0:
				print (10)
				if Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp])
				elif Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp].piece.startswith("W"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp])
					break
				temp2 += 1
				temp -= 1
			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def WqueenMove(self):
		if Board.first_click == True and Board.whites_turn == True:
			self.square_button.config(bg = "blue")
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp) >= 0 and (self.x - 1 + temp) >= 0:
				if Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp])
				elif Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp].piece.startswith("W"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp])
					break
				temp -= 1
			while (self.y - 1 + temp2) <= 7 and (self.x - 1 + temp2) <= 7:
				if Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2])
				elif Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2].piece.startswith("W"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2])
					break
				temp2 += 1
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp) >= 0 and (self.x - 1 + temp2) <= 7:
				if Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2])
				elif Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2].piece.startswith("W"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2])
					break
				temp -= 1
				temp2 += 1
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp2) <= 7 and (self.x - 1 + temp) >= 0:
				if Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp])
				elif Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp].piece.startswith("W"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp])
					break
				temp2 += 1
				temp -= 1

			for i in range(self.y, 8):
				if Board.board_grid2[i][self.x -1].piece == "":
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
				elif Board.board_grid2[i][self.x -1].piece.startswith("W"):
					break
				elif Board.board_grid2[i][self.x -1].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
					break
			for i in reversed(range(self.y - 1)):
				if Board.board_grid2[i][self.x -1].piece == "":
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
				elif Board.board_grid2[i][self.x -1].piece.startswith("W"):
					break
				elif Board.board_grid2[i][self.x -1].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
					break
			for i in range(self.x, 8):
				if Board.board_grid2[self.y - 1][i].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
				elif Board.board_grid2[self.y - 1][i].piece.startswith("W"):
					break
				elif Board.board_grid2[self.y - 1][i].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
					break
			for i in reversed(range(self.x - 1)):
				if Board.board_grid2[self.y - 1][i].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
				elif Board.board_grid2[self.y - 1][i].piece.startswith("W"):
					break
				elif Board.board_grid2[self.y - 1][i].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
					break
			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def WkingMove(self):
		if Board.first_click == True and Board.whites_turn == True:
			self.square_button.config(bg = "blue")
			if Board.Wking_moved == False and Board.H1_rook_moved == False and Board.board_grid2[7][5].piece == "" and Board.board_grid2[7][6].piece == "":
				Board.valid_squares.append(Board.board_grid2[7][6])
			if Board.Wking_moved == False and Board.A1_rook_moved == False and Board.board_grid2[7][1].piece == "" and Board.board_grid2[7][2].piece == "" and Board.board_grid2[7][3].piece == "":
				Board.valid_squares.append(Board.board_grid2[7][2])
			try:	
				if not Board.board_grid2[self.y - 1][self.x - 2].piece.startswith("W") and (self.x - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 1][self.x - 2])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 1][self.x - 0].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][self.x - 0])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 2][self.x - 0].piece.startswith("W") and (self.y - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 0])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 2][self.x - 1].piece.startswith("W") and (self.y - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 1])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 2][self.x - 2].piece.startswith("W") and (self.y - 2) >= 0 and (self.x - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 2])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 0][self.x - 0].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 0][self.x - 0])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 0][self.x - 1].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 0][self.x - 1])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 0][self.x - 2].piece.startswith("W") and (self.x - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 0][self.x - 2])
			except IndexError:
				pass

			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def BpawnMove(self):
		if Board.first_click == True and Board.blacks_turn == True:
			self.square_button.config(bg = "blue")
			if self.y == 2 and Board.board_grid2[3][self.x - 1].piece == "" and Board.board_grid2[self.y][self.x - 1].piece == "":
				Board.valid_squares.append(Board.board_grid2[3][self.x - 1])
			elif self.y == 7:
				pass
			if Board.board_grid2[self.y][self.x - 1].piece == "":
				Board.valid_squares.append(Board.board_grid2[self.y][self.x - 1])
			try:
				if Board.board_grid2[self.y][self.x - 2].piece.startswith("W") and (self.x - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y][self.x - 2])
			except IndexError:
				pass
			try:
				if Board.board_grid2[self.y][self.x - 0].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y][self.x - 0])			
			except IndexError:
				pass
			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def BrookMove(self):
		if Board.first_click == True and Board.blacks_turn == True:
			self.square_button.config(bg = "blue")
			for i in range(self.y, 8):
				if Board.board_grid2[i][self.x - 1].piece == "":
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
				elif Board.board_grid2[i][self.x - 1].piece.startswith("B"):
					break
				elif Board.board_grid2[i][self.x - 1].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
					break
			for i in reversed(range(self.y - 1)):
				if Board.board_grid2[i][self.x - 1].piece == "":
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
				elif Board.board_grid2[i][self.x - 1].piece.startswith("B"):
					break
				elif Board.board_grid2[i][self.x - 1].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
					break
			for i in range(self.x, 8):
				if Board.board_grid2[self.y - 1][i].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
				elif Board.board_grid2[self.y - 1][i].piece.startswith("B"):
					break
				elif Board.board_grid2[self.y - 1][i].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
					break
			for i in reversed(range(self.x - 1)):
				if Board.board_grid2[self.y - 1][i].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
				elif Board.board_grid2[self.y - 1][i].piece.startswith("B"):
					break
				elif Board.board_grid2[self.y - 1][i].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
					break
			Board.piece_last_clicked = self.piece
			Board.higlightValidSquares()
			Board.first_click = False
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()


	def BknightMove(self):
		if Board.first_click == True and Board.blacks_turn == True:
			self.square_button.config(bg = "blue")
			try:
				if (self.y - 2) >= 0 and (self.x - 3) >= 0 and not Board.board_grid2[self.y - 2][self.x - 3].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 3])
			except IndexError:
				pass
			try: 
				if (self.y - 3) >= 0 and (self.x - 2) >= 0 and not Board.board_grid2[self.y - 3][self.x - 2].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 3][self.x - 2])
			except IndexError:
				pass
			try:
				if (self.x - 2) >= 0 and not Board.board_grid2[self.y + 1][self.x - 2].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y + 1][self.x - 2])
			except IndexError:
				pass
			try: 
				if (self.x - 3) >= 0 and not Board.board_grid2[self.y][self.x - 3].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y][self.x - 3])
			except IndexError:
				pass
			try: 
				if not Board.board_grid2[self.y + 1][self.x].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y + 1][self.x])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y][self.x + 1].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y][self.x + 1])
			except IndexError:
				pass
			try: 
				if (self.y - 2) >= 0 and not Board.board_grid2[self.y - 2][self.x + 1].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x + 1])
			except IndexError:
				pass
			try: 
				if (self.y - 3) >= 0 and not Board.board_grid2[self.y - 3][self.x].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 3][self.x])
			except IndexError:
				pass
			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def BbishopMove(self):
		if Board.first_click == True and Board.blacks_turn == True:
			self.square_button.config(bg = "blue")
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp) >= 0 and (self.x - 1 + temp) >= 0:
				if Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp])
				elif Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp].piece.startswith("B"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp])
					break
				temp -= 1
			while (self.y - 1 + temp2) <= 7 and (self.x - 1 + temp2) <= 7:
				if Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2])
				elif Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2].piece.startswith("B"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2])
					break
				temp2 += 1
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp) >= 0 and (self.x - 1 + temp2) <= 7:
				if Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2])
				elif Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2].piece.startswith("B"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2])
					break
				temp -= 1
				temp2 += 1
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp2) <= 7 and (self.x - 1 + temp) >= 0:
				print (10)
				if Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp])
				elif Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp].piece.startswith("B"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp])
					break
				temp2 += 1
				temp -= 1
			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def BqueenMove(self):
		if Board.first_click == True and Board.blacks_turn == True:
			self.square_button.config(bg = "blue")
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp) >= 0 and (self.x - 1 + temp) >= 0:
				if Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp])
				elif Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp].piece.startswith("B"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp])
					break
				temp -= 1
			while (self.y - 1 + temp2) <= 7 and (self.x - 1 + temp2) <= 7:
				if Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2])
				elif Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2].piece.startswith("B"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp2])
					break
				temp2 += 1
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp) >= 0 and (self.x - 1 + temp2) <= 7:
				if Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2])
				elif Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2].piece.startswith("B"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp][self.x - 1 + temp2])
					break
				temp -= 1
				temp2 += 1
			temp = -1
			temp2 = 1
			while (self.y - 1 + temp2) <= 7 and (self.x - 1 + temp) >= 0:
				if Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp])
				elif Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp].piece.startswith("B"):
					break
				else:
					Board.valid_squares.append(Board.board_grid2[self.y - 1 + temp2][self.x - 1 + temp])
					break
				temp2 += 1
				temp -= 1

			for i in range(self.y, 8):
				if Board.board_grid2[i][self.x -1].piece == "":
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
				elif Board.board_grid2[i][self.x -1].piece.startswith("B"):
					break
				elif Board.board_grid2[i][self.x -1].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
					break
			for i in reversed(range(self.y - 1)):
				if Board.board_grid2[i][self.x -1].piece == "":
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
				elif Board.board_grid2[i][self.x -1].piece.startswith("B"):
					break
				elif Board.board_grid2[i][self.x -1].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[i][self.x - 1])
					break
			for i in range(self.x, 8):
				if Board.board_grid2[self.y - 1][i].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
				elif Board.board_grid2[self.y - 1][i].piece.startswith("B"):
					break
				elif Board.board_grid2[self.y - 1][i].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
					break
			for i in reversed(range(self.x - 1)):
				if Board.board_grid2[self.y - 1][i].piece == "":
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
				elif Board.board_grid2[self.y - 1][i].piece.startswith("B"):
					break
				elif Board.board_grid2[self.y - 1][i].piece.startswith("W"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][i])
					break
			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()

	def BkingMove(self):
		if Board.first_click == True and Board.blacks_turn == True:
			self.square_button.config(bg = "blue")
			if Board.Bking_moved == False and Board.H8_rook_moved == False and Board.board_grid2[0][5].piece == "" and Board.board_grid2[0][6].piece == "":
				Board.valid_squares.append(Board.board_grid2[0][6])
			if Board.Bking_moved == False and Board.A8_rook_moved == False and Board.board_grid2[0][1].piece == "" and Board.board_grid2[0][2].piece == "" and Board.board_grid2[0][3].piece == "":
				Board.valid_squares.append(Board.board_grid2[0][2])
			try:	
				if not Board.board_grid2[self.y - 1][self.x - 2].piece.startswith("B") and (self.x - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 1][self.x - 2])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 1][self.x - 0].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 1][self.x - 0])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 2][self.x - 0].piece.startswith("B") and (self.y - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 0])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 2][self.x - 1].piece.startswith("B") and (self.y - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 1])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 2][self.x - 2].piece.startswith("B") and (self.y - 2) >= 0 and (self.x - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 2][self.x - 2])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 0][self.x - 0].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 0][self.x - 0])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 0][self.x - 1].piece.startswith("B"):
					Board.valid_squares.append(Board.board_grid2[self.y - 0][self.x - 1])
			except IndexError:
				pass
			try:
				if not Board.board_grid2[self.y - 0][self.x - 2].piece.startswith("B") and (self.x - 2) >= 0:
					Board.valid_squares.append(Board.board_grid2[self.y - 0][self.x - 2])
			except IndexError:
				pass

			Board.higlightValidSquares()
			Board.first_click = False
			Board.piece_last_clicked = self.piece
			Board.square_last_clicked = Board.board_grid2[self.y - 1][self.x - 1]
		else:
			Board.secondClick()


class ChessPiece:
#	piece_list = ["pawn", "rook", "knight", "bishop", "queen", "king"]

	def move(self):
		pass

	def captured(self, ref, color):
		self.ref_dict = {
			1: Board.pawnCaptured(color),
			2: Board.rookCaptured(color),  # doesn't work # wrong syntax for switch case statement
			3: Board.knightCaptured(color),
			4: Board.bishopCaptured(color),
			5: Board.queenCaptured(color)
		}
		return self.ref_dict.get(ref)

	def __mul__(self, other):             # Method for capturing a piece
		self.rank = other.rank
		self.file = other.rank
		self.captured(other.ref_no, other.colour)


class Pawn(ChessPiece):
	def __init__(self, square, colour):
		Board.empty_square_picture = PhotoImage(file = "Bitmaps\\empty_square.png")
		self.square = square
		self.colour = colour
		if colour == "white":
			self.square.piece = "Wpawn"
			self.picture = PhotoImage(file = "Bitmaps\\Wpawn.png")
		else:
			self.square.piece = "Bpawn"
			self.picture = PhotoImage(file = "Bitmaps\\Bpawn.png")
		self.ref_no = 1
		self.moved = False
		self.square.square_button.config(image = self.picture, width = "60", \
			height = "65")


class Rook(ChessPiece):
	def __init__(self, square, colour):
		self.square = square
		self.colour = colour
		if colour == "white":
			self.square.piece = "Wrook"
			self.picture = PhotoImage(file = "Bitmaps\\Wrook.png")
		else:
			self.square.piece = "Brook"
			self.picture = PhotoImage(file = "Bitmaps\\Brook.png")
		self.ref_no = 2
		self.moved = False
		self.square.square_button.config(image = self.picture, width = "60", \
			height = "65")


class Knight(ChessPiece):
	def __init__(self, square, colour):
		self.square = square
		self.colour = colour
		if colour == "white":
			self.square.piece = "Wknight"
			self.picture = PhotoImage(file = "Bitmaps\\Wknight.png")
		else:
			self.square.piece = "Bknight"
			self.picture = PhotoImage(file = "Bitmaps\\Bknight.png")
		self.ref_no = 3
		self.square.square_button.config(image = self.picture, width = "60", \
			height = "65")


class Bishop(ChessPiece):
	def __init__(self, square, colour):
		self.square = square
		self.colour = colour
		if colour == "white":
			self.square.piece = "Wbishop"
			self.picture = PhotoImage(file = "Bitmaps\\Wbishop.png")
		else:
			self.square.piece = "Bbishop"
			self.picture = PhotoImage(file = "Bitmaps\\Bbishop.png")
		self.ref_no = 4
		self.square.square_button.config(image = self.picture, width = "60", \
			height = "65")


class Queen(ChessPiece):
	def __init__(self, square, colour):
		self.square = square
		self.colour = colour
		if colour == "white":
			self.square.piece = "Wqueen"
			self.picture = PhotoImage(file = "Bitmaps\\Wqueen.png")
		else:
			self.square.piece = "Bqueen"
			self.picture = PhotoImage(file = "Bitmaps\\Bqueen.png")
		self.ref_no = 5
		self.square.square_button.config(image = self.picture, width = "60", \
			height = "65")


class King(ChessPiece):
	def __init__(self, square, colour):
		self.square = square
		self.colour = colour
		if colour == "white":
			self.square.piece = "Wking"
			self.picture = PhotoImage(file = "Bitmaps\\Wking.png")
		else:
			self.square.piece = "Bking"
			self.picture = PhotoImage(file = "Bitmaps\\Bking.png")
		self.moved = False
		self.square.square_button.config(image = self.picture, width = "60", \
			height = "65")


class InitEmptySquare(ChessPiece):
	def __init__(self, square):
		self.square = square
		self.square.piece = ""
		self.picture = PhotoImage(file = "Bitmaps\\empty_square.png")
		self.square.square_button.config(image = self.picture, width = "60", \
			height = "65")