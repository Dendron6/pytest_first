from my_funcs.utils import division

import pytest


# a, b, expected_result = (10, 2, 5) explaines how it works

@pytest.mark.parametrize("a,b, expected_result", [(10, 2, 5), (20, 10, 2), (30, -3, -10), (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

#this test allows us to raise errors
@pytest.mark.parametrize('expected_exception, divider, div', [(ZeroDivisionError, 0,10),(TypeError,"2",20)])
def test_dev_with_error(expected_exception, divider, div):
    with pytest.raises(expected_exception):
         division(div, divider)





