def check_hello_world():
  expected = "Hello, World!"
  actual = "Hello, World!"

  if actual == expected:
    print("Test Passed: Output contains 'Hello, World!'")
    return 0
  else:
    print("Test Failed: Output does not match 'Hello, World!'")
    return 1

  if __name__ == "__main__":
    exit(check_hello_world())
