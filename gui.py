import arcade
from solver import solve, valid

WIDTH = 1000
HEIGHT = 1000

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def draw_grid(bo):
    for i in range(len(bo)):
        if i != 0:
            arcade.draw_line(0, HEIGHT/len(bo)*i, WIDTH, HEIGHT/len(bo)*i, arcade.color.BLACK, 4 if i % 3 == 0 else 1)

    for j in range(len(bo[0])):
        if j != 0:
            arcade.draw_line(WIDTH/len(bo[0])*j, 0, WIDTH/len(bo[0])*j, HEIGHT, arcade.color.BLACK, 4 if j % 3 == 0 else 1)


def draw_numbers(bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                    arcade.draw_text(str(bo[i][j]) if bo[i][j] !=0 else "", WIDTH/len(bo[0])*j+35, HEIGHT-HEIGHT/len(bo)*i-90, arcade.color.BLACK, 54)
                    print(str(bo[i][j]))


def main():
    arcade.open_window(WIDTH, HEIGHT, "Sudoku Solver")

    # Set color
    arcade.set_background_color(arcade.csscolor.WHITE)

    # Get ready to draw
    arcade.start_render()

    # Grid
    draw_grid(board)

    # Draw text at (150, 230) with a font size of 24 pts.
    draw_numbers(board)

    # Finish drawing
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()

main()
