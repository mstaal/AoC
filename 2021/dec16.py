from functools import reduce
from utils import AoCHelper as helper


class Packet:
    def __init__(self, packet_version, tail):
        self.packet_version = packet_version
        self.tail = tail


class Literal(Packet):
    def __init__(self, packet_version, value, tail):
        super().__init__(packet_version, tail)
        self.value = value

    def get_value(self):
        return self.value

    def __repr__(self):
        return f"(Version: {self.packet_version}, Value: {self.value})"

    def get_version_sum(self):
        return self.packet_version


class Operator(Packet):
    def __init__(self, packet_version, tail):
        super().__init__(packet_version, tail)
        self.value = []

    def __repr__(self):
        return f"(Version: {self.packet_version})"

    def get_version_sum(self):
        return self.packet_version + sum(val.get_version_sum() for val in self.value)

    def append(self, packet):
        self.value.append(packet)


class Sum(Operator):
    def __init__(self, packet_version, tail):
        super().__init__(packet_version, tail)

    def get_value(self):
        return sum([element.get_value() for element in self.value])


class Product(Operator):
    def __init__(self, packet_version, tail):
        super().__init__(packet_version, tail)

    def get_value(self):
        return reduce(lambda x, y: x*y, [element.get_value() for element in self.value])


class Minimum(Operator):
    def __init__(self, packet_version, tail):
        super().__init__(packet_version, tail)

    def get_value(self):
        return min([element.get_value() for element in self.value])


class Maximum(Operator):
    def __init__(self, packet_version, tail):
        super().__init__(packet_version, tail)

    def get_value(self):
        return max([element.get_value() for element in self.value])


class Greater(Operator):
    def __init__(self, packet_version, tail):
        super().__init__(packet_version, tail)

    def get_value(self):
        return 1 if self.value[0].get_value() > self.value[1].get_value() else 0


class Less(Operator):
    def __init__(self, packet_version, tail):
        super().__init__(packet_version, tail)

    def get_value(self):
        return 1 if self.value[0].get_value() < self.value[1].get_value() else 0


class Equal(Operator):
    def __init__(self, packet_version, tail):
        super().__init__(packet_version, tail)

    def get_value(self):
        return 1 if self.value[0].get_value() == self.value[1].get_value() else 0


def hex_to_bin(h):
    b = f"{int(h, 16):b}"
    return '0' * (len(h) * 4 - len(b)) + b


def buildOperator(packet_version, type_id, tail):
    if type_id == 0:
        return Sum(packet_version, tail)
    elif type_id == 1:
        return Product(packet_version, tail)
    elif type_id == 2:
        return Minimum(packet_version, tail)
    elif type_id == 3:
        return Maximum(packet_version, tail)
    elif type_id == 5:
        return Greater(packet_version, tail)
    elif type_id == 6:
        return Less(packet_version, tail)
    elif type_id == 7:
        return Equal(packet_version, tail)


def generate_packet(binary):
    packet_version = int(binary[0:3], 2)
    type_id = int(binary[3:6], 2)
    if type_id == 4:
        pieces = [binary[0:6]]
        remainder = binary[6:]
        while remainder[0] == '1':
            pieces.append(remainder[1:5])
            remainder = remainder[5:]
        pieces.append(remainder[1:5])
        remainder = remainder[5:]
        value = int(''.join(pieces)[5:], 2)
        packet = Literal(packet_version, value, remainder)
    else:
        length_type = int(binary[6])
        if length_type == 0:
            step = 15
            length_val = int(binary[7:7 + step], 2)
            tail = binary[7 + step + length_val:]
            pre_tail = binary[7 + step: 7 + step + length_val]
            packet = buildOperator(packet_version, type_id, tail)
            while pre_tail:
                inner_packet = generate_packet(pre_tail)
                pre_tail = inner_packet.tail
                packet.append(inner_packet)
        else:
            step = 11
            count_val, tail = int(binary[7:7 + step], 2), binary[7 + step:]
            packet = buildOperator(packet_version, type_id, tail)
            for idx in range(0, count_val):
                inner_packet = generate_packet(packet.tail)
                packet.tail = inner_packet.tail
                packet.append(inner_packet)
    return packet


if __name__ == '__main__':
    content = [element for element in helper.splitFile("day16.txt", "\n")][0]
    binary = ''.join([hex_to_bin(char) for char in content])
    packet = generate_packet(binary)
    summ = packet.get_version_sum()
    print(f"Result 1: {str(summ)}")

    vall = packet.get_value()
    print(f"Result 2: {str(vall)}")
