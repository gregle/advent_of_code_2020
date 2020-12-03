import os
PATH = os.path.join(os.getcwd(), 'day_1\\input.txt')

class Day1_p1:
    def doTheThing(self):
        dic = {}
        with open(PATH, 'r') as f:
            for line in f:
                val = int(line)
                difference = 2020 - val
                if val in dic:
                    return val * difference
                else:
                    dic[difference] = val

class Day1_p2:
    def doTheThing(self):
        summations = {}
        seenDigis = []

        with open(PATH, 'r') as f:
            for line in f:
                newVal = int(line)
                neededSummation = 2020 - newVal

                if neededSummation in summations:
                    v1 = summations[neededSummation]
                    v2 = newVal
                    v3 = (2020 - (v1 + v2))
                    return v1 * v2 * v3
                else:
                    for digi in seenDigis:
                        # ignore anything that's already busted
                        if (digi + newVal) < 2020:
                            summations[digi + newVal] = digi
                    seenDigis.append(newVal)

if __name__ == "__main__":
    d1p1 = Day1_p1()
    print(d1p1.doTheThing())

    d1p2 = Day1_p2()
    print(d1p2.doTheThing())
