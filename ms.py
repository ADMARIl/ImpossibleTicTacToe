from constraint import *
########################################
# HW 3 Magic Square Example using Constraint library
#
#######################################

#Example Problem
p = Problem()


#Adding Variables
p.addVariables(range(9), range(1,10))


#Adding Constrains
p.addConstraint(AllDifferentConstraint(), range(9))

p.addConstraint(ExactSumConstraint(15), [0,4,8])
p.addConstraint(ExactSumConstraint(15), [2,4,6])

for row in range(3):
    p.addConstraint(ExactSumConstraint(15),
                    [row*3+i for i in range(3)])

for col in range(3):
    p.addConstraint(ExactSumConstraint(15),
                    [col+3*i for i in range(3)])

#Get solutions
sols = p.getSolutions()
print( sols)

#Loop through solutions
#Print results
for s in sols:
    for row in range(3):
        for col in range(3):
            print(str((s[row*3+col])), end = '')
        print("")
    print("")


