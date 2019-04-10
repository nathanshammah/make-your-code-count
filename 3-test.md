# 3 - Testing your code

"Untested code is broken code". Unit testing makes sure that different components of software (each unit) work properly. To do so, all one has to do is to write some functions that perform some basic check of the purported result in a simple instance. 

## 3.1 -  Testing locally: writing the tests
- Set up a file with your testing function. Ideally, each function should have a test function. 

For example, in `test_dicke.py`, there is a class, `TestDicke` testing the `Dicke` class from the `piqs` library,

```python
import numpy as np
from numpy.testing import (assert_, run_module_suite, assert_raises,
                           assert_array_equal, assert_array_almost_equal,
                           assert_almost_equal, assert_equal)
from piqs import *
class TestDicke:
    """
    A test class for the Permutational Invariant Quantum Solver (PIQS) from the Dicke class.
    """

    def test_num_dicke_states(self):
        """
        Test the `num_dicke_states` function.
        """
        N_list = [1, 2, 3, 4, 5, 6, 9, 10, 20, 100, 123]
        dicke_states = [num_dicke_states(i) for i in N_list]
        assert_array_equal(dicke_states, [2, 4, 6, 9, 12, 16, 30, 36, 121,
                                          2601, 3906])
        N = -1
        assert_raises(ValueError, num_dicke_states, N)
        N = 0.2
        assert_raises(ValueError, num_dicke_states, N)
if __name__ == "__main__":
    run_module_suite()
```

## 3.2 - Testing locally: automated tests
- Set up a testing script. There are a couple of options, nose, nose2 and pytest.

## 3.3 - Automated cloud testing
- Set up [Travis CI](https://travis-ci.org). This continuous integration tool checks that every pull request to your GitHub project is always passing the tests according to the specifics set up by you.
That is, Travis CI every time installs from scratch all the dependencies on a clean machine.


Advance to Section [4 - Packaging your Library](4-package.md).

