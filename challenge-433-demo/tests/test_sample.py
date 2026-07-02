"""Sample tests for the demo app."""
from sample_app import greet, add

def test_greet():
    assert greet("World") == "Hello, World!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
