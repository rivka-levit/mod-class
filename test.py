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


class TestMod(TestCase):
    """Tests for Mod class functionality."""

    def setUp(self):
        self.mod = Mod(8, 3)

    def test_repr(self):
        """Test the __repr__ method."""

        expected = 'Mod(value=2, modulus=3)'
        self.assertEqual(repr(self.mod), expected)

    def test_str_method(self):
        """Test the __str__ method."""

        expected = 'Mod(2, 3)'
        self.assertEqual(str(self.mod), expected)

    def test_two_mod_equality(self):
        """Test to mod instances equality."""

        mod_1 = Mod(17, 3)
        mod_2 = Mod(18, 3)

        self.assertEqual(self.mod, mod_1)
        self.assertNotEqual(self.mod, mod_2)

    def test_mod_int_equality(self):
        """Test the equality of mod instance to an integer."""

        mod = Mod(9, 3)
        num = 11

        self.assertEqual(mod, num)

    def test_mod_int_not_equality(self):
        """Test not equal mod to an integer."""

        num = 11
        self.assertNotEqual(self.mod, num)

    def test_hash_method(self):
        """Test the __hash__ method."""

        expected = self.mod.value + self.mod.modulus
        self.assertEqual(hash(self.mod), expected)

    def test_hash_mods_with_different_modulus(self):
        """Test the __hash__ of two mods with the same value and different
        modulus."""

        s = {self.mod, Mod(14, 6)}
        self.assertEqual(len(s), 2)

    def test_int_return_residue(self):
        """Test the int function return residue."""

        expected = self.mod.value
        self.assertEqual(int(self.mod), expected)

    def test_add_two_mods(self):
        """Test adding two mod instances with the same modulus."""

        mod = Mod(11, 3)

        result = self.mod + mod

        self.assertIsInstance(result, Mod)
        self.assertEqual(result.value, 1)
        self.assertEqual(result.modulus, self.mod.modulus)

    def test_add_mod_to_int(self):
        """Test adding an integer to a mod instance."""

        new_mod = self.mod + 11

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_add_mod_to_float_error(self):
        """Test adding a float to a mod instance raises an error."""

        with self.assertRaises(TypeError):
            self.mod + 5.3

    def test_add_two_mods_with_different_modulus_error(self):
        """Test adding two mods with different modulus raises an error."""

        mod = Mod(11, 4)
        with self.assertRaises(TypeError):
            self.mod + mod
