from random import choice

DNALETTERS = "ACGT"
dna_to_rna = {'A':'U',
              'C':'G',
              'G':'C',
              'T':'A'}

rna_to_aminoacid = {'UUU': 'Phe',
                    'UUC': 'Phe',
                    'UUA': 'Leu',
                    'UUG': 'Leu',
                    'UCU': 'Ser',
                    'UCC': 'Ser',
                    'UCA': 'Ser',
                    'UCG': 'Ser',
                    'UAU': 'Tyr',
                    'UAC': 'Tyr',
                    'UAA': 'Stop',
                    'UAG': 'Stop',
                    'UGU': 'Cys',
                    'UGC': 'Cys',
                    'UGA': 'Stop',
                    'UGG': 'Trp',

                    'CUU': 'Leu',
                    'CUC': 'Leu',
                    'CUA': 'Leu',
                    'CUG': 'Leu',
                    'CCU': 'Pro',
                    'CCC': 'Pro',
                    'CCA': 'Pro',
                    'CCG': 'Pro',
                    'CAU': 'His',
                    'CAC': 'His',
                    'CAA': 'Gln',
                    'CAG': 'Gln',
                    'CGU': 'Arg',
                    'CGC': 'Arg',
                    'CGA': 'Arg',
                    'CGG': 'Arg',
                    
                    'AUU': 'Ile',
                    'AUC': 'Ile',
                    'AUA': 'Ile',
                    'AUG': 'Met',
                    'ACU': 'Thr',
                    'ACC': 'Thr',
                    'ACA': 'Thr',
                    'ACG': 'Thr',
                    'AAU': 'Asn',
                    'AAC': 'Asn',
                    'AAA': 'Lys',
                    'AAG': 'Lys',
                    'AGU': 'Ser',
                    'AGC': 'Ser',
                    'AGA': 'Arg',
                    'AGG': 'Arg',
                    
                    'GUU': 'Val',
                    'GUC': 'Val',
                    'GUA': 'Val',
                    'GUG': 'Val',
                    'GCU': 'Ala',
                    'GCC': 'Ala',
                    'GCA': 'Ala',
                    'GCG': 'Ala',
                    'GAU': 'Asp',
                    'GAC': 'Asp',
                    'GAA': 'Glu',
                    'GAG': 'Glu',
                    'GGU': 'Gly',
                    'GGC': 'Gly',
                    'GGA': 'Gly',
                    'GGG': 'Gly'}

def generate_random_DNA(length: int) -> str:
    random_sequence:str = ''.join(choice(DNALETTERS) for i in range(length*3))
    return random_sequence

def irna_tor(DnaInput: str) -> str:
    DnaInput.split().pop()
    RNAOutput: str = ''.join([dna_to_rna.get(nucleotide) for nucleotide in DnaInput])
    return RNAOutput

def amino_acid_inator(RnaInput: str) -> str:
    ProperlySeparatedRNA = []
    for n in range(0, len(RnaInput), 3):
        ProperlySeparatedRNA.append(''.join(RnaInput[n:n+3]))
    
    print(f"ProperlySeparatedRNA: {ProperlySeparatedRNA}")

    AminoacidOutput: str = ' '.join([rna_to_aminoacid.get(aminoacid) for aminoacid in ProperlySeparatedRNA])
    return AminoacidOutput

DnaSequence: str = generate_random_DNA(10)

UpperCasedDNA: str = DnaSequence.upper()

print(f"DnaSequence: {UpperCasedDNA}")

RnaSequence: str = irna_tor(UpperCasedDNA)

print(f"RnaSequence: {RnaSequence}")

NucleicAcids:str = amino_acid_inator(RnaSequence)
print(f"NucleicAcids: {NucleicAcids}")
