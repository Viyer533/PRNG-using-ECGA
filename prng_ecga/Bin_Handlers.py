from bitstring import BitArray
import numpy as np
from prng_ecga.utils import get_params, convert_to_decimal


def merge_bits(bit_vec: BitArray, b1: BitArray, b2: BitArray) -> BitArray:
    bin_len = min(len(bit_vec), 256)

    interleaved = BitArray()

    for bit1, bit2, bit3 in zip(b1.bin, bit_vec.bin, b2.bin):

        if len(interleaved) < 3 * bin_len:
            extension1 = BitArray(bin=bit1)
            extension2 = BitArray(bin=bit2)
            extension3 = BitArray(bin=bit3)

            interleaved.append(extension1)
            interleaved.append(extension2)
            interleaved.append(extension3)

    return interleaved


def concat_bits(bit_vec_x: BitArray, bit_vec_y: BitArray) -> BitArray:
    bit_vec_x.append(bit_vec_y)
    return bit_vec_x


def bitmasking(input_bitarray: BitArray) -> BitArray:
    bitarray_length = len(input_bitarray)
    rand_b = np.mod(
        np.reshape(np.random.permutation(1 * bitarray_length), (1, bitarray_length)), 2
    ).flatten()
    result_bitarray = BitArray(
        uint=input_bitarray.uint ^ int("".join(map(str, rand_b)), 2),
        length=bitarray_length,
    )
    return result_bitarray


def initial_prng(input_bitarray: BitArray, m: int = 8) -> np.ndarray:
    l1 = len(input_bitarray)
    l2 = l1 % m
    l3 = l1 - l2

    result_bitarray = input_bitarray[:l3]
    reshaped_bitarray = np.reshape(result_bitarray, (m, -1))
    result_decimals = np.apply_along_axis(
        convert_to_decimal, 0, reshaped_bitarray
    ).flatten()

    return result_decimals


def prng_sequence(
    seq: np.ndarray, upper_phi: int, psi: int, lower_phi: int, m: int = 8
) -> np.ndarray:
    final_seq_len = len(seq) - 1
    final_seq = np.empty(final_seq_len)
    for idx in range(final_seq_len):
        final_seq[idx] = (upper_phi * seq[idx] + psi * seq[idx + 1] + lower_phi) % (
            2**m
        )
    return final_seq


if __name__ == "__main__":
    input_bitarray = BitArray(bin="110010100100011110101010111010110001010101010100010")
    result = initial_prng(bitmasking(input_bitarray))
    print(result)
    upper_phi, lower_phi, psi = (
        get_params()["upper_phi"],
        get_params()["lower_phi"],
        get_params()["psi"],
    )
    res = prng_sequence(result, upper_phi, psi, lower_phi)
    print(res)
