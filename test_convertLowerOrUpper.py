import convertLowerOrUpper
import pytest

pytest.fixture(scope='module')
def test_case1() :
        assert convertLowerOrUpper.caseUnification('abcDEFGH') == 'ABCDEFGH'

def test_case2() :
        assert convertLowerOrUpper.caseUnification('ZZZZaaaaaaa') == 'zzzzaaaaaaa'
