
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns

# create discrete colormap
cmap = colors.ListedColormap(['lightgrey', 'white', 'green', 'firebrick', 'blue', 'orangered', 'grey','gold'])
bounds = [b for b in range(0, cmap.N, 1)]
norm = colors.BoundaryNorm(bounds, cmap.N)

def show_cube():
    fig, axs = plt.subplots(3,4)
    for x in range(3):
        for y in range(4):        
            # draw gridlines for faces
            if 4*x+y not in(0,2,3,8,10,11):
                axs[x][y].grid(which='major',  axis='both', linestyle='-', color='k', linewidth=2)
                axs[x][y].set_xticks(np.arange(-.5, 3, 1));
                axs[x][y].set_yticks(np.arange(-.5, 3, 1));
                axs[x][y].imshow(rubik[4*x+y], cmap=cmap, norm=norm)             
            else: # don't draw for empty grid
                axs[x][y].spines['top'].set_visible(False)
                axs[x][y].spines['right'].set_visible(False)
                axs[x][y].spines['bottom'].set_visible(False)
                axs[x][y].spines['left'].set_visible(False)
            #all grids, no ticks, no labels
            axs[x][y].tick_params(axis='both', which='both', length=0)
            #plt.setp(axs[x][y].get_xticklabels(), visible=False)
            #plt.setp(axs[x][y].get_yticklabels(), visible=False)   
            axs[x][y].get_xaxis().set_ticklabels([])
            axs[x][y].get_yaxis().set_ticklabels([])
    plt.show()

face = np.ones((3,3))
zero =face*0
rubik =[zero,face,zero,zero,face*2,face*3,face*4,face*5,zero,face*6,zero,zero]
#rubik[1][0]=[2,2,2]
show_cube()

def convert_cube(cube):
    for i,l in enumerate('xwgrboy'):
        cube = cube.replace(l, str(i))
    cube_list=[int(i) for i in list(cube)]

    up = [cube_list[0:3],cube_list[3:6],cube_list[6:9]]
    left = [cube_list[9:12],cube_list[12:15],cube_list[15:18]]
    front = [cube_list[18:21],cube_list[21:24],cube_list[24:27]]
    right = [cube_list[27:30],cube_list[30:33],cube_list[33:36]]
    back = [cube_list[36:39], cube_list[39:42], cube_list[42:45]]
    down = [cube_list[45:48], cube_list[48:51], cube_list[51:54]]
    
    return [zero,up,zero,zero,left,front,right,back,zero,down,zero,zero]

cube = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'
rubik = convert_cube(cube)
show_cube()