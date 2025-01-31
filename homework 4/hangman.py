import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")

def print_revealed_phrase(answer, letters):
  revealed_p = ""
  for char in answer:
    if char.isalpha() and char in letters:
      revealed_p += char
    elif not char.isalpha():
      revealed_p += char
    else:
      revealed_p += "_"
  print(revealed_p)

def get_letter(chars_guessed):
  while True:
    guess = input("Please enter a letter:")
    if(not guess.isalpha() or len(guess) != 1):
      if guess == "":
        print('""'+" is not a letter!")
      else:
        print('"' + guess + '"' + " is not a letter!")
    elif(guess.upper() in chars_guessed):
      print('"' + guess + '"' + " has already been guessed!")
    else:
      return guess.upper()

def won(answer,letters):
    for chars in answer:
      if chars.isalpha() and chars not in letters:
         return False   
    return True

def play_game():
  phrase = make_phrase()
  misses = 0
  guesses = []
  print("*** Welcome to Hangman ***")
  print_gallows(misses)
  while True:
        print_revealed_phrase(phrase, guesses)
        
        print("Letters guessed:", ", ".join(sorted(guesses)))
        
        guess = get_letter(guesses)
        if guess not in guesses:
          guesses.append(guess)

        if won(phrase, guesses):
                print_revealed_phrase(phrase,guesses)
                print("Congratulations!")
                break

        if guess not in phrase:
            misses += 1
            print_gallows(misses)
            
            if misses == 6:
                print("Game Over!")
                print("Solution was:", phrase)
                break
            
            