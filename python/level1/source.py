print(' '.join(sorted([char.lower() if (ord(char) - 97) % 2 == 0 else char.upper() for char in input()], reverse=True)))
