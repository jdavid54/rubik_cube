# rubik_cube
---------cube_face rotation.py 

show cube state

a study of how to display the cube faces following a sequence of the face rotations

inspired from https://ruwix.com/the-rubiks-cube/mathematics-of-the-rubiks-cube-permutation-group/

<img src="https://github.com/jdavid54/rubik_cube/mathematics-permutation-group.jpg">

--------rubik-solver01.py (need rubik_solver repo)

Enter the cube configuration as a string cubin='wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'

the programm will compute the sequence of moves for 3 methods : Beginner, CFOP and Kociemba to solve the cube

and give the time of computation for each method

--------rubik_crypting.py & cube_face_rotation.py (need rubik_solver repo)

A proposition to encrypt text file using rubik cube sequence of scrambling 

we choose a sequence of scrambling the text (which gives the encrypt key for a string of 54-letters long)

then using kociembo solver to get the decrypt sequence (which gives the decypher key)

the complete text to be encrypted must be split into strings of 54 lettres to be treated sequentially 


