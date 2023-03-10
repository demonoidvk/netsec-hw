#testing
import numpy as np
from tree import Tree, Node
from Tetris_Board import Board
from Tetris_Piece import PieceSet, Piece

from flask import *

#imports that might be needed in the future:

#from flask_cors import CORS, cross_origin
#import requests, json

app = Flask(__name__)
#CORS(app)


@app.route('/')
def index():
	return render_template('tetris-svg.html')

@app.route('/test', methods=['GET'])
def test():
	b = np.matrix([
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0,0,0],
	[1,1,1,1,0,1,1,1,1,1],
	[1,1,1,1,1,1,0,1,1,1]
	])


	#initialisation
	board = Board(b)
	root = Node([], 1, board)
	tree = Tree(root)


	board.print_board()

	square = PieceSet(1)

	move = board.best_move(square)

	return str(move)


@app.route('/tetris-ai', methods=['POST'])
def calculate_best_move():
	
	req = request.form

	board_status = req["board"]
	piece_num = int(req["piece"])

	#convert string of 0s and 1s to matrix
	matrix = []
	for x in range(20):
		row = list(board_status[x*9:x*9+10])
		row = [int(x) for x in row]
		matrix.append(row)

	board = Board(matrix)

	piece = PieceSet(piece_num)

	best_board = board.best_move(piece)
	
	moves = best_board.moves
	rotations = best_board.latest_piece.rotation

	res = {'moves': moves, 'rotations':rotations}

	return jsonify(res)


if __name__ == '__main__':
	app.run(host = '192.168.25.190', port = 4040 ,debug = True)





