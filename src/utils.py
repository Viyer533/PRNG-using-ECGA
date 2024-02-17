from bitstring import BitArray
import numpy as np


def get_params():
    im = "4.2.03.tiff"
    # p = 23
    upper_phi = 25
    psi = 73
    lower_phi = 121
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
    a = 115792089210356248762697446949407573530086143415290314195533631308867097853948
    b = 41058363725152142129326129780047268409114441015993725554835256314039467401291
    x0 = 48439561293906451759052585252797914202762949526041747995844080717082404635286
    y0 = 36134250956749795798585127919587881956611106672985015071877198253568414405109
    G0 = (x0, y0)
    n = 5
    return {
        "img": im,
        "p": p,
        "a": a,
        "b": b,
        "G0": G0,
        "n": n,
        "upper_phi": upper_phi,
        "psi": psi,
        "lower_phi": lower_phi,
    }


def convert_to_bin(src: int, base: int = 2) -> BitArray:
    hex_representation = hex(src)
    bitarray = BitArray(hex=hex_representation)
    return bitarray


def convert_to_decimal(bitarray: np.ndarray) -> int:
    return np.packbits(bitarray)


if __name__ == "__main__":
    print(convert_to_bin("200", 10))
