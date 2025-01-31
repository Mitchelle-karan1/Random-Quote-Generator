import random

quotes = [
    "The best way to predict the future is to create it.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "Your time is limited, so don’t waste it living someone else’s life.",
    "Do what you can, with what you have, where you are."
]

def get_random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print("Random Quote Generator")
    print("----------------------")
    print(get_random_quote())
