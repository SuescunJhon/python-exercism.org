def to_rna(dna_strand):
    if not dna_strand: return ""
        
    translator = {'G': 'C',
                'C': 'G',
                'T': 'A',
                'A': 'U'}

    return "".join(translator[nuc] for nuc in dna_strand)