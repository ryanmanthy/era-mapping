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

# return InChi key from PDB database
#     Parameters
#     ----------

#     pdb_id : string
#         A 4 character string giving a pdb entry of interest

#     Returns
#     -------

#     out : dict
#         A dictionary containing a list of ligands associated with the entry

#     Examples
#     --------
#     >>> ligand_dict = get_ligands('100D')
#     >>> print(ligand_dict)
#     {'id': '100D',
#     'ligandInfo': {'ligand': {'@chemicalID': 'SPM',
#                            '@molecularWeight': '202.34',
#                            '@structureId': '100D',
#                            '@type': 'non-polymer',
#                            'InChI': 'InChI=1S/C10H26N4/c11-5-3-9-13-7-1-2-8-14-10-4-6-12/h13-14H,1-12H2',
#                            'InChIKey': 'PFNFFQXMRSDOHW-UHFFFAOYSA-N',
#                            'chemicalName': 'SPERMINE',
#                            'formula': 'C10 H26 N4',
#                            'smiles': 'C(CCNCCCN)CNCCCN'}}}

#     """
#     out = get_info(pdb_id, url_root = 'http://www.rcsb.org/pdb/rest/ligandInfo?structureId=')
#     out = to_dict(out)
#     return remove_at_sign(out['structureId'])

# grab data from PubChem database

# PubChem data must be - confirmatory, testing substance with same inChIKey as PDB ligand

# use inChIKey to search PubChem database
