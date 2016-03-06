def decode_uvarint(buf):
    """Decodes an unsigned 64 bit integer from byte sequence.

    Returns the value and the number of bytes read (>0). If an error occurred,
    the, the value is 0 and the number of bytes n is <= 0 meaning:
        n == 0: buf too small
        n  < 0: value larger than 64 bits (overflow)
                and -n is the number of bytes read

    """
    x, s = 0, 0
    for i, b in enumerate(buf):
        if b < 0x80:
            if i > 9 or (i == 9 and b > 1):
                return 0, -(i + 1)

            return x | int(b) << s, i + 1

        x |= int(b&0x7f) << s
        s += 7

    return 0, 0


def encode_uvarint(n):
    ret = []
    while n >= 0x80:
        b = (n & 0x7f) | 0x80
        ret.append(b)
        n >>= 7
    ret.append(n)

    return bytes(ret)
