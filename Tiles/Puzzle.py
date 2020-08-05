import random
  

class Puzzle():    
    def __init__(self, dimension=3):
        self._dimension = dimension
        self._size = self._dimension * self._dimension
        self._tiles = []
        for i in range(1, self._size) :
            self._tiles.append(i)
        self._tiles.append(None)
        self._emptySquare = len(self._tiles) - 1
        self._isDebugging = True

    def debug(self, message):
        if self._isDebugging :
            print message

    def display(self):
        for i in range(0, len(self._tiles)) :
            if i % self._dimension == 0 :
                print
            if isinstance(self._tiles[i], int) :
                print ("\t%d\t" % self._tiles[i]),  
            else :
                print ("\t*\t"),      
        print

    def tilesToString(self, tiles):
        toString = ""
        for i in range(0,len(tiles)) :
            if i % self._dimension == 0 :                 
                toString += "\n" 
            toString += "*" if tiles[i] == None else str(tiles[i])
        return toString

    def getMapping(self, swap):
        mapping = ""
        for i in range(0, self._size) :
            mapping += "*" if i == swap else str(self._tiles[swap] if i == self._emptySquare else self._tiles[i])
        return mapping
    
    def getNewPosition(self, puzzle, old, new):
        newPuzzle = puzzle[:]
        newPuzzle[old], newPuzzle[new] = newPuzzle[new],newPuzzle[old]
        return newPuzzle
    
    def getAvailableMoves(self, puzzle):
        emptySquare = puzzle.index(None)
        availableMoves = []   
            
        up = emptySquare - self._dimension
        if (up >=0) :
            availableMoves.append(self.getNewPosition(puzzle, emptySquare, up))
            
        down = emptySquare + self._dimension    
        if (down < self._size) :
            availableMoves.append(self.getNewPosition(puzzle, emptySquare, down))
            
        left = emptySquare - 1    
        if (self._emptySquare % self._dimension > 0) :            
            availableMoves.append(self.getNewPosition(puzzle, emptySquare, left))
            
        right = emptySquare + 1    
        if (right % self._dimension > 0) :            
            availableMoves.append(self.getNewPosition(puzzle, emptySquare, up))

        self.debug("available moves: " + str(availableMoves))
        
        return availableMoves
    
    def shuffle2(self):        
        currentShuffle = self._tiles[:]
        shuffleStack = [currentShuffle[:]]
        
        for i in range(1,10):
            availableMoves = self.getAvailableMoves(currentShuffle)
            for i,newPosition in enumerate(availableMoves) :
                if newPosition in shuffleStack :
                    self.debug("duplicate position, removing " + str(newPosition))
                    availableMoves.remove(newPosition)
            
            if len(availableMoves) :
                currentShuffle = random.choice(availableMoves)
                shuffleStack.append(currentShuffle)
        
        self.debug("shufflestack:  ")
        for i in shuffleStack :
            print(self.tilesToString(i))
    ###################################s    
    
    def shuffle(self, debug=False):
        shuffleStack = [self._tiles[:]]
        #shuffleStack.append()
        if debug:
            print shuffleStack
        
        previousEmpty = -1
        shuffleHistory = [self.getMapping(self._emptySquare)]
        for i in range(0,10) : 
            up = self._emptySquare - self._dimension
            down = self._emptySquare + self._dimension
            left = self._emptySquare - 1
            right = self._emptySquare + 1    
                 
            available = []
            if (up >=0 and up != previousEmpty) :
                upPosition = self.getNewPosition(up)
                if upPosition not in shuffleHistory :
                    print ("adding up:  " + str(upPosition))
                    available.append(upPosition)
                else :
                    print ("up " + str(upPosition) + " is duplicate")
            if (down < self._size and down != previousEmpty) :
                downPosition = self.getNewPosition(down)
                if downPosition not in shuffleHistory :
                    print ("adding down:  " + str(downPosition))
                    available.append(downPosition)
                else :
                    print ("down " + str(downPosition) + " is duplicate")
            if (self._emptySquare % self._dimension > 0 and left != previousEmpty) :
                leftPosition = self.getNewPosition(left)
                if leftPosition not in shuffleHistory :
                    print ("adding left:  " + str(leftPosition))
                    available.append(leftPosition)
                else :
                    print ("left " + str(leftPosition) + " is duplicate")
            if (right % self._dimension > 0 and right != previousEmpty) :
                rightPosition = self.getNewPosition(right)
                if rightPosition not in shuffleHistory :
                    print ("adding rights:  " + str(rightPosition))
                    available.append(rightPosition)
                else :
                    print ("right " + str(rightPosition) + " is duplicate")
                 
            if debug :
                print("Available positions:  " + str(available))
                
            self._tiles = random.choice(available)
            
            if debug :
                print("board updated to " + str(self._tiles))
            #previousEmpty = self._emptySquare
            #newEmpty = random.choice(available)
            #shuffleHistory.append(self.getMapping(newEmpty))
            #print ("previous empty:  %d, new empty:  %d" % (previousEmpty, newEmpty))
            #self._emptySquare = newEmpty
            #self._tiles[previousEmpty] = self._tiles[self._emptySquare]
            #self._tiles[self._emptySquare] = None
            #print ("switch:  %d" % random.choice(available))
            #self.display()
#             for mapping in shuffleHistory :
#                 for i in range(0, len(mapping)):
#                     if (i % self._dimension == 0) :
#                         print
#                     print("\t%s\t" % mapping[i]),
#                 print("\n--------")
                    
        
        
    
    
if __name__ == '__main__' :
    puzzle8 = Puzzle()
    puzzle8.shuffle2()
    puzzle8.display()