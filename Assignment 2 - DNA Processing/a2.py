def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATCGAT')
    True
    >>> is_valid_sequence('ATCGaT')
    False
    >>> is_valid_sequence('ATWGAT')
    False
    """
    for char in dna:
        if char not in "ATCG":
            return False            
    return True

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    """    
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(dna):
    """ (char) -> char

    Return the nucleotide's complement. We have intentionally not given you any examples for this function.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    return complement.get(dna, "")

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    """
    complementary_sequence = ''
    for nucleotide in dna:
        complementary_sequence += get_complement(nucleotide)
    return complementary_sequence
