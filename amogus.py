import random
from wordle import WordleBoard, guesses, solutions, compute_pattern

amogus_template_left = [
    "XYYYX",
    "YYGGX",
    "YYYYX",
    "XYYYX",
    "XYXYX",
    "GGGGG"
]

amogus_template_right = [
    "XXYYY",
    "XYYGG",
    "XYYYY",
    "XXYYY",
    "XXYXY",
    "GGGGG"
]

amogus = (amogus_template_left, amogus_template_right)


def matches_template(target, tmpl):
    p = [g for g in [*guesses, target] if compute_pattern(target, g) == tmpl]
    if len(p) > 0:
        return random.choice(p)
    else:
        return "xxxxx"


def compute_valid_amogus(word):
    answers = []
    for tmpl in amogus:
        answers.append([matches_template(word, t) for t in tmpl])

    return tuple(answers)


def answers_to_board(a: tuple[list[str], list[str]]) -> tuple[WordleBoard, WordleBoard]:
    l, r = a
    lb = WordleBoard(l, [compute_pattern(l[-1], re) for re in l])
    rb = WordleBoard(r, [compute_pattern(l[-1], re) for re in r])
    return (lb, rb)