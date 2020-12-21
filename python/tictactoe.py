# INCOMPLETE

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def game_board():
    print("   a  b  c")
    for i, row in enumerate(game):
        print(i, row)
    
    move = input("what move do you want to make?")
