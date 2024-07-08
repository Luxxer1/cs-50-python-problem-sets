def main():
    x, y, z = input("Expression: ").split(" ")
    result = calcExpression(x, y, z)
    print(f"{result:.1f}")

def calcExpression(x, y, z):
    x = int(x)
    z = int(z)

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "/":
            return x / z
        case "*":
            return x * z

main()
