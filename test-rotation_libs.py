#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:        Rubik's cube Rotation study versiom 0.1
Purpose:
Created on Tue May  7 10:23:20 2019

@author: jeandavid
"""
#-------------------------------------------------------------------------------
from cube_face_rotation2 import *

setDebug(True)      #if True verbose run

print('Test : Do Superflip once')
#test sequence superflip une fois 
cubein=goodcube                      #initialize cube
sequence=init(cubein,'Superflip')
#print(sequence)   
cubeout, whiteOK, layer2 = doSequence(sequence)
printcube(cubein)
printcube(cubeout)

print('Test : Do Superflip twice')
#test sequence superflip 2eme fois
cubein=cubeout
sequence=init(cubein,'Superflip')
cubeout, whiteOK, layer2 = doSequence(sequence)
printcube(cubein)
printcube(cubeout)
#on retouve goodcube

# test degre
print('Test : Degree of a sequence')
cubein=goodcube
sequence=init(cubein)         #dummy sequence
sequence=("R'","D'","R","D")   # execute 6 fois on retrouve goodcube
if sequence!='':
    for i in range(6):
        print(i+1,'times')
        cubeout, whiteOK, layer2 = doSequence(sequence)
        printcube(cubein)
        printcube(cubeout)
        cubein=cubeout
        init(cubein)
else:
    print('Please enter a sequence !')
