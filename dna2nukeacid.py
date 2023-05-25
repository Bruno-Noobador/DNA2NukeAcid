"""imports the custom library"""
from library import lib

dna_sequence: str = ""

with open("DNA_Input.txt", encoding="utf-8") as input_file:
    dna_sequence = lib.filter_input(input_file.read())

dna_sequence = lib.split_dna_start(dna_sequence)
print(f"dna_sequence: {dna_sequence}")

rna_sequence: str = lib.to_rna(dna_sequence)

print(f"rna_sequence: {rna_sequence}")

aminoacids:str = lib.to_aminoacid(rna_sequence)
aminoacids = lib.split_aminoacid_stop(aminoacids)
print(f"Aminoacids: {aminoacids}")

with open("Aminoacids_output.txt", "w", encoding="utf-8") as output_file:
    print("DNA translated to the corresponding aminoacids")
    output_file.write(aminoacids)
