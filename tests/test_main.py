from app.main import say_hello

def test_say_hello():
    assert say_hello("John") == "Hello, John! Welcome to CI/CD."

