# rubik_cube
## Cube face rotation 

 * [`Face rotation`](/cube-facerotation.py)

show cube state

a study of how to display the cube faces following a sequence of the face rotations

inspired from https://ruwix.com/the-rubiks-cube/mathematics-of-the-rubiks-cube-permutation-group/

[<img src=/mathematics-permutation-group.jpg />](https://ruwix.com/the-rubiks-cube/mathematics-of-the-rubiks-cube-permutation-group/)

## Solving the cube (need rubik_solver repo)

 * [`3 methods for Rubik's cube solving`](/rubik_solver01.py)

Enter the cube configuration as a string cubin='wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'

the programm will compute the sequence of moves for 3 methods : Beginner, CFOP and Kociemba to solve the cube

and give the time of computation for each method

## Encryption & decyphering using rotations (need rubik_solver repo)

 * [`Rubik rotation for encrypting`](/rubik_crypting.py)
 * [`Encryption & decyphering libraries`](/cube_face_rotation.py)

A proposition to encrypt text file using rubik cube sequence of scrambling 

we choose a sequence of scrambling the text (which gives the encrypt key for a string of 54-letters long)

then using kociembo solver to get the decrypt sequence (which gives the decypher key)

the complete text to be encrypted must be split into strings of 54 lettres to be treated sequentially 


