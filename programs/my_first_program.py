from nada_dsl import *
import random

def generate_random_name(length):
    name = []
    for _ in range(length):
        random_char = random.randint(97, 122)  # Random lowercase ASCII character (a-z)
        name.append(random_char)
    return "".join(chr(char) for char in name)

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Generate random names (5 characters each)
    person1_name = generate_random_name(5)
    person2_name = generate_random_name(5)

    # Calculate the love index using the secret integers
    love_index = my_int1+my_int2

    # Get the first letter of each person's name
    person1_initial = person1_name[0]
    person2_initial = person2_name[0]

    # Create the output message
    love_message = f"{person1_name} ({person1_initial}) ❤️ {person2_name} ({person2_initial}):"

    return [Output(love_index, love_message, party1)]








