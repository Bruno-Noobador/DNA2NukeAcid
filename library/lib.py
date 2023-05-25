"""Constant for the letters used in the DNA"""
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

def to_rna(dna_input: str) -> str:
    """Converts DNA input into RNA with the dna_to_rna dict"""
    dna_input.split().pop()
    rna_output: str = ''.join([dna_to_rna.get(nucleotide) for nucleotide in dna_input])
    return rna_output

def to_aminoacid(rna_input: str) -> str:
    """Converts RNA into aminoacids using the rna_to_aminoacids dict"""
    codons = []
    for nucleotide in range(0, len(rna_input), 3):
        codons.append(''.join(rna_input[nucleotide:nucleotide+3]))
    if len(codons[-1]) < 3:
        codons.pop()
    print(f"codons: {codons}")

    aminoacid_output: str = ' '.join([rna_to_aminoacid.get(aminoacid) for aminoacid in codons])
    print(f"aminoacid_output: {aminoacid_output}")
    if "Stop" not in aminoacid_output:
        raise ValueError("Invalid DNA Input: no stop codon")
    return aminoacid_output

def filter_input(dna_sequence: str) -> str:
    """removes invalid characters and capitalizes the DNA input"""
    dna_sequence = dna_sequence.upper()
    if "TAC" not in dna_sequence:
        raise ValueError("Invalid DNA Input: no starting sequence in DNA")
    index:int = 0
    for nucletide in dna_sequence:
        index += 1
        if nucletide not in DNALETTERS:
            raise ValueError(f"Invalid DNA Input: invalid nucleotide at position {index}")
    return dna_sequence

def split_dna_start(dna_sequence: str) -> str:
    """Cuts the DNA at the starting sequence"""
    filtered_dna_sequence = "TAC" + dna_sequence.split("TAC", 1)[-1]
    return filtered_dna_sequence

def split_aminoacid_stop(aminoacids: str) -> str:
    """Cuts the aminoacid at any of the stop sequences"""
    filtered_aminoacids = aminoacids.split("Stop", 1)[0] + "Stop"
    return filtered_aminoacids
