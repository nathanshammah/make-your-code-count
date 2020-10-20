"""
Tests for the hello module
"""
from mylibrary.hello import hello

import pytest


def test_hello():
	"""
	Tests the hello function.
	"""
	assert(hello("John") == "Hello John")
	assert(hello("Mary") == "Hello Mary")

	pytest.raises(ValueError, hello, [5])
