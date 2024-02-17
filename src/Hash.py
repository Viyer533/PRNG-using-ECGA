from PIL import Image
import numpy as np
from hashlib import sha256
from utils import get_params, convert_to_bin
from bitstring import BitArray
import os


class Bin:
    def __init__(self):
        self.params = get_params()

    def sha_256(self):
        hash_dict = {}
        file_prefix = '../Images' if os.name == 'posix' else './Images'
        fname = f'{file_prefix}/{self.params["img"]}'
        with open(fname, "rb") as f:
            img_info = f.read()  # read entire file as bytes
            hash_hex = f'0x{sha256(img_info).hexdigest()}'
            hash_dict['img'] = BitArray(hex=hash_hex)

        for k, v in self.params.items():
            if k in ["x0", "y0", "img"]:
                continue
            hash_hex = f'0x{sha256(str(v).encode()).hexdigest()}'
            hash_dict[k] = BitArray(hex=hash_hex)
        return hash_dict

    def merge_bits(self, bit_vec: BitArray, h1:str, h2:str) -> BitArray:
        h_dict  = self.sha_256() 
        bin_len = min(len(bit_vec), 256)
        bin_res = BitArray()
        print(type(bin_res))
        bin_arrs = [h_dict[h1], bit_vec, h_dict[h2]]
        print("in merge bits fn")
        for i in range(3*bin_len):
            for arr in bin_arrs:
                if i < len(arr):
                    bin_res.append(BitArray(arr[i]))
        #     if i < bin_res.
        # for bit1, bit2, bit3 in zip(h_dict[h1], bit_vec, h_dict[h2]):
        #     print(f"bit1:{bit1},bit2:{bit2},bit3:{bit3}\n")
        #     if len(bin_res) >= 3*bin_len:
        #         return bin_res
        #     bin_res.append(BitArray(bool = bit1))
        #     bin_res.append(BitArray(bool = bit2))
        #     bin_res.append(BitArray(bool = bit3))
        return bin_res
    
    def concat_bits(self, bit_vec_x: BitArray, bit_vec_y: BitArray) -> BitArray:
        bit_vec_x.append(bit_vec_y)
        return bit_vec_x
    
b = Bin()
print(b.sha_256())
print(b.merge_bits(BitArray(hex='0xc8'),'a','b'))
print(b.concat_bits(BitArray(hex = '0xc8'),BitArray(hex = '0xd9')))