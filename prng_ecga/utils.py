from bitstring import BitArray
import numpy as np
from prng_ecga.config import config

def get_params():
    G0 = (config["x0"], config["y0"])
    return {
        "img": config["img"],
        "p": config["p"],
        "a": config["a"],
        "b": config["b"],
        "G0": G0,
        "n": config["n"],
        "upper_phi": config["upper_phi"],
        "psi": config["psi"],
        "lower_phi": config["lower_phi"],
        "m" : config["m"],
    }

def convert_to_bin(src: int, base: int = 2) -> BitArray:
    hex_representation = hex(src)
    bitarray = BitArray(hex=hex_representation)
    return bitarray


def convert_to_decimal(bitarray: np.ndarray) -> int:
    return abs(int.from_bytes(np.packbits(bitarray), byteorder="big"))


if __name__ == "__main__":
    print(convert_to_bin("200", 10))
