from constraint import *


########################################
# HW 3 Magic Square Example using Constraint library
#
#######################################

class MS:
    # size = 3

    def __init__(self, size):
        # self.name = name
        self.size = size
        self.pr = Problem(RecursiveBacktrackingSolver())

    def getSolution(self):
        n = self.size

        exact_sum = n * (n ** 2 + 1) / 2
        print(exact_sum)
        # Adding Variables
        self.pr.addVariables(range(0, n ** 2), range(1, (n ** 2) + 1))

        # Adding Constrains
        self.pr.addConstraint(AllDifferentConstraint(), range(n ** 2))

        tl_to_br = [0]
        for i in range(n - 1):
            tl_to_br.append(tl_to_br[i] + n + 1)
        print("TL to BR is", tl_to_br)
        tr_to_bl = [n - 1]
        for i in range(n - 1):
            tr_to_bl.append(tr_to_bl[i] + n - 1)
        print("TR to BL is", tr_to_bl)

        self.pr.addConstraint(ExactSumConstraint(exact_sum), tl_to_br)
        self.pr.addConstraint(ExactSumConstraint(exact_sum), tr_to_bl)

        for row in range(n):
            self.pr.addConstraint(ExactSumConstraint(exact_sum),
                                  [row * n + i for i in range(n)])

        for col in range(n):
            self.pr.addConstraint(ExactSumConstraint(exact_sum),
                                  [col + n * i for i in range(n)])

        # Get solutions
        sols = self.pr.getSolutions()
        print(sols)

        # Loop through solutions
        # Print results
        for s in sols:
            for row in range(3):
                for col in range(3):
                    print(str((s[row * 3 + col])), end='')
                print("")
            print("")


def main():
    MS(4).getSolution()


main()
