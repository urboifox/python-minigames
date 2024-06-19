import random

def get_wordle():
    words = [
        "apple", "baker", "cider", "delta", "eagle",
        "fjord", "grape", "hotel", "india", "joker",
        "karma", "lemon", "mango", "novel", "orange",
        "piano", "quest", "river", "risen", "tango",
        "umbra", "mamba", "women", "death", "yacht",
        "zebra", "alarm", "beach", "crane", "dance",
        "emote", "flute", "giant", "happy", "igloo",
        "jolly", "knife", "lemon", "money", "noble",
        "oasis", "peace", "queen", "rider", "space",
        "tiger", "unity", "vital", "witty", "young",
    ]
    return random.choice(words)