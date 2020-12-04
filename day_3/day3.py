import os
PATH = os.path.join(os.getcwd(), 'day_3\\input.txt')

class Day3_p1:
    def doTheThing(self):
        playerPosition = 0
        trees = 0
        with open(PATH, 'r') as f:
            # read line one because we need to know the line length
            # and we don't want to consider the starting line for tree counting
            lineLength = len(f.readline().rstrip())
            # then iterate through the rest of the lines (moving down the slope one step at a time)
            for line in f:
                # advance the player to the right three spaces
                # then mod (%) the player position to loop back to the start of the line if necessary
                # (ie. moving to the next mapt tile to the right)
                playerPosition = (3 + playerPosition) % lineLength
                # check for trees
                if line[playerPosition] == '#':
                    trees += 1
        return trees


class Day3_p2:
    def doTheThingTweakedFromPart1(self, rightRate, downRate):
        playerPosition = 0
        trees = 0
        with open(PATH, 'r') as f:
            lineLength = len(f.readline().rstrip())
            for line in f:
                # this time the right movement rate comes from the function call
                playerPosition = (rightRate + playerPosition) % lineLength
                # and we can skip extra lines based on the downrate
                # starting at 1 because of how numbers work
                for downMovement in range(1, downRate):
                    line = f.readline()

                if line[playerPosition] == '#':
                    trees += 1
        return trees
    
    def doTheThing(self):
        arrayOfSlopes = [1, 3, 5, 7]
        result = 1
        # do all the 1 down slopes
        for slope in arrayOfSlopes:
            result *= self.doTheThingTweakedFromPart1(slope, 1)
        # then do the 2 down slope
        result *= self.doTheThingTweakedFromPart1(1, 2)
        return result
        

if __name__ == "__main__":
    d3p1 = Day3_p1()
    print(d3p1.doTheThing())

    d3p2 = Day3_p2()
    print(d3p2.doTheThing())
