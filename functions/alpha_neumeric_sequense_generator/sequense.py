"""Alphaneumeric sequense generator."""
from sequence_generator import SeqGen


def increment(sequence, seq):
    """Increment the left hand side of aplha part."""
    seq.rollover_len = len(sequence) + 1
    seq.value = sequence[::-1]
    return (SeqGen.next(seq)[::-1])


def generate_sequence(sequence):
    """Unique aplha numeric sequence generator."""
    if sequence[len(sequence) - 1] == 'Z':
        return sequence + "A"

    s = SeqGen(26, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if sequence[0].isdigit() and sequence[0] == '9':
        sequence = list(sequence)
        sequence[0] = 'A'
        sequence = ''.join(sequence)
    elif sequence[0] == 'Z':
        sequence = list(sequence)
        sequence[0] = '0'
        sequence = ''.join(sequence)
        sequence = sequence[0] + increment(sequence[1:], s)
    else:
        sequence = list(sequence)
        sequence[0] = (chr(ord(sequence[0]) + 1))
        sequence = ''.join(sequence)
    return sequence