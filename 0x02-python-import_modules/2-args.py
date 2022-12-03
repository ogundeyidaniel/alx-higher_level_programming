#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    string = "arguments" if n != 1 else "argument"
    sign = ":" if n > 0 else "."
    print("{} {}{}".format(n, string, sign))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, str(sys.argv[i])))
