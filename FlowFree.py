import time

class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.startValue = False

class Puzzle:
    # Variables: Nodes in the puzzle
    # Domain: List of starting colors, ie [(, colors)]
    # Constraints: Each variable can be only one color, all variables of the
    # same color must be connected either vertically or horizontally, all variables
    # must have a color, for none start nodes at most two connected nodes can be
    # the same color

    def __init__(self, filename):
        self.startingValues = []
        self.colList = []
        self.colsInMaze = 0
        self.rowsInMaze = 0
        self.colors = set()
        self.emptyNodes = 0
        self.numAssignments = 0
        self.runTime = 0.0
        self.endPoints = []

        puzzleObject = open(filename, 'r')
        rows = 0

        for line in puzzleObject:
            rowList = []
            cols = 0

            for char in line[:-1]:
                node = Node(rows, cols, char)

                if char != '_':
                    node.startValue = True
                    self.colors.add(char)
                    self.endPoints.append(node)
                else:
                    self.emptyNodes += 1

                rowList.append(node)

                cols += 1

            rows += 1

            self.colList.append(rowList)
            self.colsInMaze = len(rowList)

        self.rowsInMaze = rows

    def printPuzzle(self):
        for row in self.colList:
            line = ""
            for node in row:
                line += node.value
            print(line)

    def btAlgorithm(self):
        startTime = time.time()
        #print("Starting backtracking...")
        #print(self.colors)
        if self.goalTest():
            #print("Goal Found")
            endTime = time.time()
            self.runTime = endTime - startTime
            return True

        nextNode = self.getUnassignedNode()
        if nextNode == None:
            #print("No Nodes")
            return None
        else:
            #print(str(nextNode.row) + "," + str(nextNode.col))
            pass
        for color in self.colors:
            #print("Checking color: " + color)
            if self.meetsContraints(nextNode, color):
                self.numAssignments += 1
                nextNode.value = color
                self.emptyNodes -= 1
                #self.printPuzzle()
                #input("Press Enter to continue")
                currentState = self.btAlgorithm()
                if currentState != None:
                    return currentState
                else:
                    nextNode.value = '_'
                    self.emptyNodes += 1
        return None

    def smartBtAlgorithm(self):
        startTime = time.time()
        #print("Starting backtracking...")
        #print(self.colors)
        if self.goalTest():
            #print("Goal Found")
            endTime = time.time()
            self.runTime = endTime - startTime
            return True

        nextNode = self.getUnassignedNode()
        if nextNode == None:
            #print("No Nodes")
            return None
        else:
            #print(str(nextNode.row) + "," + str(nextNode.col))
            pass
        for color in self.colors:
            #print("Checking color: " + color)
            if self.meetsSmartContraints(nextNode, color):
                self.numAssignments += 1
                nextNode.value = color
                self.emptyNodes -= 1
                #self.printPuzzle()
                #input("Press Enter to continue")
                currentState = self.smartBtAlgorithm()
                if currentState != None:
                    return currentState
                else:
                    nextNode.value = '_'
                    self.emptyNodes += 1
        return None

    def getUnassignedNode(self):
        for row in self.colList:
            for node in row:
                if node.value == '_':
                    return node
        return None

    def getAdjacentNodes(self, node):
        adjacentNodes = []

        # Top Node
        if node.row > 0:
            adjacentNodes.append(self.colList[node.row - 1][node.col])
        # Bottom Node
        if node.row < self.rowsInMaze - 1:
            adjacentNodes.append(self.colList[node.row + 1][node.col])
        # Left Node
        if node.col > 0:
            adjacentNodes.append(self.colList[node.row][node.col - 1])
        # Right Node
        if node.col < self.colsInMaze - 1:
            adjacentNodes.append(self.colList[node.row][node.col + 1])

        return adjacentNodes

    def meetsContraints(self, node, color):
        # Check to make sure node does not already contain a color
        if node.value != '_':
            #print("Failed Constraint: Node already has a value")
            return False

        adjacentNodes = self.getAdjacentNodes(node)

        # Check to make sure node is not Isolated
        matchingColorNodes = 0
        for otherNode in adjacentNodes:
            if otherNode.value == '_' or otherNode.value == color:
                matchingColorNodes += 1
        if matchingColorNodes == 0:
            #print("Failed Constraint: No matching adjacent nodes")
            return False

        # Check for zig-zag pattern on non-start nodes
        for otherNode in adjacentNodes:
            matchingColorNodes = 0
            if otherNode.startValue == False:
                otherAdjacentNodes = self.getAdjacentNodes(otherNode)
                for otherAdjNode in otherAdjacentNodes:
                    if otherAdjNode.value == color:
                        matchingColorNodes += 1
                if matchingColorNodes >= 2:
                    #print("Failed Constraint: Zig-zag pattern")
                    return False

        # All contraints pass
        return True

    def meetsSmartContraints(self, node, color):
        # Check to make sure node does not already contain a color
        if node.value != '_':
            #print("Failed Constraint: Node already has a value")
            return False

        adjacentNodes = self.getAdjacentNodes(node)

        # Check to make sure node is not isolating an adjacent node
        for otherNode in adjacentNodes:
            if otherNode.value != '_':
                matchingColorNodes = 0
                otherAdjacentNodes = self.getAdjacentNodes(otherNode)
                for otherAdjNode in otherAdjacentNodes:
                    if otherAdjNode.value == otherNode.value or otherAdjNode.value == '_':
                        matchingColorNodes += 1
                    if otherNode.value == color:
                        matchingColorNodes += 1
                if otherNode.startValue:
                    if matchingColorNodes <= 1:
                        #print("Failed Constraint: Isolated starting node: " + str(otherNode.row) + "," + str(otherNode.col))
                        return False
                else:
                    if matchingColorNodes <= 2:
                        #print("Failed Constraint: Isolated non-starting node: " + str(otherNode.row) + "," + str(otherNode.col))
                        return False

        # Check to make sure node is not Isolated
        matchingColorNodes = 0
        for otherNode in adjacentNodes:
            if otherNode.value == '_' or otherNode.value == color:
                matchingColorNodes += 1
        if matchingColorNodes == 0:
            #print("Failed Constraint: No matching adjacent nodes")
            return False

        # Check for zig-zag pattern on non-start nodes
        for otherNode in adjacentNodes:
            matchingColorNodes = 0
            if otherNode.startValue == False:
                otherAdjacentNodes = self.getAdjacentNodes(otherNode)
                for otherAdjNode in otherAdjacentNodes:
                    if otherAdjNode.value == color:
                        matchingColorNodes += 1
                if matchingColorNodes >= 2:
                    #print("Failed Constraint: Zig-zag pattern")
                    return False

        # All contraints pass
        return True

    def goalTest(self):
        #condition = True
        #for node in self.endPoints:
            #print("Color: " + node.value)
            #if self.goalsMet(node) == False:
                #condition = False
                #print("Failed")
                #break
            #print("Success")
        #self.printPuzzle()
        #input("Press Enter to continue")
        if self.emptyNodes == 0:
            self.printPuzzle()
            return True
        else:
            return False

    def goalsMet(self, startNode):
        adjacentNodes = self.getAdjacentNodes(startNode)
        #print("Starting Node: " + str(startNode.row) + "," + str(startNode.col) + " - " + startNode.value)
        for adjacentNode in adjacentNodes:
            #print("Adjacent Node: " + str(adjacentNode.row) + "," + str(adjacentNode.col) + " - " + adjacentNode.value)
            #input("Press Enter to continue")
            if adjacentNode.value == startNode.value and adjacentNode.startValue == True:
                return True
            elif adjacentNode.value == startNode.value:
                return self.goalsMet(adjacentNode)
        return False
