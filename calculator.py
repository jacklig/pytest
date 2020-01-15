import math

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class CaInputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class ExpressionHelper:
    _sb = 0
    _eb = 0

class CalculationHelper:

    def __init__(self, sExp, vUnit):
        #
        # vUnit indicates we are doing testing and additional checks
        #
        self.fUnit = vUnit

        #
        # This is just to make our logic simpler to follow.
        #
        sExp = "(" + sExp + ")"

        if vUnit==True: print(sExp)

        self._Result = "Invalid"
        self._eh = ExpressionHelper()
        sExp = sExp.replace(" ","")

        self._eh._sb = sExp.count('(')
        self._eh._eb = sExp.count(')')

        if self._eh._sb != self._eh._eb:
            raise CaInputError("The number of opening and closing brackets must match", str(self._eh._sb) + " must equal " + str(self._eh._eb))

        i=0
        for c in sExp:
            if "0123456789()+-*/^".__contains__(c)!=True:
                raise CaInputError("Expression contains invalid characters", c)

        if vUnit==True: print(sExp)

        _evaluated = True
        while _evaluated:
            _evaluated = False
            _ob = 0
            _cb = 0
            i = 0
            i2 = 0
            _insub = 0

            for c in sExp:
                if c == '(':
                    _ob = i
                    _insub += 1

                if c == ')':
                    _cb = i
                    _insub -= 1
                    _evaluated, sExp = self.Simplify(sExp, _ob, _cb)
                    if _evaluated: break
                    else: raise CaInputError("bad expression", "check string")

                i+=1

        self._Result = sExp

    def Result(self):
        return self._Result

    def EvalInner(self, sInner):
        if sInner.__contains__("()"):
            raise CaInputError("Bad expression", sInner)

        c = sInner.count('+')
        c += sInner.count('-')
        c += sInner.count('*')
        c += sInner.count('/')
        c += sInner.count('^')
        c += sInner.count('%')

        _f = True
        _vList = []
        _l = ""
        i = 0

        for c in sInner:
            if "+-*/%^".__contains__(c) and _l != "":
                _vList.append(float(_l))
                _vList.append(c)
                _l = ""
            #
            # The following two cases only occur when you start an equation like:
            #   -19+20 or +19-20
            #
            elif c == '-' and _l == '':
                _l += c
            elif c == '+' and _l == '':
                # do nothing
                i = i

            #
            # Just seeing a #
            #
            else:
                _l += c

            i = i+1

        if _l != "":
            _vList.append(float(_l))
            _l = ""

        if len(_vList) == 1:
            return _vList[0]

        if len(_vList)%2 == 0:
            raise CaInputError("Bad input couldn't a valid equation", sInner)


        #
        # do exponents
        #
        ops = "^*/+-"
        fcns = []
        fcns.append(lambda x, y: math.pow(x, y))
        fcns.append(lambda x, y: x*y)
        fcns.append(lambda x, y: x/y)
        fcns.append(lambda x, y: x+y)
        fcns.append(lambda x, y: x-y)

        w = 0

        for j in range(len(ops)):
            i = 1
            while i < len(_vList):
                fCompound = False
                fdo = False

                if (j==1) or (j==3):
                    fCompound = True

                if _vList[i] == ops[j]:
                    fcn = fcns[j]
                    fdo = True
                elif fCompound and _vList[i] == ops[j+1]:
                    fcn = fcns[j+1]
                    fdo = True

                if fdo:
                    _v = fcn(_vList[i-1],_vList[i+1])
                    del _vList[i-1]
                    del _vList[i-1]
                    _vList[i-1] = _v
                    i = 1
                    w += 1
                    continue

                i += 2

        return _vList[0]

    def Simplify(self, sExp, _ob, _cb):
        # left part not including the opening bracket
        # len(lp) == 0-_ob
        lp = sExp[0:_ob]

        # right part not including ending bracket.  Ending bracket may
        # be the last character so _cb+1 may equal len of sExp
        #
        # len = _cb+1 - len(sExp)
        if _cb > len(sExp):
            raise CaInputError("Bad expression", sExp)

        rp = sExp[_cb+1:len(sExp)]

        #
        # we will replace eval later
        #
        res = str(self.EvalInner(sExp[_ob+1:_cb]))

        res = lp+res+rp

        if(res == sExp):
            return False, "0"

        return True, res

def calculate_expression(sExp, fUnit):
    _ch = CalculationHelper(sExp, fUnit)
    return _ch.Result()

def main():
    # calculate_expression("(((2*3)+(1+2))*2)")
    # print(calculate_expression("(8/4-99/33)"))
    # tst1()
    f = open("out.txt", 'a')
    print(calculate_expression("    18*63/17", True))
    print(int(float(calculate_expression("     12", True))))
    f.writelines(calculate_expression("    18*63/17", True))
    f.close()

if __name__ == "__main__":
    main()