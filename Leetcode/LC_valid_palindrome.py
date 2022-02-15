
def main():
    s = "0P"
    if len(s) ==1:
            return True
    si=""
    for i, c in enumerate(s):
        if c.isalpha():
            si = si+c.lower()
    print(si)
    reversed_s = si[::-1]
    print(reversed_s)
    print(si == reversed_s)


if __name__ == "__main__":
    main()
