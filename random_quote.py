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

def display_multiple_quotes(n):
    if n > len(quotes):
        print("Not enough quotes available.")
        return
    for quote in random.sample(quotes, n):
        print(f'- {quote}')

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Get a Random Quote")
        print("2. Add a New Quote")
        print("3. Display Multiple Quotes")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(get_random_quote())
        elif choice == "2":
            new_quote = input("Enter the new quote: ")
            add_quote(new_quote)
        elif choice == "3":
            n = int(input("Enter number of quotes to display: "))
            display_multiple_quotes(n)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
