from PIL import Image
import numpy as np
from hashlib import sha256
from utils import get_params
    
class Bin:
    def __init__(self):
        self.params = get_params()

    def SHA_256 (self):
        hash_arr = []
        
        fname = f"Images/{self.params["img"]}"
        with open(fname,"rb") as f:
            img_info = f.read() # read entire file as bytes
            readable_hash = sha256(img_info).hexdigest()
            hash_arr.append(readable_hash)
        
        for k, v in self.params.items():
            if k in ["x0", "y0", "img"]:
                continue
            hash = sha256(str(v).encode()).hexdigest()
            hash_arr.append(hash)
        return hash_arr

b = Bin()
print(b.SHA_256())