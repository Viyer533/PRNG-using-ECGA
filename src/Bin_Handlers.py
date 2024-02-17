from utils import get_params, convert_to_bin
from bitstring import BitArray
import numpy as np

def merge_bits(self, bit_vec: BitArray, h1:BitArray, h2:BitArray) -> BitArray:
        bin_len = min(len(bit_vec), 256)
        bin_res = BitArray(length = 3*bin_len)
    
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