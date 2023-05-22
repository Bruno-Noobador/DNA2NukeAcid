from random import choice

DNALETTERS = "ACGT"
dna_to_rna = {'A':'U',
              'C':'G',
              'G':'C',
              'T':'A'}

def generate_random_DNA(length: int) -> str:
    random_sequence:str = ''.join(choice(DNALETTERS) for i in range(length))
    return random_sequence

def irna_tor(DnaInput: str) -> str:
    DnaInput.split().pop()
    RNAOutput: str = ''.join([dna_to_rna.get(nucleotide) for nucleotide in DnaInput])
    return RNAOutput

DnaSequence: str = generate_random_DNA(5)

UpperCasedDNA: str = DnaSequence.upper()

print(UpperCasedDNA)

RnaSequence: str = irna_tor(UpperCasedDNA)

print(RnaSequence)
