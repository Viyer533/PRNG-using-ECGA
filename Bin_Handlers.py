from PIL import Image
import numpy as np
from hashlib import sha256
from Input_Params import get_params

# class Images:
#     def __init__(self):
#         self.fname = get_params()["img"]

#     def image_proc(self):
#         img = Image.open(f"Images/{self.fname}")
#         # img.show()
#         img = np.array(img)
#         img_vec = img.flatten().reshape(1,-1)
#         print(img_vec)
#         return img_vec
    
class Bin:
    def __init__(self):
        self.params = get_params()

    #def dec_to_bin_str(self, x = None, y = None):
        

    def SHA_256 (self):
        hash_arr = []
        # img = Images() #self.params["img"]
        # img_vec = img.image_proc()
        #
        fname = f"Images/{self.params["img"]}"
        with open(fname,"rb") as f:
            bytes = f.read() # read entire file as bytes
            readable_hash = sha256(bytes).hexdigest()
            hash_arr.append(readable_hash)
        
        for k, v in self.params.items():
            if k in ["x0", "y0", "img"]:
                continue
            hash = sha256(str(v).encode()).hexdigest()
            hash_arr.append(hash)
        return hash_arr

b = Bin()
print(b.SHA_256())