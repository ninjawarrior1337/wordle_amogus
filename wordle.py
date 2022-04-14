from functools import cache
from jinja2 import Template
import htmlmin
import json

solutions: list[str] = []
guesses: list[str] = []

def load_wordle_words():
    global guesses, solutions
    with open("valid_guesses_nyt.json") as f:
        guesses = json.load(f)

    with open("possible_words_nyt.json") as f:
        solutions = json.load(f)

    guesses.extend(solutions)

@cache
def compute_pattern(target: str, guessed: str) -> str:
  ABSENT = 0
  PRESENT = 1
  CORRECT = 2
  LETTER_MAP = {0: "X", 1: "Y", 2: "G"}

  result = [ABSENT] * 5
  incorrect = [True] * 5
  unused = [True] * 5

  for i in range(5):
    if target[i] == guessed[i]:
      result[i] = CORRECT
      incorrect[i] = False
      unused[i] = False
    
  for i in range(5):
    if incorrect[i]:
      correctLetter = target[i]
      for k in range(5):
        if unused[k] and correctLetter == guessed[k]:
          result[k] = PRESENT
          unused[k] = False
          break
      

  return "".join(LETTER_MAP[j] for j in result)

class WordleBoard():
    words: list[str]
    results: list[str]

    def __init__(self, words: list[str], results: list[str]) -> None:
        self.words = [w.upper() for w in words]
        self.results = results

    @staticmethod
    def map_to_class(s: str):
        if s == "G":
            return "correct"
        elif s == "X":
            return "wrong"
        elif s == "Y":
            return "exists"

    def _repr_html_(self) -> str:
        with open("wordle.html", "r") as f:
            tmpl = Template(f.read())
            letters = [c for w in self.words for c in w]
            results = [self.map_to_class(c) for r in self.results for c in r]
            html = tmpl.render({"lr": zip(letters, results)})
            return htmlmin.minify(html)

load_wordle_words()