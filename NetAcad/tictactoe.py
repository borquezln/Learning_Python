from random import randrange
import time

def DisplayBoard(board):    # la función lee el tablero y lo dibuja
    for i in range(3):
        print("+-------"*3, "+", sep="")
        for j in range(3):
            print("|  ", board[i][j], "  ", end="")
        print("|")
    print("+-------"*3, "+", sep="")
#----------------------------------------------------------------------------------------------------
def EnterMove(board):   # la función lee el tablero, pide el movimiento y actualiza el tablero
    while True:
        jugada = int(input("Ingrese un número para jugar: "))
        libres = MakeListOfFreeFields(board)
        for item in libres:
            i = item[0]
            j = item[1]
            if board[i][j] == jugada:
                board[i][j] = "O"
                return
#----------------------------------------------------------------------------------------------------
def MakeListOfFreeFields(board):    # la función examina el tablero y construye una lista de todos los cuadros vacíos 
    valor = 1
    libres = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == valor:
                libre = (i, j)
                libres.append(libre)
            valor += 1
    return libres
#----------------------------------------------------------------------------------------------------
def VictoryFor(board, sign):    # la función lee el tablero para verificar si alguien ganó
    for i in range(3):  #lectura de filas
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True

    for i in range(3):  #lectura de columnas
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True

    #lectura de diagonales
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return True
#----------------------------------------------------------------------------------------------------
def DrawMove(board):    # la función dibuja el movimiento de la maquina y actualiza el tablero
    print("Juega la máquina")
    while True:
        jugada = randrange(1,10)   # Instrucción para que juegue la PC
        libres = MakeListOfFreeFields(board)
        for item in libres:
            i = item[0]
            j = item[1]
            if board[i][j] == jugada:
                board[i][j] = "X"
                return
#----------------------------------------------------------------------------------------------------
board = [[1,2,3],[4,5,6],[7,8,9]]
movs = 0
print("Comienza el juego")
DisplayBoard(board)
while True:
    if movs == 9:
        print("Empate")
        break

    elif not movs%2:
        DrawMove(board)
        DisplayBoard(board)
        if VictoryFor(board, "X"):
            print("¡Ha ganado la máquina!")
            time.sleep(5)
            break
        else:
            movs += 1
    
    else:
        EnterMove(board)
        DisplayBoard(board)
        if VictoryFor(board, "O"):
            print("¡Ha ganado el usuario!")
            time.sleep(5)
            break
        else:
            movs += 1
