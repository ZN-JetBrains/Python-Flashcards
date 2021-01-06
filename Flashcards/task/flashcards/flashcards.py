import random
import json


class Menu:
    ADD = "add"
    REMOVE = "remove"
    IMPORT = "import"
    EXPORT = "export"
    RANDOM = "ask"
    EXIT = "exit"


class Flashcards:
    def __init__(self):
        self.flashcard_dict = {}

    def print_all_cards(self):
        if not self.flashcard_dict:
            print("Empty.")
            return
        for key, value in self.flashcard_dict.items():
            print(f'"{key}" = "{value}"')

    def add_card(self):
        print("The card:")
        while True:
            term = input()
            if term in self.flashcard_dict:
                print(f"The term \"{term}\" already exists. Try again:")
                continue
            else:
                print(f"The definition of the card:")
                while True:
                    definition = input()
                    if definition in self.flashcard_dict.values():
                        print(f"The definition \"{definition}\" already exists. Try again:")
                        continue
                    print(f'The pair ("{term}":"{definition}") has been added.')
                    self.flashcard_dict[term] = definition
                    break
            break

    def remove_card(self):
        print("Which card?")
        card = input()
        if card in self.flashcard_dict:
            del self.flashcard_dict[card]
            print("The card has been removed.")
        else:
            print(f'Can\'t remove "{card}": there is no such card.')

    def load_cards_from_file(self):
        file_name = input("File name:\n")
        try:
            with open(f"{file_name}", "r") as in_file:
                if in_file:
                    temp_dict = json.load(in_file)
                    for key, value in temp_dict.items():
                        self.flashcard_dict[key] = value
                    print(f"{len(temp_dict)} cards have been loaded.")
        except:
            print("File not found.")

    def save_cards_to_file(self):
        file_name = input("File name:\n")
        try:
            with open(f"{file_name}", "w") as out_file:
                if out_file:
                    json.dump(self.flashcard_dict, out_file)
                    print(f"{len(self.flashcard_dict)} cards have been saved.")
        except:
            print("File not found.")

    def ask_random_cards(self):
        if not self.flashcard_dict:
            print("Empty.")
            return
        try:
            num_cards = int(input("How many times to ask?\n"))
        except ValueError:
            pass
        else:
            for _ in range(num_cards):
                key = random.choice(list(self.flashcard_dict))
                correct_answer = self.flashcard_dict[key]
                user_guess = input(f'Print the definition of "{key}":\n')
                if user_guess == correct_answer:
                    print("Correct!")
                else:
                    if user_guess in self.flashcard_dict.values():
                        other_key = get_key(self.flashcard_dict, user_guess)
                        print(f"Wrong. The right answer is \"{correct_answer}\", ", end="")
                        print(f"but your definition is correct for \"{other_key}\".")
                    else:
                        print(f"Wrong. The right answer is \"{correct_answer}\".")

    def run(self):
        while True:
            user_input = input("Input the action (add, remove, import, export, ask, exit):\n")

            if user_input == Menu.ADD:
                self.add_card()
            elif user_input == Menu.REMOVE:
                self.remove_card()
            elif user_input == Menu.IMPORT:
                self.load_cards_from_file()
            elif user_input == Menu.EXPORT:
                self.save_cards_to_file()
            elif user_input == Menu.RANDOM:
                self.ask_random_cards()
            elif user_input == Menu.EXIT:
                print("Bye bye!")
                break
            elif user_input == "print":
                self.print_all_cards()
            else:
                print("[Error]: That is not a valid action.")


def add_cards(a_dict, a_amount_cards):
    for index in range(a_amount_cards):
        print(f"The term for card #{index + 1}:")
        while True:
            term = input()
            if term in a_dict:
                print(f"The term \"{term}\" already exists. Try again:")
                continue
            else:
                print(f"The definition for card #{index + 1}:")
                while True:
                    definition = input()
                    if definition in a_dict.values():
                        print(f"The definition \"{definition}\" already exists. Try again:")
                        continue
                    a_dict[term] = definition
                    break
                break


def get_key(a_dict, a_value):
    for key, value in a_dict.items():
        if value == a_value:
            return key
    return None


def set_num_cards():
    while True:
        try:
            cards = int(input("Input the number of cards:\n"))
        except ValueError:
            print("[Error]: Invalid input, not a number!")
        else:
            return cards


def play_game(a_dict):
    for key, value in a_dict.items():
        print(f"Print the definition of \"{key}\":")
        user_guess = input()

        if user_guess == value:
            print("Correct!")
        else:
            if user_guess in a_dict.values():
                other_key = get_key(a_dict, user_guess)
                print(f"Wrong. The right answer is \"{value}\", but your definition is correct for \"{other_key}\".")
            else:
                print(f"Wrong. The right answer is \"{value}\".")


def run():
    app = Flashcards()
    app.run()

    # flashcard_dict = {}
    # num_cards = set_num_cards()
    # add_cards(flashcard_dict, num_cards)
    # play_game(flashcard_dict)


if __name__ == "__main__":
    run()
