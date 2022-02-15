
#unit testing
def add_five(n):
    n = n+4
    return n

def testing():
    assert add_five(5) == 10


def main():
    testing()
    print("All good")



if __name__ == "__main__":
    main()
