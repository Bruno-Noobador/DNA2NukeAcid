import random

DNALETTERS = "ACGT"

def generate_random_DNA(length: int) -> str:
    random_sequence:str = ''.join(random.choice(DNALETTERS) for i in range(length))
    return random_sequence

def irna_tor(DnaInput: str) -> str:
    DnaInput.split().pop()
    RnaOutput: str = ""

    for nucleotide in UpperCasedDNA:
        if nucleotide == "A":
            RnaOutput += "U"

        if nucleotide == "C":
            RnaOutput += "G"

        if nucleotide == "G":
            RnaOutput += "C"

        if nucleotide == "T":
            RnaOutput += "A"


    return RnaOutput

DnaSequence: str = generate_random_DNA(100)

UpperCasedDNA: str = DnaSequence.upper()

print(UpperCasedDNA)

RnaSequence: str = irna_tor(UpperCasedDNA)

print(RnaSequence)
