import math
from random import seed
from random import random
import time
import time as TI

class GenHelper:
    """helps build minecraft stuff"""


def generate(sName, vParams, vOptions):
    start = time.time()
    seed(start)
    print("Generate: " + sName + vParams + vOptions + " " + str(random()) + str(random()))

    CDICK = {0:"normal",1:"cross",2:"battle",4:"pistol"}
    end = time.time()
    print(end-start)
    return "done"

def main():
    print("main\n\n\n")

if __name__ == "__main__":
    main()

