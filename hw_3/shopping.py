"""Shopping Spree - A modified version of the knapsack dynamic programming problem.

SETUP:
Acme Super Store is having a contest to give away shopping sprees to lucky families. 
If a family wins a shopping spree each person in the family can take any items in the store 
that he or she can carry out, however each person can only take one of each type of item. 

This is an algorithm to determine the maximum total price of items for each family 
and the items that each family member should select.

INPUT:
The input file named “shopping.txt” consists of T test cases
T (1 ≤ T ≤ 100) is given on the first line of the input file.

Each test case begins with a line containing a single integer number N that indicates the
number of items (1 ≤ N ≤ 100) in that test case

Followed by N lines, each containing two integers: P and W. The first integer (1 ≤ P ≤
5000) corresponds to the price of object and the second integer (1 ≤ W ≤ 100)
corresponds to the weight of object.

The next line contains one integer (1 ≤ F ≤ 30) which is the number of people in that
family.

The next F lines contains the maximum weight (1 ≤ M ≤ 200) that can be carried by the
ith person in the family (1 ≤ i ≤ F).

OUTPUT:
Results written to a file named “results.txt”. 


Thomas Banghart
Oregon State University
CS325 - Analysis of Algorithms (Fall 2020)
HW - 3
"""
from utils import *
import os


def ShoppingSpreeDP(N, M, P, W):
    """
    Dynamic Programming algorithim for the knapsack problem
    """
    # Table with each item as row, and weight person can carry as col
    # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
    V = [[0 for _ in range(M+1)] for _ in range(N+1)]
    # Additonal table to keep track of item indices because we care more about what items are optimal than their price.
    I = [[0 for _ in range(M+1)] for _ in range(N+1)]
    # Populate the table with optimal choices for each weight capacity
    for i in range(N + 1):
        for j in range(M + 1):
        # Initalize the base state of each row and col
            
            if i == 0 or j == 0:
                V[i][j] = 0
                I[i][j] = ""

            # Else if we are not at the tables edges, lets see if the person can carry a new item
            elif W[i-1] <= j:
            # The current cell is the max of either:
            # Price of the item + the previous optimal choice for the remaining weight 
            # OR it is simply the same as before the new item was introduced (bring down prev row)
                newChoice = P[i - 1] + V[i - 1][j - W[i - 1]]
                prevOptimal = V[i - 1][j]
                newItems = str(I[i - 1][j - W[i - 1]]) + str(i-1) + " "
                prevItems = I[i - 1][j]
                if newChoice > prevOptimal:
                    V[i][j] = newChoice
                    I[i][j] = newItems
                else:
                    V[i][j] = prevOptimal
                    I[i][j] = prevItems
            else:
                prevOptimal = V[i - 1][j]
                prevItems = I[i - 1][j]
                V[i][j] = prevOptimal
                I[i][j] = prevItems

    return V[N][M], I[N][M]


def ShoppingSpree(T, F, N, M, P, W):
    """
    T = # of test cases (total number of familys)
    F = # of family members
    N = # of items
    M = Array of weights that each family member can carry where F[i] -> M[i]
    P = Array of prices for an item
    W = Array of weights for each item such that P[i] -> W[i]
    """
    total = 0
    C = [0] * F
    for i in range(F):
        val, C[i] = ShoppingSpreeDP(N, M[i], P, W)
        total += val

    with open('shopping.out', 'a') as file:
        file.write("Test Case {}\n".format(T + 1))
        file.write("Total Price {}\n".format(total))
        file.write("Member Items\n")
        for i in range(F):
            C[i] = [str(int(i.strip()) + 1) for i in C[i].split(" ")[:-1]]
            file.write("{0}: {1}\n".format(i+1, " ".join(C[i])))
        # file.write("\n")


def main():
    if os.path.exists("shopping.out"):
      os.remove("shopping.out")
    T, N, P, W, F, M = read_file()
    for i in range(T):
        ShoppingSpree(i, F[i], N[i], M[i], P[i], W[i])



if __name__ == "__main__":
    main()
