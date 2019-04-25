#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     24/04/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from rubik_solver import utils
import time

methods=['Beginner', 'CFOP', 'Kociemba']
cube = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'

for m in methods:
    print('Start process :',m)
    start = time.time()
    solution = utils.solve(cube, m)
    end = time.time()
    print('Time of process :',end - start,'s')
    print(solution)


def main():
    pass

if __name__ == '__main__':
    main()
