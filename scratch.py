import math
import calculator as CH
import generate

def fxIter():
    myList = range(4)
    for x in myList:
        yield x*x

def tst1():
    mygen = fxIter()
    print(mygen)

    for x in mygen:
        print(x)

    vStr = "hellokitty\n"
    print(vStr[0])
    for c in vStr:
        print(c, ord(c))


class ExpressionHelper:
    _sb = 0
    _eb = 0

def main():
    # calculate_expression("(((2*3)+(1+2))*2)")
    # print(calculate_expression("(8/4-99/33)"))
    tst1()

    print(generate.generate("1", "2", "3"))
    print(CH.calculate_expression("    18*63/17", True))
    print(int(float(CH.calculate_expression("    ( -12  ^(18/6    ))/12", True))))
    print(CH.calculate_expression("    18*63/17", False))
    print(int(float(CH.calculate_expression("     -12  ^(12/6    )", False))))

if __name__ == "__main__":
    main()

