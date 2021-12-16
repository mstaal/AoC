from utils import AoCHelper as helper
from enum import Enum


class Packet:
    def __init__(self, packet_version, type_id):
        self.packet_version = packet_version
        self.type_id = type_id
        self.tail = None
        self.value = None


class Literal(Packet):
    def __init__(self, packet_version, type_id, value, tail):
        super().__init__(packet_version, type_id)
        self.value = value
        self.tail = tail

    def __repr__(self):
        return f"Type: {self.type_id}"

    def get_version_sum(self):
        return self.packet_version


class Operator(Packet):
    def __init__(self, packet_version, type_id, length_type, operator_val, tail):
        super().__init__(packet_version, type_id)
        self.length_type = LengthType(length_type) if length_type is not None else None
        self.operator_val = operator_val
        self.tail = tail

    def __repr__(self):
        return f"Type: {self.type_id}; Length_Type: {self.length_type.name}"

    def get_version_sum(self):
        return self.packet_version + sum(val.get_version_sum() for val in self.value)


class LengthType(Enum):
    total_length = 0
    number_of = 1


def hex_to_bin(h):
    b = f"{int(h, 16):b}"
    return '0' * (len(h) * 4 - len(b)) + b


binarymap = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


def generate_packet(binary):
    packet_version = int(binary[0:3], 2)
    type_id = int(binary[3:6], 2)
    length_type = int(binary[6])
    if type_id == 4:
        pieces = [binary[0:6]]
        remainder = binary[6:]
        continue_to_run = True
        while continue_to_run:
            if remainder[0] == '0':
                continue_to_run = False
            pieces.append(remainder[1:5])
            remainder = remainder[5:]
        value = int(''.join(pieces)[5:], 2)
        packet = Literal(packet_version, type_id, value, remainder)
    else:
        if length_type == 0:
            step = 15
            inner_values = []
            operator_val = int(binary[7:7 + step], 2)
            tail = binary[7 + step: 7 + step + operator_val]
            packet = Operator(packet_version, type_id, length_type, operator_val, tail)
            while len(tail) >= 11:
                inner_packet = generate_packet(tail)
                tail = inner_packet.tail
                inner_values.append(inner_packet)
            packet.value = inner_values
        else:
            step = 11
            inner_values = []
            count_val = int(binary[7:7 + step], 2)
            tail = binary[7 + step:]
            packet = Operator(packet_version, type_id, length_type, count_val, tail)
            for idx in range(0, count_val):
                inner_packet = generate_packet(tail)
                tail = inner_packet.tail
                inner_values.append(inner_packet)
            packet.value = inner_values
    return packet


if __name__ == '__main__':
    content = [element for element in helper.splitFile("day16.txt", "\n")][0]
    binary = ''.join([hex_to_bin(char) for char in content])
    res1 = generate_packet(binary)
    summ = res1.get_version_sum()
    print(f"Result 1: {str(res1)}")
