import check50
import check50.c

@check50.check()
def exists():
    """helpers.c exists."""
    check50.exists("helpers.c")


@check50.check(exists)
def compiles():
    """helpers.c compiles."""
    check50.include("helpers.h", "find.c", "sort.c")
    check50.c.compile("sort.c", "helpers.c", exe_name="sort", lcs50=True)
    check50.c.compile("find.c", "helpers.c", exe_name="find", lcs50=True)


@check50.check(compiles)
def sort_reversed():
    """sorts {5,4,3,2,1}"""
    test_sorted([5, 4, 3, 2, 1])


@check50.check(compiles)
def sort_shuffled():
    """sorts {5,3,1,2,4,6}"""
    test_sorted([5, 3, 1, 2, 4, 6])


@check50.check(compiles)
def first_among_three():
    """finds 28 in {28,29,30}"""
    check50.run("./find 28").stdin("28").stdin("29").stdin("30").stdin(check50.EOF).exit(0)

# @check("compiles")
# def second_among_three(self):
#     """finds 28 in {27,28,29}"""
#     self.spawn("./find 28").stdin("27").stdin("28").stdin("29").stdin(EOF).exit(0)
#
# @check("compiles")
# def third_among_three(self):
#     """finds 28 in {26,27,28}"""
#     self.spawn("./find 28").stdin("26").stdin("27").stdin("28").stdin(EOF).exit(0)
#
# @check("compiles")
# def second_among_four(self):
#     """finds 28 in {27,28,29,30}"""
#     self.spawn("./find 28").stdin("27").stdin("28").stdin("29").stdin("30").stdin(EOF).exit(0)
#
# @check("compiles")
# def third_among_four(self):
#     """finds 28 in {26,27,28,29}"""
#     self.spawn("./find 28").stdin("26").stdin("27").stdin("28").stdin("29").stdin(EOF).exit(0)
#
# @check("compiles")
# def fourth_among_four(self):
#     """finds 28 in {25,26,27,28}"""
#     self.spawn("./find 28").stdin("25").stdin("26").stdin("27").stdin("28").stdin(EOF).exit(0)
#
# @check("compiles")
# def not_among_three(self):
#     """doesn't find 28 in {25,26,27}"""
#     self.spawn("./find 28").stdin("25").stdin("26").stdin("27").stdin(EOF).exit(1)
#
# @check("compiles")
# def not_among_four(self):
#     """doesn't find 28 in {25,26,27,29}"""
#     self.spawn("./find 28").stdin("25").stdin("26").stdin("27").stdin("29").stdin(EOF).exit(1)
#
# @check("compiles")
# def needle_too_low_four(self):
#     """doesn't find 28 in {29,30,31,32}"""
#     self.spawn("./find 28").stdin("29").stdin("30").stdin("31").stdin("32").stdin(EOF).exit(1)
#
# @check("compiles")
# def needle_too_low_three(self):
#     """doesn't find 28 in {29, 30, 31}"""
#     self.spawn("./find 28").stdin("29").stdin("30").stdin("31").stdin(EOF).exit(1)
#
# @check("compiles")
# def correctly_sorts(self):
#     """finds 28 in {30,27,28,26}"""
#     self.spawn("./find 28").stdin("30").stdin("27").stdin("28").stdin("26").stdin(EOF).exit(0)

def test_sorted(items):
    check = check50.run("./sort")
    for i in items:
        check.stdin(str(i))
    check.stdin(check50.EOF)
    for i in sorted(items):
        check.stdout(str(i))
    check.exit(0)
