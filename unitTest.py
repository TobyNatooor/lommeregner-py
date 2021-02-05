from splitStringFunction import SplitStringFunction

test = SplitStringFunction("x^2-10*x+1")
assert test.num1 == 1
assert test.num2 == -10
assert test.num3 == 1
assert test.power == 2
test = SplitStringFunction("-x^1+7*x-33")
assert test.num1 == -1
assert test.num2 == 7
assert test.num3 == -33
assert test.power == 1
test = SplitStringFunction("4x^5-21")
assert test.num1 == 4
assert test.num2 == 0
assert test.num3 == -21
assert test.power == 5
test = SplitStringFunction("-6x^6+13*x")
assert test.num1 == -6
assert test.num2 == 13
assert test.num3 == 0
assert test.power == 6
test = SplitStringFunction("5*x-667")
assert test.num1 == 0
assert test.num2 == 5
assert test.num3 == -667
assert test.power == 0
test = SplitStringFunction("-x^1+50")
assert test.num1 == -1
assert test.num2 == 0
assert test.num3 == 50
assert test.power == 1
# test = SplitStringFunction("53")
# assert test.num1 == 0
# assert test.num2 == 0
# assert test.num3 == 53
# assert test.power == 0
print("All tests succeeded!")

from lommeregnerClass import Lommeregner
test = Lommeregner()
test.insertNum("5")
test.insertOperator("+")
test.insertNum("5")
test.calculate()
assert "10" == test.LRLabel
