def CheckEnum(lives):
  lives += 1
  if lives == 6:
      print(Pictures[0])
  elif lives == 5:
      print(Pictures[1])
  elif lives == 4:
      print(Pictures[2])
  elif lives == 3:
      print(Pictures[3])
  elif lives == 2:
      print(Pictures[4])
  elif lives == 1:
      print(Pictures[5])
  elif lives == 0:
      print(Pictures[6])
  def CheckEnum(lives):
    lives += 1
    if lives == 6:
        print(Pictures[0])
    elif lives == 5:
        print(Pictures[1])
    elif lives == 4:
        print(Pictures[2])
    elif lives == 3:
        print(Pictures[3])
    elif lives == 2:
        print(Pictures[4])
    elif lives == 1:
        print(Pictures[5])
    elif lives == 0:
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