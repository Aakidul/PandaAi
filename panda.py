import tokens
import difflib
import random
import re
import os
os.system("clear")
general_apologies = [
    "My apologies, I didn't understand. Can you rephrase that?",
    "Apologies, I'm having trouble understanding. Can you try again?",
    "Sorry, I'm not sure what you mean.",
    "Sorry,I didn't quite catch that.",
    "I'm sorry, could you please repeat that?"
]

def main():
    print ("""                                                                                                                               ⠀⣠⣶⣾⣿⣶⣦⡀⣀⣀⣀⣀⣀⣀⣀⣀⡀⣤⣶⣿⣷⣶⣄⠀
⢰⣿⣿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠉⠉⠛⢿⣿⣿⣿⣿⣇
⠸⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡏
⠀⠙⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠋⠀
⠀⠀⡞⠀⣠⣶⣿⠿⣷⡄⠀⠀⠀⠀⢠⣾⠿⢿⣶⣄⠀⢸⡀⠀
⠀⠀⢷⠀⣿⣿⣿⣦⣾⠇⠀⠛⡟⠀⢸⣿⣦⣾⣿⣿⠀⣸⠁⠀
⠀⠀⠘⣆⠙⠿⢿⣿⠟⠀⠘⢶⣷⠖⠀⠻⣿⣿⠿⠋⣠⠏⠀⠀
⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠓⠶⠤⢤⣄⣀⣤⠤⠴⠞⠋⠁⠀⠀⠀⠀⠀

[ GMLM~GENERATIVE MINI LANGUAGE MODEL ]
[ SUBSCRIBE AAKIDUL YOUTUBE CHANNEL 🐼 ]
  """)
    print("Panda: Hello! I'm Panda, your friendly chatbot.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Panda: Goodbye!")
            break
        elif is_math_question(user_input):
            answer = calculate_math(user_input)
            print("Panda: Your answer is", answer)
        else:
            response = get_response(user_input)
            print("Panda:", response)

def get_response(input_text):
    input_text_lower = input_text.lower()
    closest_match = difflib.get_close_matches(input_text_lower, tokens.patterns.keys(), n=1, cutoff=0.5)
    if closest_match:
        return random.choice(tokens.patterns[closest_match[0]])
    else:
        return random.choice(general_apologies)

def is_math_question(input_text):
    math_patterns = ["[0-9]+[+*/-][0-9]+", "[0-9]+[÷×][0-9]+", "[0-9]+[x][0-9]+", "[0-9]+[×][0-9]+"]
    for pattern in math_patterns:
        if re.search(pattern, input_text):
            return True
    return False

def calculate_math(math_expression):
    return eval(math_expression.replace('÷', '/').replace('×', '*').replace('x', '*'))

if __name__ == "__main__":
    main()
