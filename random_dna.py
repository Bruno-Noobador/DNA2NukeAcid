from random import choice

DNALETTERS = "ACGT"

def generate(length: int) -> str:
    random_sequence:str = ''.join(choice(DNALETTERS) for i in range(length*3))
    return random_sequence

DnaSequence: str = generate(5)

with open("DNA_Input.txt", "w") as InputFile:
    print("Random DNA generated")
    InputFile.write(DnaSequence)