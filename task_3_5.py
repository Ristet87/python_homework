from random import choice


def get_jokes(n):
    jokes = []
    for i in range(n):
        joke = ' '.join([choice(nouns), choice(adverbs), choice(adjectives)])
        jokes.append(joke)
    print(jokes)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]

get_jokes(5)


