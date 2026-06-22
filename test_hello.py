# test_hello.py
# Importing hello.py makes Python parse it. While hello.py has a syntax error,
# this import fails, pytest reports a collection error, and CI goes red.
# Once the loop adds the missing ")", this passes.
import hello  # noqa: F401


def test_hello_imports():
    assert True
