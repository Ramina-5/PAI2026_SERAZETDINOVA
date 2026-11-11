import numpy as np

from arxiv_trends.my_module import typed_function


def test_typed_function():
    assert not typed_function(np.zeros(10), "")
