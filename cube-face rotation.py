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

indexes = {'F':((7,8,9,28,31,34,48,47,46,18,15,12),(19,20,21,24,27,26,25,22)), \
           'R':((27,24,21,9,6,3,37,40,43,54,51,48),(34,31,28,29,30,33,36,35)), \
           'L':((19,22,25,46,49,52,45,42,39,1,4,7),(12,15,18,17,16,13,10,11)), \
           'U':((21,20,19,12,11,10,39,38,37,30,29,28),(9,8,7,4,1,2,3,6)), \
           'D':((25,26,27,34,35,36,43,44,45,16,17,18),(46,47,48,51,54,53,52,49)), \
           'B':((3,2,1,10,13,16,52,53,54,36,33,30),(37,38,39,42,45,44,43,40)), \
           'E':((22,23,24,31,32,33,40,41,42,13,14,15),())\
}

colorzone={'y':(0,9), 'b':(9,18), 'r':(18,27), 'g':(27,36), 'o':(36,45), 'w':(45,54)}

def fullfaceOK(c):
    z=colorzone[c]
    n=cube_list[z[0]:z[1]].count(c)
    if n==9: 
        print('Face',c,'full',z,cube_list[z[0]:z[1]])
    else:
        print('Face',c,'corrupted',z,cube_list[z[0]:z[1]])

def cubestate():
    for c in ('ybrgow'):
        fullfaceOK(c)    

def rotation(face):
    for k in (0,1):                 #0:adjacent edges, 1:face
        tampon=[]
        #print(face,k)
        index=indexes[face[0]][k]
        for i in index:
            tampon.append(cube_list[i-1])
        #print(tampon)
        if '\'' not in face :                      #clockwise
            tampon=tampon[-3+k:]+tampon[0:-3+k]
            if '2' in face :
                tampon=tampon[-3+k:]+tampon[0:-3+k]
        else:                                      #counterclock
            tampon=tampon[3-k:]+tampon[0:3-k]
            if '2' in face :
                tampon=tampon[3-k:]+tampon[0:3-k]
        m=0
        for i in index:
            cube_list[i-1]=tampon[m]
            m+=1
        #print(tampon)

def whitecrossOK():
    for k in (47,49,51,53):
        if 'w' != cube_list[k-1]:
            return False
    return True
def whitefaceOK():
    for k in range(46,55):
        if 'w' != cube_list[k-1]:
            return False
    return True
def secondlayerOK():
    for k in (13, 22, 31, 40):
        if cube_list[k] != cube_list[k-1] or cube_list[k] != cube_list[k+1] :
            return False
    return True

def doSequence(seq):
    s=0
    layer2='second layer not complete'
    whiteOK = 'white face never complete'
    for f in seq:
        s+=1
        print('\n',s,'-rotation ',f)
        if 'Y' in f and '\'' not in f:
            for k in ("E'","U","D'"):         # Y is equivalent to 3 horizontal rotations mid, up and down layers
                rotation(k)                     # turn all the cube front to left keeping yellow as up and white as down
            if '2' in f:
                for k in ("E'","U","D'"):         # Y2 is Y, Y
                    rotation(k)
        elif 'Y\'' in f:
            for k in ("E","U'","D"):           # Y' the reverse turn all the cube front to right
                rotation(k)
            if '2' in f:
                for k in ("E","U'","D"):       # twice if Y'2
                    rotation(k)
        else:
            rotation(f)
        cube2=''
        if whitecrossOK(): print("white cross OK")
        if whitefaceOK():
            print("white face complete")
            whiteOK='white face complete'
        if secondlayerOK():
            print("second layer complete")
            layer2='second layer complete'
        for i in cube_list:
            cube2+=i
        printcube(cube2)
        cubestate()
    return cube2, whiteOK, layer2

def printcube(cube):
    # print up face (yellow)
    print('   ',cube[0:3])
    print('   ',cube[3:6])
    print('   ',cube[6:9])
    # print 4 lateral faces (blue, red, green, orange)
    print(cube[9:12],cube[18:21],cube[27:30],cube[36:39])
    print(cube[12:15],cube[21:24],cube[30:33],cube[39:42])
    print(cube[15:18],cube[24:27],cube[33:36],cube[42:45])
    #print down face (white)
    print('   ',cube[45:48])
    print('   ',cube[48:51])
    print('   ',cube[51:54])
    
