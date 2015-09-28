

'''
# = wall
S = start
G = Goal
E = Enerage
C = CheckPoint
'''

def print_maze(maze):
    for i in maze:
        line = ''
        for j in i:
            line += j
        print line

def dfs(curPos,path,maze):
    global resultPath,B,C,E,target  
    #print_maze(maze)
    #print 

    if curPos in target:
        # find the shortest path
        if len(resultPath) == 0 or len(resultPath) > len(path): 
            resultPath = []
            for i in path:
                    resultPath.append(i)
        return

    for v in D: #vector
        newPos = [curPos[0] + v[0],curPos[1] +v[1]]
        if maze[newPos[0]][newPos[1]] not in wall:
            maze[newPos[0]][newPos[1]] = "@"
            dfs(newPos,path+[newPos],maze)
            maze[newPos[0]][newPos[1]] = "."


def pos2vector(path):
    #convert position to vector
    result = ''
    for j in xrange(1,len(path)):
            offset = path[j][0] - path[j-1][0]
            if offset == 0:
                offset = path[j][1] - path[j-1][1]
                if offset > 0:
                    result += 'R'
                else:
                    result += 'L'
            else:
                if offset > 0:
                    result += 'D'
                else:
                    result += 'U'
    return result

wall = ['#','@']
D = [(0,1),(0,-1),(1,0),(-1,0)] # set of vector
f = open('maze.txt','r')
fw = open('result.txt','w')
for i in range(1001):
    maze = []
    resultPath = []
    C = []
    E = []
    target = []
    finalPathVector = ''
    data = f.readline().split(' ')
    print data
    #print data
    for line in xrange(eval(data[1])):
        maze.append(list(f.readline().replace('\n','')))

    print_maze(maze)
    print 
    for x in xrange(eval(data[0])):
        for y in xrange(eval(data[1])):
            #print "x=%d,y=%d" % (x,y)
            if maze[y][x] == 'S':
                S = [y,x]
            if maze[y][x] == 'G':
                G = [y,x]
            if maze[y][x] == 'C':
                C.append([y,x])
            if maze[y][x] == 'E':
                E.append([y,x])

    print 'S' + str(S)
    print 'G' + str(G)
    print 'C' + str(C)
    print 'E' + str(E)

    # achieve all checkpoint
    target = C
    for j in range(len(C)):
        resultPath = []
        maze[S[0]][S[1]] = '#'
        dfs(S,[S],maze)
        maze[S[0]][S[1]] = '.'
        finalPathVector += pos2vector(resultPath)
        # remove the checkpoint that we complete
        target.remove(resultPath[len(resultPath)-1])
        # set next StartPoint
        S = resultPath[len(resultPath)-1]
        # clear all the component on path
        for coor in resultPath:
            maze[coor[0]][coor[1]] = '.'
    
    resultPath = []
    # the Goal
    target = [G]
    maze[S[0]][S[1]] = '#'
    dfs(S,[S],maze)
    print resultPath
    
    finalPathVector += pos2vector(resultPath)

    print finalPathVector
    fw.write(finalPathVector + '\n')
    print '==========================================='

fw.close()
f.close()

#Conglaturations! Your final energy is 3557. ... TMCTF{AMAZING_1001_MAZES_lool}
