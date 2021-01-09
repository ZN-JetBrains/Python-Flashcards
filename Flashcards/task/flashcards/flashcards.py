import random
import json
from io import StringIO


class Menu:
    ADD = "add"
    REMOVE = "remove"
    IMPORT = "import"
    EXPORT = "export"
    RANDOM = "ask"
    EXIT = "exit"
    LOG = "log"
    HARD = "hardest card"
    RESET = "reset stats"
    PRINT = "print"


class Flashcards:
    def __init__(self):
        self.flashcard_dict = {}
        self.logger = StringIO()

    def print_all_cards(self):
        if not self.flashcard_dict:
            print("Empty.")
            return
        for key in self.flashcard_dict.keys():
            print(f'"{key}": {self.flashcard_dict[key]}')

    def add_card(self):
        output_str = "The card:"
        self.log_line(output_str)
        print(output_str)
        while True:
            term = input()
            self.log_line(term)
            if term in self.flashcard_dict:
                output_str = f"The term \"{term}\" already exists. Try again:"
                self.log_line(output_str)
                print(output_str)
                continue
            else:
                output_str = "The definition of the card:"
                self.log_line(output_str)
                print(output_str)
                while True:
                    definition = input()
                    self.log_line(definition)
                    definition_exists = False
                    for key in self.flashcard_dict.keys():
                        if definition == self.flashcard_dict[key]["Capital"]:
                            output_str = f"The definition \"{definition}\" already exists. Try again:"
                            self.log_line(output_str)
                            print(output_str)
                            definition_exists = True
                            break
                    if definition_exists:
                        continue
                    output_str = f'The pair ("{term}":"{definition}") has been added.'
                    self.log_line(output_str)
                    print(output_str)
                    self.flashcard_dict[term] = {"Capital": definition, "Errors": 0}
                    break
            break

    def remove_card(self):
        output_str = "Which card?"
        self.log_line(output_str)
        print(output_str)
        card = input()
        self.log_line(card)
        if card in self.flashcard_dict:
            del self.flashcard_dict[card]
            output_str = "The card has been removed."
            self.log_line(output_str)
            print(output_str)
        else:
            output_str = f'Can\'t remove "{card}": there is no such card.'
            self.log_line(output_str)
            print(output_str)

    def load_cards_from_file(self):
        output_str = "File name:"
        self.log_line(output_str)
        print(output_str)
        file_name = input()
        self.log_line(file_name)
        try:
            with open(f"{file_name}", "r") as in_file:
                if in_file:
                    temp_dict = json.load(in_file)
                    for key in temp_dict.keys():
                        self.flashcard_dict[key] = temp_dict[key]
                    output_str = f"{len(temp_dict)} cards have been loaded.\n"
                    self.log_line(output_str)
                    print(output_str)
        except FileNotFoundError:
            output_str = "File not found.\n"
            self.log_line(output_str)
            print(output_str)

    def save_cards_to_file(self):
        output_str = "File name:"
        self.log_line(output_str)
        print(output_str)
        file_name = input()
        self.log_line(file_name)
        try:
            with open(f"{file_name}", "w") as out_file:
                if out_file:
                    json.dump(self.flashcard_dict, out_file)
                    output_str = f"{len(self.flashcard_dict)} cards have been saved.\n"
                    self.log_line(output_str)
                    print(output_str)
        except FileNotFoundError:
            output_str = "File not found.\n"
            self.log_line(output_str)
            print(output_str)

    def ask_random_cards(self):
        if not self.flashcard_dict:
            output_str = "Empty."
            self.log_line(output_str)
            print(output_str)
            return
        try:
            output_str = "How many times to ask?"
            self.log_line(output_str)
            print(output_str)
            num_cards = int(input())
            self.log_line(str(num_cards))
        except ValueError:
            pass
        else:
            for _ in range(num_cards):
                random_key = random.choice(list(self.flashcard_dict.keys()))
                correct_answer = self.flashcard_dict[random_key]["Capital"]
                output_str = f'Print the definition of "{random_key}":'
                self.log_line(output_str)
                print(output_str)
                user_guess = input()
                self.log_line(user_guess)
                if user_guess == correct_answer:
                    output_str = "Correct!\n"
                    self.log_line(output_str)
                    print(output_str)
                else:
                    error_cnt = self.flashcard_dict[random_key]["Errors"] + 1
                    self.flashcard_dict[random_key]["Errors"] = error_cnt

                    other_key = None
                    for key in self.flashcard_dict.keys():
                        if user_guess == self.flashcard_dict[key]["Capital"]:
                            other_key = key
                            break

                    if other_key:  # If definition guess is one of the other terms
                        output_str = f"Wrong. The right answer is \"{correct_answer}\", "
                        output_str += f"but your definition is correct for \"{other_key}\".\n"
                        self.log_line(output_str)
                        print(output_str)
                    else:
                        output_str = f"Wrong. The right answer is \"{correct_answer}\".\n"
                        self.log_line(output_str)
                        print(output_str)

    def log(self):
        log_name = input("File name:\n")
        # Move cursor to index 0 of entire string
        self.logger.seek(0)
        with open(log_name, "w", encoding="utf-8") as log_file:
            for line in self.logger:
                log_file.write(line)
        print("The log has been saved.\n")

    def print_hardest_card(self):
        if not self.flashcard_dict:
            output_str = "There are no cards with errors.\n"
            self.log_line(output_str)
            print(output_str)
            return
        hardest_card = ""
        count = 0
        for key in self.flashcard_dict.keys():
            if self.flashcard_dict[key]["Errors"] > count:
                hardest_card = key
                count = self.flashcard_dict[key]["Errors"]
        if count == 0:
            output_str = "There are no cards with errors.\n"
            self.log_line(output_str)
            print(output_str)
            return
        hardest_cards = [hardest_card]
        for key in self.flashcard_dict.keys():
            if self.flashcard_dict[key]["Errors"] == count and key != hardest_card:
                hardest_cards.append(key)
        if len(hardest_cards) == 1:
            output_str = f'The hardest card is "{hardest_card}". You have {count} errors answering it.\n'
            self.log_line(output_str)
            print(output_str)
        else:
            output_str = "The hardest cards are "
            print(output_str, end="")
            index = 0
            for _ in range(len(hardest_cards)):
                if index == 0:
                    append_str = f'"{hardest_cards[index]}"'
                    output_str += append_str
                    print(append_str, end="")
                else:
                    append_str = f', "{hardest_cards[index]}"'
                    output_str += append_str
                    print(append_str, end="")
                index += 1
            append_str = f". You have {count} errors answering them.\n"
            output_str += append_str
            self.log_line(output_str)
            print(output_str)

    def reset_stats(self):
        for key in self.flashcard_dict.keys():
            self.flashcard_dict[key]["Errors"] = 0
        # TODO: Verify
        output_str = "Card statistics have been reset.\n"
        self.log_line(output_str)
        print(output_str)

    def log_line(self, a_line):
        self.logger.write(f"{a_line}\n")

    def run(self):
        while True:
            print_action = "Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):"
            print(print_action)
            user_input = input()

            self.log_line(print_action)
            self.log_line(user_input)

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
                bye_str = "Bye bye!"
                self.log_line(bye_str)
                print(bye_str)
                break
            elif user_input == Menu.LOG:
                self.log()
            elif user_input == Menu.HARD:
                self.print_hardest_card()
            elif user_input == Menu.RESET:
                self.reset_stats()
            elif user_input == Menu.PRINT:
                self.print_all_cards()
            else:
                error_str = "[Error]: That is not a valid action."
                self.log_line(error_str)
                print(error_str)


def run():
    app = Flashcards()
    app.run()


if __name__ == "__main__":
    run()
