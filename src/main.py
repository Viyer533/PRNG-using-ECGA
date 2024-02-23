import numpy as np
from EC_init import EC
from Hash import Hash
from utils import get_params, convert_to_bin
from Bin_Handlers import (
    merge_bits,
    concat_bits,
    bitmasking,
    initial_prng,
    prng_sequence,
)
from Optimisation import optimisation

params = get_params()
ec = EC()
hash_handler = Hash()
points_arr = ec.gen_points(params["n"])
hash_dict = hash_handler.sha_256()
i_prns = np.array([])

for G in points_arr:
    x, y = G
    bin_x, bin_y = convert_to_bin(x), convert_to_bin(y)
    bin_x_merged = merge_bits(hash_dict["a"], bin_x, hash_dict["b"])
    bin_y_merged = merge_bits(hash_dict["img"], bin_y, hash_dict["p"])
    bin_xy = concat_bits(bin_x_merged, bin_y_merged)
    bin_xyz = bitmasking(bin_xy)
    bin_dec_arr = initial_prng(bin_xyz)
    i_prns = np.concatenate(
        [
            i_prns,
            prng_sequence(
                bin_dec_arr, params["upper_phi"], params["psi"], params["lower_phi"]
            ),
        ]
    )


if __name__ == "__main__":
    print(i_prns)
    o_prns = optimisation(i_prns)
    print(o_prns)
    # np.save('Optimized_PRNS.npy', o_prns)