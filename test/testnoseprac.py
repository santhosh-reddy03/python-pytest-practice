from dev.sample_test import add2num

from nose.tools import assert_equals, ok_, eq_, raises

class Testadd2num():

    def test_sum2pos(self):
        assert add2num(6, 7)==13 

    def test_sum1pos_1neg(self):
        assert add2num(5, -6)==-1

def test_nose():
    assert_equals('HELLO','hello'.upper())

def test_using_ok():
    ok_(2+3==5)

@raises(TypeError)
def test_using_eq():
    eq_(2+'3',5)


# from nose.tools 
# import raises
class SampleTestClass:
    @raises(TypeError)
    def test_sample1(self):
        pow(2, '4')
    @raises(Execption)    
    def test_sample2(self):        
        max([7, 8, '4'])
    
    @raises(Exception)
    def test_sample3(self):
        int('hello')