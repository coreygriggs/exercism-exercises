
def to_rna(strand):
    complement_dicts = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    transcription = ''
    for nucleotide in strand:
        transcription += complement_dicts.get(nucleotide)
    return transcription

