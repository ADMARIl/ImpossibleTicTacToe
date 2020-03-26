from constraint import *


########################################
# HW 3 Magic Square Example using Constraint library
#
#######################################

class MS:

    def __init__(self, size):
        # self.name = name
        self.size = size
        self.pr = Problem()

    def getSolution(self):
        n = self.size

        exact_sum = n * (n ** 2 + 1) / 2
        # print(exact_sum)
        # Adding Variables
        self.pr.addVariables(range(0, n ** 2), range(1, (n ** 2) + 1))

        # Adding Constrains
        self.pr.addConstraint(AllDifferentConstraint(), range(n ** 2))

        tl_to_br = [0]
        for i in range(n - 1):
            tl_to_br.append(tl_to_br[i] + n + 1)
        # print("TL to BR is", tl_to_br)

        tr_to_bl = [n - 1]
        for i in range(n - 1):
            tr_to_bl.append(tr_to_bl[i] + n - 1)
        # print("TR to BL is", tr_to_bl)

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
            for row in range(n):
                for col in range(n):
                    print(str((s[row * n + col])), end=' ')
                print("")
            print("")


if __name__ == "__main__":
    """
    some_sols = [
        {0: 1, 3: 4, 5: 6, 6: 7, 9: 9, 12: 14, 10: 12, 15: 15, 13: 3, 14: 2, 2: 13, 7: 10, 11: 5, 8: 8, 4: 11, 1: 16},
        {0: 1, 3: 4, 5: 6, 6: 7, 9: 10, 12: 13, 10: 11, 15: 16, 13: 3, 14: 2, 8: 8, 11: 5, 7: 9, 4: 12, 2: 14, 1: 15},
        {0: 1, 3: 4, 5: 7, 6: 6, 9: 9, 12: 15, 10: 12, 15: 14, 13: 2, 14: 3, 2: 13, 8: 8, 11: 5, 4: 10, 7: 11, 1: 16},
        {0: 1, 3: 4, 5: 7, 6: 6, 9: 11, 12: 13, 10: 10, 15: 16, 13: 2, 14: 3, 8: 8, 11: 5, 7: 9, 4: 12, 1: 14, 2: 15}]

    n = 4
    for s in some_sols:
        for row in range(n):
            for col in range(n):
                print(str((s[row * n + col])), end=' ')
            print("")
        print("")
    """

    # run magic square solve
    MS(3).getSolution()
