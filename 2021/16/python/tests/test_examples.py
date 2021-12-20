import unittest

import main


class ExampleTests(unittest.TestCase):

    def test_hex2bin(self):
        self.assertEqual('1111', main.hex2bin('F'))
        self.assertEqual('0001', main.hex2bin('1'))
        self.assertEqual('00011111', main.hex2bin('1F'))
        self.assertEqual('00000100', main.hex2bin('04'))

    def test_parse_literal(self):
        self.assertEqual((15, 2021),
                         main.parse_literal('101111111000101000'))

    def test_parse_packet(self):
        self.assertEqual(
            (21, {'version': 6,
                  'type_id': 4,
                  'literal': 2021}),
            main.parse_packet('110100101111111000101000'))

    def test_parse_packets(self):
        self.assertEqual(
            (27, [{'version': 6,
                   'type_id': 4,
                   'literal': 10},
                  {'version': 2,
                   'type_id': 4,
                   'literal': 20}]),
            main.parse_packets('1101000101001010010001001000000000'))

    def test_parse_operator_with_length(self):
        self.assertEqual(
            (43, [{'version': 6,
                   'type_id': 4,
                   'literal': 10},
                  {'version': 2,
                   'type_id': 4,
                   'literal': 20}]),
            main.parse_operator(
                '00000000000110111101000101001010010001001000000000'))

    def test_parse_operator_with_number(self):
        self.assertEqual(
            (45, [{'version': 2,
                   'type_id': 4,
                   'literal': 1},
                  {'version': 4,
                   'type_id': 4,
                   'literal': 2},
                  {'version': 1,
                   'type_id': 4,
                   'literal': 3}
                  ]),
            main.parse_operator(
                '10000000001101010000001100100000100011000001100000'))

    def test_parse_packets_more_examples_1(self):
        self.assertEqual(
            (69,
             [{'version': 4,
               'type_id': 2,
               'sub-packets':
                   [{'version': 1,
                     'type_id': 2,
                     'sub-packets':
                         [{'version': 5,
                           'type_id': 2,
                           'sub-packets':
                               [{'version': 6,
                                 'type_id': 4,
                                 'literal': 15}]}]}]}]),
            main.parse_packets(main.hex2bin('8A004A801A8002F478'))
        )

    def test_sum_versions(self):
        self.assertEqual(
            16,
            main.sum_versions(
                main.parse_packet(
                    main.hex2bin('8A004A801A8002F478'))[1]))

    def test_solve_more_examples_1(self):
        self.assertEqual(16, main.solve_part_1('8A004A801A8002F478'))

    def test_solve_more_examples_2(self):
        self.assertEqual(12, main.solve_part_1('620080001611562C8802118E34'))

    def test_solve_more_examples_3(self):
        self.assertEqual(23, main.solve_part_1('C0015000016115A2E0802F182340'))

    def test_solve_more_examples_4(self):
        self.assertEqual(31, main.solve_part_1('A0016C880162017C3686B18A3D4780'))

    def test_calculate_value_sum(self):
        self.assertEqual(3, main.solve_part_2('C200B40A82'))

    def test_calculate_value_product(self):
        self.assertEqual(54, main.solve_part_2('04005AC33890'))

    def test_calculate_value_min(self):
        self.assertEqual(7, main.solve_part_2('880086C3E88112'))

    def test_calculate_value_max(self):
        self.assertEqual(9, main.solve_part_2('CE00C43D881120'))

    def test_calculate_value_less_than(self):
        self.assertEqual(1, main.solve_part_2('D8005AC2A8F0'))

    def test_calculate_value_greater_than(self):
        self.assertEqual(0, main.solve_part_2('F600BC2D8F'))

    def test_calculate_value_equal(self):
        self.assertEqual(0, main.solve_part_2('9C005AC2F8F0'))

    def test_calculate_value(self):
        self.assertEqual(1, main.solve_part_2('9C0141080250320F1802104A08'))
