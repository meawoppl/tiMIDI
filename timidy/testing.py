import unittest, sys

import timidi.tests


def test():
    return unittest.main(timidi.tests)

if __name__ == "__main__":
    sys.exit(0 if test() else 1)
