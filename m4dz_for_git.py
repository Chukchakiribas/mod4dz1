def palindrome(pal):
    return pal == pal[::-1]

while True:
    pal = input()
    print(f'True' if palindrome(pal) else 'False')