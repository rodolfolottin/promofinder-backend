import sys
import os
import unittest

sys.path.insert(0, os.path.realpath('./') + '/..')


from twitter_handler import TwitterHandler, parse_link_from_text

class APITwitterHanderTest(unittest.TestCase):

    def setUp(self):
        self.app = TwitterHandler()

    def test_parse_link_from_text_end_of_line(self):
        text = "[Nespresso Benefit] Voltou! Cafeteiras com 40% OFF + 50 cápsulas. Frete Grátis Goiânia. https://t.co/jwVIhMUg9X"
        link_expected = "https://t.co/jwVIhMUg9X"
        result = parse_link_from_text(text)
        self.assertEqual(result, link_expected)

    def test_parse_link_from_text_middle_of_line(self):
        text = "[SUB] Moto Z Power Edition https://t.co/nY2Sekn35F R$ 2.079,20 em 1x Subcard"
        link_expected = "https://t.co/nY2Sekn35F"
        result = parse_link_from_text(text)
        self.assertEqual(result, link_expected)

    def test_parse_link_from_text_start_of_line(self):
        text = "https://t.co/nY2Sekn35F [SUB] Moto Z Power Edition R$ 2.079,20 em 1x Subcard"
        link_expected = "https://t.co/nY2Sekn35F"
        result = parse_link_from_text(text)
        self.assertEqual(result, link_expected)

    def test_parse_link_from_text_empty(self):
        text = ""
        link_expected = "Not known"
        result = parse_link_from_text(text)
        self.assertEqual(result, link_expected)

    def test_parse_link_from_text_none(self):
        text = None
        link_expected = "Not known"
        result = parse_link_from_text(text)
        self.assertEqual(result, link_expected)


if __name__ == '__main__':
    unittest.main()
