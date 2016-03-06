import varint

def test_encode_decode():
    sample = [(0, 1), (100, 1), (1314, 2), (123456, 3), (123456789, 4)]
    for x, n in sample:
        buf = varint.encode_uvarint(x)
        x_, n_ = varint.decode_uvarint(buf)
        assert x == x_
        assert n == n_
