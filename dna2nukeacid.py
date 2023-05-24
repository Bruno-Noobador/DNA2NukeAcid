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

def irna_tor(DnaInput: str) -> str:
    DnaInput.split().pop()
    rna_output: str = ''.join([dna_to_rna.get(nucleotide) for nucleotide in DnaInput])
    return rna_output

def amino_acid_inator(RnaInput: str) -> str:
    properly_separated_rna = []
    for n in range(0, len(RnaInput), 3):
        properly_separated_rna.append(''.join(RnaInput[n:n+3]))
    
    print(f"ProperlySeparatedRNA: {properly_separated_rna}")

    aminoacid_output: str = ' '.join([rna_to_aminoacid.get(aminoacid) for aminoacid in properly_separated_rna])
    return aminoacid_output

dna_sequence: str = ""

with open("DNA_Input.txt") as input_file:
    dna_sequence = input_file.read()

upper_cased_dna: str = dna_sequence.upper()

print(f"DnaSequence: {upper_cased_dna}")

rna_sequence: str = irna_tor(upper_cased_dna)

print(f"rna_sequence: {rna_sequence}")

aminoacids:str = amino_acid_inator(rna_sequence)
print(f"Aminoacids: {aminoacids}")
