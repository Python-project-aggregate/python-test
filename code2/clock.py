
import timeit
def test1(strlist):
    return "".join(strlist)

def test2(strlist):
    result = ""
    for v in strlist:
        result = result+v
    return result

if __name__ == "__main__":
    strlist = ["a very very very very very very very long string" for n in range(100000)]
    timer1 = timeit.Timer("test1(strlist)", "from __main__ import strlist, test1")
    timer2 = timeit.Timer("test2(strlist)", "from __main__ import strlist, test2")
    time1 = timer1.timeit(number=100)
    time2 = timer2.timeit(number=100)
    print("join: %f, plus: %f" % (time1, time2))