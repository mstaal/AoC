from utils import AoCHelper as helper
from enum import Enum


class Packet:
    def __init__(self, packet_version, type_id):
        self.packet_version = packet_version
        self.type_id = type_id
        self.tail = None


class Literal(Packet):
    def __init__(self, packet_version, type_id, value, tail):
        super().__init__(packet_version, type_id)
        self.value = value
        self.tail = tail

    def __repr__(self):
        return f"(Type: {self.type_id}, Version: {self.packet_version}, Value: {self.value})"

    def get_version_sum(self):
        return self.packet_version


class Operator(Packet):
    def __init__(self, packet_version, type_id, length_type, operator_val, tail):
        super().__init__(packet_version, type_id)
        self.length_type = LengthType(length_type) if length_type is not None else None
        self.operator_val = operator_val
        self.tail = tail
        self.value = []

    def __repr__(self):
        return f"(Type: {self.type_id}, Version: {self.packet_version}, Length_Type: {self.length_type.name})"

    def get_version_sum(self):
        return self.packet_version + sum(val.get_version_sum() for val in self.value)

    def append(self, packet):
        self.value.append(packet)


class LengthType(Enum):
    total_length = 0
    number_of = 1


def hex_to_bin(h):
    b = f"{int(h, 16):b}"
    return '0' * (len(h) * 4 - len(b)) + b


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
        packet = Literal(packet_version, type_id, value, remainder)
    else:
        length_type = int(binary[6])
        if length_type == 0:
            step = 15
            length_val = int(binary[7:7 + step], 2)
            tail = binary[7 + step + length_val:]
            pre_tail = binary[7 + step: 7 + step + length_val]
            packet = Operator(packet_version, type_id, length_type, length_val, tail)
            while pre_tail:
                inner_packet = generate_packet(pre_tail)
                pre_tail = inner_packet.tail
                packet.append(inner_packet)
        else:
            step = 11
            count_val, tail = int(binary[7:7 + step], 2), binary[7 + step:]
            packet = Operator(packet_version, type_id, length_type, count_val, tail)
            for idx in range(0, count_val):
                inner_packet = generate_packet(packet.tail)
                packet.tail = inner_packet.tail
                packet.append(inner_packet)
    return packet


if __name__ == '__main__':
    content = [element for element in helper.splitFile("day16.txt", "\n")][0]
    binary = ''.join([hex_to_bin(char) for char in content])
    res1 = generate_packet(binary)
    summ = res1.get_version_sum()
    print(f"Result 1: {str(res1)}")
