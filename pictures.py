def CheckEnum(lives):
  if lives-1 == 6:
      print(Pictures[0])
  elif lives-1 == 5:
      print(Pictures[1])
  elif lives-1 == 4:
      print(Pictures[2])
  elif lives-1 == 3:
      print(Pictures[3])
  elif lives-1 == 2:
      print(Pictures[4])
  elif lives-1 == 1:
      print(Pictures[5])
  elif lives-1 == 0:
      print(Pictures[6])


Pictures = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
