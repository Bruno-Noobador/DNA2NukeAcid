"""Imports the choice function from the standart random library"""
from random import choice

DNALETTERS = "ACGT"

def generate(length: int) -> str:
    """Generate a random dna sequence with a valids starting sequence"""
    random_sequence:str = ''.join(choice(DNALETTERS) for i in range(length))

    if "TAC" not in random_sequence or random_sequence[-1] == "TAC":
        random_sequence = generate(length)
    return random_sequence

DnaSequence: str = generate(100)

with open("DNA_Input.txt", "w",encoding="utf-8") as InputFile:
    print("Random DNA generated")
    InputFile.write(DnaSequence)
    