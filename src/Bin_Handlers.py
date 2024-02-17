from utils import get_params, convert_to_bin
from bitstring import BitArray
from Hash import Bin
import numpy as np


def merge_bits(bit_vec: BitArray, b1:BitArray, b2:BitArray) -> BitArray:
    bin_len = min(len(bit_vec), 256)
        
    interleaved = BitArray()

    for bit1, bit2, bit3 in zip(b1.bin, bit_vec.bin, b2.bin):

        if len(interleaved) < 3*bin_len:

            extension1 = BitArray(bin=bit1)
            extension2 = BitArray(bin=bit2)
            extension3 = BitArray(bin=bit3)

            interleaved.append(extension1)
            interleaved.append(extension2)
            interleaved.append(extension3)
            
    return interleaved
        
    
def concat_bits(self, bit_vec_x: BitArray, bit_vec_y: BitArray) -> BitArray:
    bit_vec_x.append(bit_vec_y)
    return bit_vec_x

def bitmasking(input_bitarray: BitArray) -> BitArray:
    bitarray_length = len(input_bitarray)
    rand_b = np.mod(np.reshape(np.random.permutation(1 * bitarray_length), (1, bitarray_length)), 2).flatten()
    result_bitarray = BitArray(uint=input_bitarray.uint ^ int(''.join(map(str, rand_b)), 2), length=bitarray_length)
    return result_bitarray

if __name__ == '__main__':
    input_bitarray = BitArray(bin = '11001010')
    result = bitmasking(input_bitarray)
    print(result.bin)
    res = merge_bits(BitArray(bin = '1010101'), BitArray(bin = '110101011'), BitArray(bin = '101010110'))
    print(res.bin)
