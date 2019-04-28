#-------------------------------------------------------------------------------
# Name:        rubik_crypto
# Purpose:     use rubik cube scrambling to crypt files
#
# Author:      Jean
#
# Created:     24/04/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from rubik_solver import utils
import cube_face_rotation
#from cube_face_rotation import *
import time

methods=['Beginner', 'CFOP', 'Kociemba']

def solve_all(cube):
    for m in methods:
        print('Start process :',m)
        start = time.time()
        solution = utils.solve(cube, m)
        end = time.time()
        print('Time of process :',end - start,'s')
        print(solution)

def kociemba(cube):
    solution = utils.solve(cube, 'Kociemba')
    s=str(solution)
    s=s.replace('[','')
    s=s.replace(']','')

    liste=s.split(', ')
    return liste

def generateKey():
    # a faire une seule fois
    goodcube = 'yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww'
    cubein=goodcube
    method='Beginner'
    # sequence pour encryptage
    encrypt = cube_face_rotation.sequence_def(method)     # choose a sequence to scramble the cube
    print(encrypt)
    cube_face_rotation.cubein=cubein
    cubeout = cube_face_rotation.doSequence(encrypt)     # on mélange le cube avec une séquence personnelle encrypt
    print(cubein)
    print(cubeout)
    decrypt = kociemba(cubeout)        # on cherche la solution Kociemba  decrypt qui servira pour le décryptage
    print(decrypt)
    return encrypt, decrypt


def main():
    #cube = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'
    #cube= 'wyrbybwbgoroybggwogorwrogwrwybggbbrbwrbwogoyyyryowgroy'

    text2code= 'azertyuiopqsdfghjklmwxcvbn1234567890nbvcxwmlkjhgfdsqpo'

    #encrypt, decrypt = generateKey()

    #crypting
    encrypt=["F'", 'R', "U'", "R'", 'U', 'U', 'F2', 'Y', "B'", 'U', 'B', 'U', 'F2', 'Y', "R'", "F'", 'U', 'F', 'R', 'U', 'U', 'U', 'F2', 'Y', 'L', 'F', "U'", "F'", "L'", 'U', 'F2', 'Y', "L'", 'U', 'L', "U'", 'R', 'U', "R'", 'Y', "U'", "F'", "U'", 'F', 'Y', 'B', 'U', "B'", 'R', 'U', "R'", 'Y', 'Y', "U'", "L'", 'U', 'L', 'U', 'F', "U'", "F'", 'Y', 'Y', 'U2', 'Y2', 'U', 'R', "U'", "R'", "U'", "F'", 'U', 'F', 'Y', 'Y', 'U', 'R', "U'", "R'", "U'", "F'", 'U', 'F', 'Y', 'F', 'R', 'U', "R'", "U'", "F'", 'U2', 'F', 'R', 'U', "R'", "U'", "F'", 'F', 'R', 'U', "R'", "U'", "F'", 'U', 'U', 'U', 'U', 'R', "U'", "L'", 'U', "R'", "U'", 'L', "R'", "D'", 'R', 'D', "R'", "D'", 'R', 'D', 'U', "R'", "D'", 'R', 'D', "R'", "D'", 'R', 'D', 'U', 'U', "R'", "D'", 'R', 'D', "R'", "D'", 'R', 'D', 'U', 'Y']
    decrypt = ['R', "B'", "R'", 'L', "F'", 'D', 'R', 'D2', 'R2', 'L2', 'F', 'B2', 'U', "D'", 'B2', 'D', 'R2', 'B2', 'U', 'F2', 'B2']
    cubein=text2code                                             #text to encryptr
    cube_face_rotation.cubein=cubein
    cubeout = cube_face_rotation.doSequence(encrypt)             #encrypting
    print(cubein)
    print(cubeout)
    #decypher
    cubein=cubeout
    cube_face_rotation.cubein=cubein                       # text encrypted to decypher
    cubeout = cube_face_rotation.doSequence(decrypt)
    print(cubein)
    print(cubeout)                                   # original text decyphered


if __name__ == '__main__':
    main()
