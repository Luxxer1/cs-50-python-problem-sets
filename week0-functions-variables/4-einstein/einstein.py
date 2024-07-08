def main():
    m = int(input("m: "))
    print(calcJoules(m))

def calcJoules(m):
    c = 300000000
    return m * (c**2)

main()
