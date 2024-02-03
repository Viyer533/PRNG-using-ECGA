import random
from bitarray import bitarray

def xor_with_random(input_bitarrays):
    
    bitarray_length = len(input_bitarrays[0])

    random_bitarray = bitarray([random.choice([0, 1]) for _ in range(bitarray_length)])

    result_bitarrays = [input_bitarray ^ random_bitarray for input_bitarray in input_bitarrays]

    return result_bitarrays