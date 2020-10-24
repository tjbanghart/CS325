"""Shopping Spree Utils - I/O utiliy methods for assisting with shopping.py

Thomas Banghart
Oregon State University
CS325 - Analysis of Algorithms (Fall 2020)
HW - 3
"""

def read_file():
    """
    Reads the contents of shopping.txt and returns arrays to be sorted.
    """
    T = 0
    N = [None] * 1000
    F = [None] * 1000
    P = [[None for _ in range(1000)] for _ in range(1000)]
    W = [[None for _ in range(1000)] for _ in range(1000)]
    M = [[None for _ in range(1000)] for _ in range(1000)]
    try:
        with open('shopping.txt', 'r') as file:
            T = int(file.readline().strip())
            for i in range(T):
                N[i] = (int(file.readline().strip()))
                for j in range(N[i]):
                    line = file.readline().split(" ")
                    price = int(line[0])
                    weight = int(line[1])
                    P[i][j] = price
                    W[i][j] = weight
                F[i] = int(file.readline().strip())
                for j in range(F[i]):
                    M[i][j] = int(file.readline().strip())
    except EnvironmentError:
        print("This program needs a \"shopping.txt\" file in the same directory to read from.")
    return T, N, P, W, F, M


if __name__ == "__main__":
    read_file()
