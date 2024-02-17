from utils import get_params, convert_to_bin
from bitstring import BitArray


def merge_bits(self, bit_vec: BitArray, h1:BitArray, h2:BitArray) -> BitArray:
        bin_len = min(len(bit_vec), 256)
        bin_res = BitArray(length = 3*bin_len)
        print(type(bin_res))
        
    
def concat_bits(self, bit_vec_x: BitArray, bit_vec_y: BitArray) -> BitArray:
    bit_vec_x.append(bit_vec_y)
    return bit_vec_x

