from pypdb import *

# build query from PDB service
sequence_similarity = input("Enter sequence similarity: ")
sequence_type = input("Enter sequence type: ")  
evalue_cutoff = input("Enter evalue cutoff: ")
identity_cutoff = input("Enter identity cutoff: ")

# query elements displayed as [sequence_similarity, sequence_type, evalue_cutoff, identity_cutoff]
query_elements = [sequence_similarity, sequence_type, evalue_cutoff, identity_cutoff]
print(str(query_elements))

# need to test for empty inputs and validate inputs

query_keys = ["Sequence Similarity", "Sequence Type", "E-value Cutoff", "Identity Cutoff"]
query_values = [sequence_similarity, sequence_type, evalue_cutoff, identity_cutoff]

query_string = " AND ".join([f"{key} = {value}" for key, value in zip(query_keys, query_values)])
# grab data from PDB database using PyPDB
found_pdbs = Query(str(query_elements)).search()
print('result: ' + str(found_pdbs[:10])) # print first 10 PDBs

# grab data from PubChem database

# PubChem data must be - confirmatory, testing substance with same inChIKey as PDB ligand
