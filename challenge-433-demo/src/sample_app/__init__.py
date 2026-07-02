#!/usr/bin/env python3
"""A tiny sample app to demonstrate qtop-style CI/CD pipeline structure."""

__version__ = "0.1.0"


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def main():
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
