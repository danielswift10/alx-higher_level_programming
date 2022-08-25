#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    last_element = len(sys.argv) - 1

    if last_element == 0:
        print("{} arguments.".format(last_element))
    elif last_element == 1:
        print("{} argument:".format(last_element))
    else:
        print("{} arguments:".format(last_element))

   for i in range(last_element):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))