import os
import re
PATH = os.path.join(os.getcwd(), 'day_2\\input.txt')

class Day2_p1:        
    def doTheThing(self):
        count = 0
        with open(PATH, 'r') as f:
            for line in f:
                # chop up the line into rules and limits
                splitLine = line.rstrip().split(': ')
                rules = splitLine[0].split(' ')
                limits = list(map(int, rules[0].split('-')))

                # find all target character matches
                matches = re.findall(rules[1], splitLine[1])

                # make sure the match count is between the bounds
                if limits[0] <= len(matches) and len(matches) <= limits[1]:
                    count += 1
        return count

class Day2_p2:        
    def doTheThing(self):
        count = 0
        with open(PATH, 'r') as f:
            for line in f:
                # chop up the line into password, key character, and positions
                splitLine = line.rstrip().split(': ')
                rules = splitLine[0].split(' ')
                positions = list(map(int, rules[0].split('-')))
                password = splitLine[1]
                
                # check to make sure the password is long enough to begin with
                # then just make sure the booleans are different (ie: T/F, not T/T or F/F)
                if len(password) >= positions[1]:
                    thing1 = password[positions[0] - 1] == rules[1]
                    thing2 = password[positions[1] - 1] == rules[1]
                    if thing1 != thing2:
                        count += 1
        return count

if __name__ == "__main__":
    d2p1 = Day2_p1()
    print(d2p1.doTheThing())

    d2p2 = Day2_p2()
    print(d2p2.doTheThing())
