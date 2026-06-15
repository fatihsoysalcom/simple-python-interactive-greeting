# This is a simple Python script to demonstrate basic input/output operations.
# It's a common "first program" for beginners learning Python and setting up their environment.

def main():
    # Print a welcome message to the console. This is the first output the user sees.
    print("Merhaba! Python dünyasına hoş geldiniz.") # Welcome to the Python world!

    # Use the input() function to get text input from the user.
    # The prompt message is displayed to the user.
    user_name = input("Adınız nedir? ") # What is your name?

    # Use an f-string (formatted string literal) to include the user's name in the next prompt.
    fav_lang = input(f"Merhaba {user_name}! Favori programlama diliniz nedir? ") # Hello {name}! What is your favorite programming language?

    # Print a personalized message using another f-string.
    # This combines the user's input into a meaningful response, demonstrating variable usage.
    print(f"Harika bir seçim, {user_name}! {fav_lang} ile kod yazmaya başlamak için VS Code'u kullanabilirsiniz.")
    # Great choice, {name}! You can use VS Code to start coding with {fav_lang}.

    print("İyi kodlamalar!") # Happy coding!

# This ensures that the main() function is called only when the script is executed directly
# (not when imported as a module).
if __name__ == "__main__":
    main()
