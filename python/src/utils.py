def let_to_coords(pos):
    letter = pos[0].lower()
    letter = int(ord(letter) - 97)
    number = int(pos[1]) - 1
    return letter, number
