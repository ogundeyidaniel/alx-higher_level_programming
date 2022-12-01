#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    args, arg_len = sys.argv, len(sys.argv) - 1
    table = {"+": add, "-": sub, "*": mul, "/": div}
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a, op, b = int(args[1]), args[2], int(args[3])
    c = table[args[2]](a, b)
    print("{} {} {} = {}".format(a, op, b, c))
