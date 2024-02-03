from PIL import Image
import numpy as np
from hashlib import sha256
from utils import get_params
from bitstring import BitArray
import os


class Bin:
    def __init__(self):
        self.params = get_params()

    def sha_256(self):
        hash_arr = []
        file_prefix = '../Images' if os.name == 'posix' else './Images'
        fname = f'{file_prefix}/{self.params["img"]}'
        with open(fname, "rb") as f:
            img_info = f.read()  # read entire file as bytes
            hash_hex = f'0x{sha256(img_info).hexdigest()}'
            hash_bin = BitArray(hex=hash_hex).bin
            hash_arr.append(hash_bin)

        for k, v in self.params.items():
            if k in ["x0", "y0", "img"]:
                continue
            hash_hex = f'0x{sha256(str(v).encode()).hexdigest()}'
            hash_bin = BitArray(hex=hash_hex).bin
            hash_arr.append(hash_bin)
        return hash_arr


b = Bin()
print(b.sha_256())
