from dev.sample_dev import add2num

import pytest

# @pytest.mark.skip("testing skip")
class Testadd():
    
    def test_add2(self):
        assert add2num(2,3) == 5

    def test_add1neg1pos(self):
        assert add2num(1, -4) == -3

def test_excep():
    with pytest.raises(TypeError):
        assert 2 + '3' == 5