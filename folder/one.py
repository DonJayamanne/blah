import chess.uci
from chess import Board

SF = chess.uci.popen_engine('/Users/donjayamanne/Desktop/Development/PythonStuff/Blah/wow')
sample_fen = 'rnb1k2r/pp2pp2/3p3p/2pP2p1/2P1B3/2q3B1/P4PPP/R2Q1KNR b kq - 0 12'

SF.uci()
SF.isready()

board = Board()
board.set_fen(sample_fen)

SF.ucinewgame()a
SF.position(board)

res = SF.go(nodes=50_000)

print(res)

x = f''
