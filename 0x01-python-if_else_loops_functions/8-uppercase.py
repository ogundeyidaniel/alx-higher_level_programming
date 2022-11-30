#!/usr/bin/python3
def uppercase(str):
    print("".format()
            .join(list(map(lambda x: chr(ord(x) - 32)
                           if ord(x) in range(97, 123) else x, str))))
