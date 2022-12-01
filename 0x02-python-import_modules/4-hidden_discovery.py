#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for x in dir(hidden_4):
        if not x.startswith("__"):
            print(x)
