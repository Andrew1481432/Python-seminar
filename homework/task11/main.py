from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
)


def parse(buf, offs, ty):
    return unpack_from(FMT[ty], buf, offs)[0], offs + calcsize(FMT[ty])


def parse_a(buf, offs):
    a1_offs, offs = parse(buf, offs, 'uint16') # Адрес (uint16) структуры B
    a1, a1_offs = parse_b(buf, a1_offs)
    a2, offs = parse(buf, offs, 'uint16')  # uint16
    a3, offs = parse(buf, offs, 'int8')  # int8

    # region Массив uint8, размер 3
    a4_size = 3
    a4 = []
    for _ in range(a4_size):
        val, offs = parse(buf, offs, 'uint8')
        a4.append(val)
    # endregion

    a5, offs = parse(buf, offs, 'int32')  # int32
    a6, offs = parse(buf, offs, 'int8')  # int8
    a7, offs = parse(buf, offs, 'uint32')  # uint32

    # region Массив uint64, размер 2
    a8_size = 2
    a8 = []
    for _ in range(a8_size):
        val, offs = parse(buf, offs, 'uint64')
        a8.append(val)
    # endregion

    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8), offs


def parse_b(buf, offs):
    b1_offs, offs = parse(buf, offs, 'uint16')  # Адрес(uint16) структуры C
    b1, b1_offs = parse_c(buf, b1_offs)
    b2, offs = parse(buf, offs, 'uint32')  # uint32
    b3, offs = parse(buf, offs, 'float')  # float
    b4, offs = parse(buf, offs, 'uint8')  # uint8
    b5, offs = parse(buf, offs, 'uint32')  # uint32
    b6, offs = parse(buf, offs, 'int16')  # int16
    b7, offs = parse(buf, offs, 'int32')  # int32

    # region Размер (uint16) и адрес (uint16) массива структур D
    b8_size, offs = parse(buf, offs, 'uint16')
    b8_offs, offs = parse(buf, offs, 'uint16')
    b8 = []
    for i in range(b8_size):
        val, b8_offs = parse_d(buf, b8_offs)
        b8.append(val)
    # endregion

    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8), offs


def parse_c(buf, offs):
    c1, offs = parse(buf, offs, 'uint32')  # uint32
    # region Размер (uint32) и адрес (uint32) массива char
    c2_size, offs = parse(buf, offs, 'uint32')
    c2_offs, offs = parse(buf, offs, 'uint32')
    c2 = []
    for _ in range(c2_size):
        val, c2_offs = parse(buf, c2_offs, 'char')
        c2.append(val.decode())
    # endregion
    return dict(C1=c1, C2=''.join(c2)), offs


def parse_d(buf, offs):
    # region Размер (uint32) и адрес (uint16) массива uint64
    d1_size, offs = parse(buf, offs, 'uint32')  # Размер (uint32)
    d1_offs, offs = parse(buf, offs, 'uint16')  # адрес (uint16)
    d1 = []
    for _ in range(d1_size):
        val, d1_offs = parse(buf, d1_offs, 'uint64')  # массива uint64
        d1.append(val)
    # endregion
    d2, offs = parse(buf, offs, 'uint8')  # uint8

    return dict(D1=d1, D2=d2), offs


def main(buf):
    return parse_a(buf, 3)[0]


data = (b'WINh\x00;\x13\xfb\x07\x91\xf5_\x9f\xf0\x1b\xc5\x89\x1d\xdb\xeb'
        b'\x80\xa4\xd0\xf8\n7_\xc8W\xad\xb9\xe0\xa6\xa2\xd49bj\x8c\xb6{J\x02\x00'
        b'\x00\x00$\x00\x00\x00\xcd\xbf38\x99\xa6ydq\xbf\xca\xbe\xc4\x81Z\xedNj'
        b'\xc1H\x14\x8b\xf4\xea\xf1vK\xa3\x19N\xd6\x9d\xb2\x9b\xd0\x03U\x93'
        b'b\x14\x03\x00\x00\x002\x00\x1c\x02\x00\x00\x00J\x00\r&\x00gw\xf1pg\x12'
        b'z?\x88R\xee&\t\xe3\xe7^\xa7\x95d\x02\x00Z\x00')

print(main(data))

data1 = (b'WINa\x00^\xd6\xccMxBcFB-\xee\x02QHb\x0b6\xed<\x00"\xfa\x92\xc1\x8f\xaaS'
         b'B%\x99\\sjkd\x8dd3\x03\x00\x00\x00$\x00\x00\x00\x0f\x83\xc8\x15D\x98\xe12z'
         b'\xf1\xee\xf5B\xdf\xd3DR^\xcd\xeaRw)x\xe3\xf4\xbd+\xb2\x80\xe9\xd2\x02'
         b"\x00\x00\x003\x005\x02\x00\x00\x00C\x00\xde'\x00\x06=\xe7S\x0coh?\xc8"
         b'\xa1\xf4%\x0e\x8f\xf4\x7f\xa15\xfb\x02\x00S\x00')
print(main(data1))
