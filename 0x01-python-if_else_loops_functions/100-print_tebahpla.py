#!/usr/bin/python3
print("".format().join(list(map(lambda x: chr(x).upper() if x %
                                2 is not 0 else chr(x),
                                [x for x in range(122, 96, -1)]))), end="")
