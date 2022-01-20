class Centrifuge:
    tubesIn = []

    def __init__(self, numTubes):
        self.numTubes = numTubes

    def add(self, tube):
        if type(tube) == int:
            tube = Tube(data=tube)
        self.tubesIn.append(tube.data)

    def erase(self):
        self.tubesIn = []


class Tube:
    def __init__(self, data):
        self.data = data

# Main function to balance a given number of tubes (numTubesBalance)
def bc(numTubesBalance):
    c = Centrifuge(24)
    c.erase()

    if numTubesBalance % 2 == 0:
        for i in range(numTubesBalance // 2):
            t = Tube(data=i)
            c.add(t)
            c.add(balanceEven(t))

    else:

        num_balanced = 0

        count = 1

        t = Tube(data=0)

        c.add(t)

        for tube in balanceOdd(t):
            c.add(tube)

        while 2 * num_balanced < numTubesBalance - 3:
            if count not in c.tubesIn and balanceEven(count).data not in c.tubesIn:
                c.add(Tube(count))
                c.add(Tube(balanceEven(count).data))
                num_balanced += 1
            count += 1

    if checkBalance(c.tubesIn) == False or len(c.tubesIn) != numTubesBalance or c.numTubes in c.tubesIn:

        return f"A {c.numTubes}-slot centrifuge cannot balance {numTubesBalance} tube(s)!"

    else:
        return c.tubesIn


# Helper function to balance a given #tube with ONE other tube
def balanceEven(given):
    if type(given) == int:
        t = Tube(data=int((given + 12) % 24))
    else:
        t = Tube(data=int((given.data + 12) % 24))

    return t


# Helper function to balance a given #tube with TWO other tubes
def balanceOdd(given):
    tubes = []

    for num in range(2):
        if type(given) == int:
            mod_num = 24 + given
        else:
            mod_num = 24 + given.data

        given = (mod_num + int(21 / 3 + 1)) % 24

        t = Tube(data=given)

        tubes.append(t)

    return tubes


# Function that returns a boolean on whether a given list of tube #s is balanced or not
def checkBalance(given):
    for i in range(len(given)):
        if balanceEven(given[i]).data not in given:
            for q in balanceOdd(given[i]):
                if q.data not in given:
                    return False
    return True


if __name__ == '__main__':

    for num in range(25):
        print(num, bc(num))
