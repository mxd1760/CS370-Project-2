import matplotlib.pyplot as plt

import numpy as np
from TreasureMaze import TreasureMaze

def show(qmaze):
    plt.grid('on')
    nrows, ncols = qmaze.maze.shape
    ax = plt.gca()
    ax.set_xticks(np.arange(0.5, nrows, 1))
    ax.set_yticks(np.arange(0.5, ncols, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    canvas = np.copy(qmaze.maze)
    for row,col in qmaze.visited:
        canvas[row,col] = 0.6
    pirate_row, pirate_col, _ = qmaze.state
    canvas[pirate_row, pirate_col] = 0.3   # pirate cell
    canvas[nrows-1, ncols-1] = 0.9 # treasure cell
    img = plt.imshow(canvas, interpolation='none', cmap='gray')
    return img

maze = np.array([
    [ 1.,  0.,  1.,  1.,  1.,  1.,  1.,  1.],
    [ 1.,  0.,  1.,  1.,  1.,  0.,  1.,  1.],
    [ 1.,  1.,  1.,  1.,  0.,  1.,  0.,  1.],
    [ 1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.],
    [ 1.,  1.,  0.,  1.,  1.,  1.,  1.,  1.],
    [ 1.,  1.,  1.,  0.,  1.,  0.,  0.,  0.],
    [ 1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.],
    [ 1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.]
])


qmaze = TreasureMaze(maze)


def poll_actions():
   print("Actions: ")
   print(" 1 - move up")
   print(" 2 - move down")
   print(" 3 - move left")
   print(" 4 - move right")
   print(" 5 - reset")
   print(" 6 - quit")
   return int(input(" --> "))

if __name__=="__main__":
    while True:
        action = poll_actions()
        match action:
          case 1: #move up
            print(qmaze.act(1))
          case 2: #move down
            print(qmaze.act(3))
          case 3: #move left
            print(qmaze.act(0))
          case 4: 
            print(qmaze.act(2))
          case 5:
            print(qmaze.reset({0,0}))
          case 6: 
            break
        show(qmaze)
        plt.show()
            