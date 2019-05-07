#-------------------------------------------------------------------------------
# Name:        rubik_crypto2
# Purpose:     use rubik cube scrambling to crypt files
#
# Author:      Jean
#
# Created:     24/04/2019
# Copyright:   (c) Jean 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from cube_face_rotation2 import *


def main():
    setDebug(True)
    gen=True
    if gen :
        encrypt, decrypt = generateKey()
        #print(encrypt,decrypt)
    else:
        encrypt=["F'", 'R', "U'", "R'", 'U', 'U', 'F2', 'Y', "B'", 'U', 'B', 'U', 'F2', 'Y', "R'", "F'", 'U', 'F', 'R', 'U', 'U', 'U', 'F2', 'Y', 'L', 'F', "U'", "F'", "L'", 'U', 'F2', 'Y', "L'", 'U', 'L', "U'", 'R', 'U', "R'", 'Y', "U'", "F'", "U'", 'F', 'Y', 'B', 'U', "B'", 'R', 'U', "R'", 'Y', 'Y', "U'", "L'", 'U', 'L', 'U', 'F', "U'", "F'", 'Y', 'Y', 'U2', 'Y2', 'U', 'R', "U'", "R'", "U'", "F'", 'U', 'F', 'Y', 'Y', 'U', 'R', "U'", "R'", "U'", "F'", 'U', 'F', 'Y', 'F', 'R', 'U', "R'", "U'", "F'", 'U2', 'F', 'R', 'U', "R'", "U'", "F'", 'F', 'R', 'U', "R'", "U'", "F'", 'U', 'U', 'U', 'U', 'R', "U'", "L'", 'U', "R'", "U'", 'L', "R'", "D'", 'R', 'D', "R'", "D'", 'R', 'D', 'U', "R'", "D'", 'R', 'D', "R'", "D'", 'R', 'D', 'U', 'U', "R'", "D'", 'R', 'D', "R'", "D'", 'R', 'D', 'U', 'Y']
        decrypt = ['R', "B'", "R'", 'L', "F'", 'D', 'R', 'D2', 'R2', 'L2', 'F', 'B2', 'U', "D'", 'B2', 'D', 'R2', 'B2', 'U', 'F2', 'B2']
    print(len(encrypt),len(decrypt))
    #crypting
    text2code= 'azertyuiopqsdfghjklmwxcvbn1234567890nbvcxwmlkjhgfdsqpo'
    cubein=text2code 
    sequence=init(cubein)                  #text to encryptr
    #cube_face_rotation2.cubein=cubein
    cubeout, whiteok, layer2 = doSequence(encrypt)             #encrypting
    print(cubein)
    print(cubeout)
    #decypher
    cubein=cubeout
    sequence=init(cubein)                       # text encrypted to decypher
    cubeout, whiteok, layer2 = doSequence(decrypt)
    print(cubein)
    print(cubeout)                                   # original text decyphered


if __name__ == '__main__':
    main()