def printresult():
    print('Solver method :',method)
    print('Cube in :')
    print(cubein)
    print('Cube out :')
    print(cubeout)
    print(cubeout==goodcube)
    print(whiteOK)
    print(layer2)
    print(finalface)

def fff(t):
    n=t.count('Y')
    m=t.count('Y\'')
    p=t.count('Y2')
    return ("final face "+"rgob"[(n-2*m+p)%4],n,m,p)
    
    
cubein = 'wowgybwyogygybyoggrowbrgywrborwggybrbwororbwborgowryby'
goodcube = 'yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww'
method='CFOP'
finalface=''

cube_list=list(cubein)
#face='R'
#sequence-test=('F','F\'','R','R\'','L','L\'','U','U\'','D','D\'','B','B\'')
#test rotation Y
##sequence=("Y",)
if method == 'CFOP':        # cross (C), first two layers (F2L), orient last layer (OLL), permute last layer (PLL)
    # méthode CFOP      F=         g                   o                                b                       31  r
    text="F', R, U', R', U, U, F2, Y, B', U, B, U, F2, Y, R', F', U, F, R, U, U, U, F2, Y, L, F, U', F', L', U, F2, Y"
    #                                                 g     r                                           g  o
    text+=", L', U, L, U', U, F', U, F, U, F', U2, F, Y, U, Y', R', U', R, U2, R', U', R, U, R', U', R, Y, Y"
    #                                              b                                 r  g
    text+=", B, U, B', U, F', U2, F, U, F', U2, F, Y, U2, U', R, U, R', U, R, U, R', Y, Y"     #second layer complete at green in front
    #
    text+=", R', F, R, U, R', F', R"
    #        o                b  r  g  o     b  r  g  o     b  r
    text+=", Y, L, U', L', U, Y, Y, Y, Y, U, Y, Y, Y, Y, U, Y, Y"
    text+=", R, U', R, U, R, U, R, U', R', U', R2"
    finalface=fff(text)
    liste=text.split(', ')
    sequence=liste    #avec rotation Y

if method == 'Beginner':
    # méthode Beginner                                                                                          31 at F2 cross done
    text="F', R, U', R', U, U, F2, Y, B', U, B, U, F2, Y, R', F', U, F, R, U, U, U, F2, Y, L, F, U', F', L', U, F2, Y, L', U, L, U'"
    text+=", R, U, R', Y, U', F', U', F, Y, B, U, B', R, U, R', Y, Y"
    ##ygoyyrrbyobyybrbbbbrrgrbrrrgybogggggyygoooooowwwwwwwww
    #cubein = 'ygoyyrrbyobyybrbbbbrrgrbrrrgybogggggyygoooooowwwwwwwww'
    #cube_list=list(cubein)
    #                      rotation 61
    text+=", U', L', U, L, U, F, U', F', Y, Y, U2, Y2, U, R, U', R', U', F', U, F, Y, Y, U, R, U', R', U', F', U, F, Y, F, R, U, R', U', F', U2, F, R, U, R', U', F', F, R, U, R', U', F', U, U, U, U"
    text+=", R, U', L', U, R', U', L, R', D', R, D, R', D', R, D, U, R', D', R, D, R', D', R, D, U, U, R', D', R, D, R', D', R, D, U"
    finalface=fff(text)
    liste=text.split(', ')
    sequence=liste    #avec rotation Y


if method == 'Kaciemba':
    #méthode Kaciemba
    sequence=("L'","F","B2","R'","B","R'","L","B","D'","F'","U","B2","U","F2","D'","R2","L2","U","F2","D'")
    #reverse=("D","F'2","U'","L'2","R'2","D","F'2","U'","B'2","U'","F","D","B'","L'","R","B'","R","B'2","F'","L")
    finalface=fff(text)
    
cubeout, whiteOK, layer2 = doSequence(sequence)

printresult()




