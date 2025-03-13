import unittest

from utils import find_matching_cidr

class TestIpInCidr(unittest.TestCase):
    def test_ip_inside_cidr(self):
        self.assertTrue(find_matching_cidr("10.0.0.100", "10.0.0.0/10"))
        self.assertTrue(find_matching_cidr("10.63.255.255", "10.0.0.0/10"))

    def test_ip_outside_cidr(self):
        self.assertFalse(find_matching_cidr("10.64.0.1", "10.0.0.0/10"))
        self.assertFalse(find_matching_cidr("192.168.1.1", "10.0.0.0/10"))

    def test_ip_at_network_boundary(self):
        self.assertTrue(find_matching_cidr("10.0.0.0", "10.0.0.0/10"))
        self.assertFalse(find_matching_cidr("10.64.0.0", "10.0.0.0/10"))

    def test_ip_with_spaces(self):
        self.assertTrue(find_matching_cidr(" 10.0.0.100 ", "10.0.0.0/10"))

    def test_invalid_ip(self):
        self.assertFalse(find_matching_cidr("999.999.999.999", "10.0.0.0/10"))
        self.assertFalse(find_matching_cidr("abcd", "10.0.0.0/10"))

    def test_invalid_cidr(self):
        self.assertFalse(find_matching_cidr("10.0.0.100", "10.0.0.0/99"))  # Invalid subnet mask
        self.assertFalse(find_matching_cidr("10.0.0.100", "abcd"))  # Non-numeric CIDR

if __name__ == "__main__":
    unittest.main()
