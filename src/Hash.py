from PIL import Image
import numpy as np
from hashlib import sha256
from utils import get_params, convert_to_bin
from bitstring import BitArray
import os


class Hash:
    
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
      