from unittest import TestCase

from mod import Mod


class TestModClassInit(TestCase):
    """Tests for Mod class initialization"""

    def test_create_mod_successful(self):
        """Test creating a mod instance successfully."""

        v = 7
        m = 3

        mod_1 = Mod(v, m)

        self.assertEqual(mod_1.value, v % m)
        self.assertEqual(mod_1.modulus, m)

    def test_non_int_value_error(self):
        """Test creating a mod with non-int value raises an error."""

        v = 5.3
        m = 3

        with self.assertRaises(ValueError):
            Mod(v, m)

    def test_negative_modulus_error(self):
        """Test creating a mod with negative modulus raises an error."""

        v = 5
        m = -8

        with self.assertRaises(ValueError):
            Mod(v, m)

    def test_zero_modulus_error(self):
        """Test creating a mod with zero modulus raises an error."""

        v = 8
        m = 0

        with self.assertRaises(ValueError):
            Mod(v, m)
