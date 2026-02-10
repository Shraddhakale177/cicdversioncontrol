
from src.app import greet

def test_greet_default():
    assert greet("Tester") == "Hello, Tester! This app proves the CI/CD flow works."
