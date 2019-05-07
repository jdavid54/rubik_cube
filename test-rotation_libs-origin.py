#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:34:47 2019

@author: jeandavid
"""
#-------------------------------------------------------------------------------
from cube_face_rotation import *
#import cube_face_rotation 

#face='R'
#cubeout = doSequence("F")        #test rotation F
#sequence-test=('F','F\'','R','R\'','L','L\'','U','U\'','D','D\'','B','B\'')
#test rotation Y
#sequence=("Y",)    # la virgule a la fin compte

scrambledcube='wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'
goodcube = 'yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww'
cubein = goodcube
cubein = scrambledcube
init(cubein)            #passage du parametre cubein et creation de cube_list
method = 'Beginner'
#cube_list=list(cubein)
sequence = getSequence(method)
cubeout = doSequence(sequence)

print(cubein)
print(cubeout)
print(cubeout==goodcube)