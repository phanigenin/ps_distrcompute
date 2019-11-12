from src.multithread import PSCMultiThreadExecutor
from nose import with_setup
from nose.tools import nottest,raises,assert_equal,assert_equals,assert_almost_equal

thrdpool = None


@nottest
def setupThreadPoolExecutor():
    global thrdpool
    thrdpool = PSCMultiThreadExecutor(workers=6)

print('teeee')

@with_setup(setupThreadPoolExecutor)
def test_mapfunction():# Tries to add reverse dep, invalid dag
    print('Phani')

    def calc_square(x):
        return x**2

    def calc_npow(x,n):
        return x**n

    res = thrdpool.map(calc_square,range(5))
    #res = thrdpool.map(calc_square,[1,2,4])
    print(res)
    assert True