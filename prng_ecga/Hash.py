from hashlib import sha256
from bitstring import BitArray
from PIL import Image
import os
from prng_ecga.utils import get_params


class Hash:

    def __init__(self):
        self.params = get_params()

    def sha_256(self):
        hash_dict = {}
        # file_prefix = "../Images" if os.name == "posix" else "./Images"
        # fname = f'{file_prefix}/{self.params["img"]}'
        fname = f'{self.params["img"]}'
        
        with open(fname, "rb") as f:
            img_info = f.read()
            hash_hex = f"0x{sha256(img_info).hexdigest()}"
            hash_dict["img"] = BitArray(hex=hash_hex)

        for k, v in self.params.items():
            if k in ["a", "p", "b"]:
                hash_hex = f"0x{sha256(str(v).encode()).hexdigest()}"
                hash_dict[k] = BitArray(hex=hash_hex)
        return hash_dict
