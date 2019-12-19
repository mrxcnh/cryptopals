import sys

C = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwzyz0123456789+/'


def base64_encode(b: bytes) -> str:
    o = ''
    l = len(b) // 3
    for i in range(0, l):
        k = 3 * i
        g1 = b[k] >> 2
        g2 = ((b[k] & 0x03) << 4) | (b[k+1] >> 4)
        g3 = ((b[k+1] & 0x0F) << 2) | (b[k+2] >> 6)
        g4 = b[k+2] & 0x3F

        o += C[g1] + C[g2] + C[g3] + C[g4]
    
    r = len(b) % 3
    if r == 1:
        g1 = b[l] >> 2                                               
        g2 = ((b[l] & 0x03) << 4) | (b[l+1] >> 4)
        o += C[g1] + C[g2] + '=='

    if r == 2:
        g1 = b[l] >> 2
        g2 = ((b[l] & 0x03) << 4) | (b[l+1] >> 4)                               
        g3 = ((b[l+1] & 0x0F) << 2) | (b[l+2] >> 6)
        o += C[g1] + C[g2] + C[g3] + '='

    return o


if _name_ == '_main_':
    str_in = sys.argv[1]
    print(base64_encode(bytes.fromhex(str_in)))
