#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addition_result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            addition_result += int(arg)
    print("{}".format(addition_result))