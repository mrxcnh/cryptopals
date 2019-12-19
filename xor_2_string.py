import sys

def change_to_hex(str_in: str) -> int:
    return int(str_in, base=16)


def xor_2_string(str_1, str_2):
    int_1 = change_to_hex(str_1)
    int_2 = change_to_hex(str_2)
    return str(hex(int_1 ^ int_2))[2:]


if __name__ == '__main__':
    out = xor_2_string(sys.argv[1], sys.argv[2])
    print(out)

