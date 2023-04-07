import handin4

'''Test the test of the read_data function'''
fasta_dict = handin4.read_fasta('Ecoli.prot.fasta')
print(len(fasta_dict))

'''Test the test of the find_prot function'''
yhcn = handin4.find_prot(fasta_dict, 'YHCN_ECOLI')

'''Test the test of the find_prot function'''
boom = handin4.find_prot(fasta_dict, 'BOOM_ECOLI')

'''Test the test of the find_prot2 function'''
matches = handin4.find_prot2(fasta_dict, '\\A..._ECOLI')
print(len(matches))